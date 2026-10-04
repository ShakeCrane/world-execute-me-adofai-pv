"""Full v03 blocking export, selected-frame proof, four high-risk clips.
No network/audio download. Encoder must already be available locally.
"""
from pathlib import Path
import argparse,hashlib,json,os,platform,random,shutil,subprocess,sys
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
import PIL
from PIL import Image,ImageDraw
from film.deltarune_poc import renderer as r,dr_ui as ui
from film.deltarune_poc.lyric_scenes import execution_state
OUT=ROOT/'out/deltarune_v03'
RANGES={'P1_handoff_protect':(3821,4072),'P2_absence_reentry':(2650,2838),'P3_creation_normal':(0,715),'P4_love_recursion':(4259,5086)}
CONTACTS={
 'P1': [3902,3915,3938,3962,3988,4000,4012,4020,4030,4040,4052,4064],
 'P2': [2650,2662,2674,2693,2728,2754,2784,2837,4072,4100,4138,4163],
 'P3': [1,43,93,130,156,200,242,251,269,432,535,655],
 'P4': [4259,4319,4344,4430,4442,4460,4519,4543,4601,4734,4814,5085],
 'EXEC12':[a['frame']+min(11,3820-a['frame']) for a in r.PLAN['execution_pulse_anchors']]}

def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def pixel(im):return hashlib.sha256(im.tobytes()).hexdigest()
def ffmpeg():
    exe=shutil.which('ffmpeg')
    if exe:return exe
    candidates=list((ROOT/'out/dr_runtime/imageio_ffmpeg/binaries').glob('ffmpeg*.exe'))
    if not candidates:raise RuntimeError('Local ffmpeg required. No automatic network install.')
    return str(candidates[0])
