"""Small, asset-independent primitives for authored pixel scenes.

Coordinates use x/right, y/up, z/away. These helpers provide projection and
raster placement only; scene geometry, occlusion and artistic choices belong
to the calling shot. Pillow and NumPy are the only dependencies.
"""
import math

import numpy as np
from PIL import Image


def walk_frame_index(distance, distance_per_pose, frame_count, moving=True):
    """Choose a pose from travelled distance without previous-frame state.

    Distance must be nonnegative; the caller calibrates stride and supplies
    ordered source frames. A stopped character uses pose zero.
    """
    if distance < 0 or distance_per_pose <= 0 or frame_count <= 0:
        raise ValueError("Expected nonnegative distance and positive interval/count")
    return int(distance / distance_per_pose) % frame_count if moving else 0


def raster_at_foot(source, foot, projected_height):
    """Return (RGBA raster, top-left) using nearest sampling and integer placement.

    Aspect ratio comes from the source canvas. The pivot is its bottom centre,
    not a detected anatomical foot; transparent margins must be checked per
    source. Depth-related integer size steps remain visible by design.
    """
    height = round(projected_height)
    if height < 1:
        raise ValueError("Projected height must round to at least one pixel")
    width = max(1, round(height * source.width / source.height))
    sprite = source.convert("RGBA").resize((width, height), Image.Resampling.NEAREST)
    fx, fy = map(round, foot)
    return sprite, (fx - width // 2, fy - height)


def perspective_camera(aim, distance, yaw, pitch, focal, center):
    """Return a pure world-point -> screen-point projection.

    Angles are degrees. This does not clip geometry; every submitted point
    must lie in front of the camera. Keep pitch away from +/-90 degrees.
    Units are authored scene units, not DELTARUNE room coordinates.
    """
    if distance <= 0 or focal <= 0 or abs(pitch) >= 90:
        raise ValueError("Expected positive distance/focal and abs(pitch) < 90")
    yaw, pitch = map(math.radians, (yaw, pitch))
    aim = np.array(aim, float)
    forward = np.array([
        -math.sin(yaw) * math.cos(pitch),
        -math.sin(pitch),
        math.cos(yaw) * math.cos(pitch),
    ])
    eye = aim - forward * distance
    right = -np.cross(forward, [0, 1, 0])
    right /= np.linalg.norm(right)
    up = np.cross(forward, right)

    def project(point):
        q = np.array(point, float) - eye
        depth = float(q @ forward)
        if depth <= 0:
            raise ValueError("Point lies on or behind the camera plane")
        return (
            center[0] + focal * float(q @ right) / depth,
            center[1] - focal * float(q @ up) / depth,
        )

    return project


def paste_quad(canvas, texture, points, project):
    """Nearest-project one RGBA texture onto an ordered planar quadrilateral.

    Corners are top-left, top-right, bottom-right, bottom-left. Mutates the
    RGBA canvas and returns projected corners. Painter order is the caller's
    responsibility; this is not a depth buffer or a general mesh renderer.
    Degenerate quads are rejected by the homography solver.
    """
    dst = np.array([project(p) for p in points], float)
    src = [(0, 0), (texture.width, 0),
           (texture.width, texture.height), (0, texture.height)]
    matrix, target = [], []
    for (x, y), (u, v) in zip(dst, src):
        matrix.extend([
            [x, y, 1, 0, 0, 0, -u * x, -u * y],
            [0, 0, 0, x, y, 1, -v * x, -v * y],
        ])
        target.extend([u, v])
    coeff = np.linalg.solve(matrix, target)
    transformed = texture.convert("RGBA").transform(
        canvas.size, Image.Transform.PERSPECTIVE, coeff, Image.Resampling.NEAREST
    )
    canvas.alpha_composite(transformed)
    return dst.tolist()
