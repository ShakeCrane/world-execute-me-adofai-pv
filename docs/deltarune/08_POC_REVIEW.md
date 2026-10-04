> 历史设计/研究记录（v0.1或暂停v0.2）：保留材料，不是当前上位分镜。当前歌词导演依据见09_LYRIC_DIRECTOR_LEDGER、10_DIRECTOR_REWRITE、06 v0.3与STATUS。旧镜数/排期/PoC范围不代表当前状态。

# 最小画面研究与验收记录

2026-10-01；独立PIL入口 `film/deltarune_poc/renderer.py`。这是原创程序化二创study，AI参与代码/导演文档，美术未使用ImageGen或游戏导出素材。许可证与provenance见05及asset清单。不是完整成片或原游戏画面复刻。

## 输出与范围

- DR57–60局部关系机制：4344–4654 exclusive，12.917s。
- DR64–67结尾机制：4929–5086 exclusive，6.542s。
- 原尺寸still：1280×720/24fps，共104张，含菜单变形、selector移动、停止输入、hardcut、手/心显现的逐帧序列。
- 两段640×360/12fps无声lossless WebP：`out/deltarune_poc/menu_preview.webp`、`ending_preview.webp`。毫秒duration累计取整，不以每帧83ms累计漂移；对应原始整数帧时刻。
- 九格比较：`menu_contact.png`、`ending_contact.png`；完整still用五位帧号PNG定位。
- 可追溯技术manifest：`data/deltarune/poc_validation.json`，含源码/plan/font/PNG与像素hash、runtime、每张的shot/time。

输出目录按原.gitignore排除；生成步骤和技术manifest在仓库。没有把生成歌词、音频或游戏脚本加入Git。入口遇到其他frame、float或bool时拒绝，不返回旧DSH画面假装完成。

## 目视检查：哪些读到了

已实际打开两张contact sheet、1280原图4495/4543/4969，并在修正后复查4495/4601/ending contact。逐帧状态由manifest交叉核对；没有听音，也没有声称已播放完整游戏录像。

| 检查点 | 观察 / 结论 | 限制 |
|---|---|---|
| 4344、4418 | Stop和Proceed可读，心在左；Kris身体/衣色为主要面积，Noelle远景为镜子 | 未做Noelle完整牵腕表演，不能代替E32游戏视觉 |
| 4436–4448 | 左字退去再变成Proceed，框和心在变形中保留 | 明确是PV压缩，不重演前6/第7组全部对白 |
| 4448、4454、4460 | 红心从左到右可读，身体不随selector位移换向 | 角色手势情感仍是几何study，最终美术要重验 |
| 4495 | 单一伸手轮廓、绿色衣带、菜单及连接同时可读；无脸部“恶笑” | 手牌不能独自说明Kris动机，不据此写其仇恨Player |
| 4519–4543 | 文本/框退去，红心和身体仍存在；灰线分支与关系影子留下 | 二分图是作者比较，不是新增游戏菜单；影子的Susie识别度不足，生产阶段需要明确原创造型 |
| 4574、4601 | 继续侧重新要求Proceed，收框节奏缩短；心趋白但保留红轮廓，停止侧痕迹不删 | 压缩两次deadline，不是原游戏每组严格单调倒计时 |
| 4969→4970 | 最后一条1px线→纯黑，未叠原chime提示 | 还没有自备歌曲，实际音乐硬切需听音检查 |
| 4994 | Side B章要求位于黑场中央，未来未画出来 | 文本游戏转录待R03画面核对，非官方启动界面 |
| 5028、5057、5085 | 角色的手/红心/未闭框留下，作者问题不遮主体并保持至末帧 | 没有给未发布后续章或角色生死定论 |

第一轮明确修正：4495附近原来重复叠画两只手，改成同一角色手的参数变化；收缩原来在4969仍有68px高，改成该帧1px；停止输入后的黑色残余box删除；继续侧补上confirmation收框/红轮廓，避免把DR60留成静态分支图。这些修正已经重新渲染，不沿用旧hash。

**本轮通过的是机制可读性和确定性。** 单镜成立不等于全片情绪成立；没有把104张still都称为人工逐一艺术验收。尚未渲染DR55起床、DR56完整引路或DR61–63递归框；目前两段之间不连播成“完整尾段”。

## 技术结果

104个selected frame按固定seed乱序重画，像素hash一致。4970–4981共12帧为完全黑；4969与5085非黑。8个非法/超范围输入被拒绝。先后selector位移174px，而相同时段身体变化小于2px。输出规格为RGB1280×720。游戏tick没有当24fps PV frame用。

全曲plan另经独立原word timeline重算：67镜连续覆盖[0,5086)，395锚点、98非空唱词行、36 evidence引用、11连续事件；DR49/50各六次执行起音。原baseline75个Python文件内容hash（LF归一化）保持一致。该检查不等于原全工程build成功。

## 重现

使用有Pillow的Python，以及本机Windows Consolas；font文件不再分发。当前机器已用Codex bundled Python成功执行以下步骤。无需恢复歌词或提供音频即可重现PoC，歌词隐私扫描可选使用已忽略的本地LRC。

```powershell
python tools/audit_deltarune_baseline.py
python tools/design_deltarune_plan.py
python tools/validate_deltarune_plan.py
python tools/render_deltarune_poc.py
```

Windows以外的生产适配需明确改用已许可字体并保存新font hash，不能声称换字体后像素hash不变。Pillow或字体版本变化也需重新记录视觉结果。

## 后续执行优先级

下一段优先DR52–53的control handoff：对象走出TV时Player仍指挥HERO，Kris先拉开Susie，Susie再断线。它验证“角色拒绝”与“玩家失去所有自由”是否被错误混同。随后做DR34–39同一SOUL分离和Normal开头，验证warm合作与后半施压的对比。最终美术、R01–03游戏画面、听音与全片节奏均保持未验收。