def run(cmd):
    p=subprocess.run(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
    if p.returncode:raise RuntimeError(p.stderr.decode('utf-8',errors='replace')[-3000:])
    return p

def contacts(name,frames):
    cols=3;tw,th,cap=426,240,28
    image=Image.new('RGB',(cols*tw,((len(frames)+cols-1)//cols)*(th+cap)),(15,22,33));d=ImageDraw.Draw(image)
    for i,n in enumerate(frames):
        x=i%cols*tw;y=i//cols*(th+cap)
        image.paste(Image.open(OUT/'stills'/f'{n:05d}.png').resize((tw,th),Image.Resampling.LANCZOS),(x,y))
        d.text((x+8,y+th+5),f"{r.shot_at(n)['id']}  f{n}  {n/24:.3f}s",font=ui.font(ui.MONO,16),fill=(201,215,224))
    image.save(OUT/f'{name}_contact.png')

def stills():
    frames=set()
    for s in r.PLAN['shots']:
        a,b=s['start_frame'],s['end_frame'];frames.update([a,min(a+12,b-1),(a+b)//2,b-1])
    for ns in CONTACTS.values():frames.update(ns)
    frames.update(range(4000,4041,2));frames.update(range(2650,2694,2));frames.update(range(4430,4461,2));frames.update(range(4962,4996))
    frames.update([1774,1865,1951,2043,2080,2124,2838,2885,2928,3014,3093,3149,3231,1637,1667,1682]);frames.update([1718,1773,1865,1902,2043,2080,2124,848,863,889,1000,1040])
    CONTACTS['REPAIRS']=[200,242,269,1637,1667,1718,1865,1902,4344,4448,848,1000]
    (OUT/'stills').mkdir(parents=True,exist_ok=True);records=[];expected={}
    for n in sorted(frames):
        im=r.frame(n);assert im.mode=='RGB' and im.size==(1280,720);im.save(OUT/'stills'/f'{n:05d}.png');expected[n]=pixel(im)
        records.append(dict(frame=n,shot=r.shot_at(n)['id'],pixel_sha256=expected[n],file=(OUT/'stills'/f'{n:05d}.png').relative_to(ROOT).as_posix(),png_sha256=sha(OUT/'stills'/f'{n:05d}.png')))
    shuffled=list(frames);random.Random(20261004).shuffle(shuffled)
    for n in shuffled:assert pixel(r.frame(n))==expected[n],f'Order dependent frame {n}'
    for n in range(4970,4994):assert r.frame(n).getbbox() is None
    assert r.frame(4969).getbbox()[3]-r.frame(4969).getbbox()[1]==1
    assert r.frame(4994).getbbox() is not None and r.frame(5085).getbbox() is not None
    for n in [-1,5086,1.5,True,None]:
        try:r.frame(n)
        except ValueError:pass
        else:raise AssertionError(f'Unsupported input accepted: {n}')
    for n in [3902,3962,4000,4030,4052,4064]:assert r.frame(n).getpixel((98,101))==(240,68,98),'Input source must remain visible despite camera'
    assert len({execution_state(a['frame'],r.PLAN)[1]['mode'] for a in r.PLAN['execution_pulse_anchors']})==12
    for name,ns in CONTACTS.items():contacts(name,ns)
    for i in range(0,38,9):contacts(f'FULL_{i//9+1}',[(s['start_frame']+s['end_frame'])//2 for s in r.PLAN['shots'][i:i+9]])
    contacts('P1_motion',list(range(4000,4041,2)))
    contacts('P2_motion',list(range(2650,2694,2)))
    contacts('P4_motion',list(range(4430,4461,2)))
    return records

def encode(exe,start=0,end=5086,filename="full_rough_v03_silent.mp4"):
    dest=OUT/filename;err=OUT/(filename+'.log')
    cmd=[exe,'-hide_banner','-loglevel','error','-y','-f','rawvideo','-pix_fmt','rgb24','-s','640x360','-r','24','-i','pipe:0','-an','-c:v','libx264','-preset','fast','-crf','20','-pix_fmt','yuv420p','-movflags','+faststart',str(dest)]
    seen={s['id']:set() for s in r.PLAN['shots'] if s['start_frame']<end and s['end_frame']>start};chain=hashlib.sha256()
    with err.open('wb') as e:
        proc=subprocess.Popen(cmd,stdin=subprocess.PIPE,stderr=e,creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
        try:
            for n in range(start,end):
                im=r.frame(n);h=pixel(im);seen[r.shot_at(n)['id']].add(h);chain.update(bytes.fromhex(h));proc.stdin.write(im.resize((640,360),Image.Resampling.BILINEAR).tobytes())
                if n%480==0:print(f'Rendered {n}/5086 ({n/24:.1f}s)',flush=True)
            proc.stdin.close();code=proc.wait()
        except BaseException:
            proc.kill();proc.wait();raise
    if code:raise RuntimeError(err.read_text(encoding='utf-8',errors='replace'))
    assert all(len(v)>1 for v in seen.values()),'A whole shot is an unchanging still'
    print(f'Encoded {filename}: {end-start} original frames',flush=True)
    # Decode the actual file; count_frames is encoder-independent verification.
    probe=run([exe,'-hide_banner','-i',str(dest),'-map','0:v:0','-fps_mode','passthrough','-f','null','-'])
    info=probe.stderr.decode('utf-8',errors='replace')
    import re
    matches=re.findall(r'frame=\s*(\d+)',info);assert matches and int(matches[-1])==end-start
    assert '640x360' in info and '24 fps' in info and 'Audio:' not in info
    if start==0 and end==5086:
        run([exe,'-hide_banner','-loglevel','error','-y','-i',str(dest),'-vf',r'select=eq(n\,4012)','-frames:v','1',str(OUT/'decoded_f04012.png')])
    return dict(file=dest.relative_to(ROOT).as_posix(),sha256=sha(dest),decoded_frames=end-start,fps=24,resolution=[640,360],duration_seconds=(end-start)/24,audio_tracks=0,original_pixel_hash_chain=chain.hexdigest(),unique_frames_by_shot={k:len(v) for k,v in seen.items()})

def clips(exe):
    ranges=dict(RANGES);ranges['P2_reentry']=(4072,4164)
    records=[]
    for name,(a,b) in ranges.items():
        result=encode(exe,a,b,name+'.mp4')
        records.append(dict(name=name,source_range=[a,b],frames=result['decoded_frames'],file=result['file'],sha256=result['sha256']))
    return records

def manifest(records,video=None,clip_records=None):
    sources=[Path(__file__),ROOT/'tools/design_deltarune_plan.py',*sorted((ROOT/'film/deltarune_poc').glob('*.py'))]
    report=dict(design_version='0.3',technical_passed=True,errors=[],renderer_sources={p.relative_to(ROOT).as_posix():sha(p) for p in sources},plan_sha256=sha(ROOT/'data/deltarune_shot_plan.json'),stills=records,shuffle_replays=len(records),supported_range=[0,5086],hard_cut_black_frames_checked=24,unsupported_inputs_rejected=5,independent_execution_states=12,
    runtime=dict(python=platform.python_version(),Pillow=PIL.__version__,font_path=str(ui.FONT_FILE),font_sha256=sha(ui.FONT_FILE)),video=video,clips=clip_records or [],audio_review='PENDING',art_review='NEXT HUMAN ART GATE',visual_review='docs/deltarune/11_BLOCKING_REVIEW.md; technical checks alone do not prove direction',limitations=['Silent rough only','Original geometry, not final character art','Game visual R01–03 pending','No real-time full playback or audio listening claim'])
    (ROOT/'data/deltarune/poc_validation_v03.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    return report

def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--stills-only',action='store_true');args=parser.parse_args()
    records=stills();print(f'{len(records)} stills + shuffled replay checks passed',flush=True)
    if args.stills_only:manifest(records);return
    exe=ffmpeg();video=encode(exe);clip_records=clips(exe);manifest(records,video,clip_records)
    print(json.dumps(dict(technical_passed=True,video=video['file'],frames=video['decoded_frames'],clips=len(clip_records)),ensure_ascii=False))
if __name__=='__main__':main()
