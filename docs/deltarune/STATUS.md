# 当前范围：只分析剧情与分镜

更新2026-10-04；以用户最新指示为准：**本轮不做任何艺术加工，只分析剧情和分镜。**

有效依据：作者最新创作意图 → 01事实边界 → 02反证 → [最低理解参考](../DR_PV_MINIMUM_STORY_REFERENCE.md) → 歌词英语结构/精确timing → 历史03–08及PoC。旧方案不因已经实现而获得设计优先权。

## 当前交付

| 文件 | 内容 |
|---|---|
| 09_LYRIC_DIRECTOR_LEDGER.md | 98非空唱词行逐行关键词、英语语义、条件句/代词、双关、DR关系、可能分镜、误读边界及确认项 |
| 10_DIRECTOR_REWRITE.md | 全67旧镜去向；五幕结构、情绪曲线、每10–20秒观看问题、motif三次变义、Hero/Support/Breath/Transition预算与15项自检 |
| 06_SHOT_BIBLE.md / data/deltarune_shot_plan.json | v0.3，38镜连续5086帧；每镜剧情目的、主体、空间、动作、剪辑与事实限制 |
| tools/design_deltarune_plan.py | 同一source of truth生成上述三文档与JSON，避免漂移 |
| data/deltarune/plan_validation.json | 395原逐词锚点/98唱词行、67旧镜去向、36证据ID、38镜连续时间与原75代码文件的独立核对，通过 |

本轮主要重构：Vessel具体部件/参数→丢弃空位→另处既存Kris；真实合作与自愿给予；数学建模不穷尽主体；探索到内容消费渐变；首Execution中性善意；God权力也依赖世界回应；一次持续absence；Fragments目标剪枝；God/arguments双层冲突；十二次关系状态变化；Love先感情本义；先Player能停止，再显上游章界。

## 范围与待项

- 只讨论剧情、歌词、分镜、构图意图、动作意图与剪辑结构；不执行画面加工、角色美术、素材生成或艺术验收。
- 先前生成的几何PoC与无声rough保留为历史机制材料，不是当前交付或完成标准。11_BLOCKING_REVIEW.md已标为历史；不再继续渲染。旧媒体manifest不绑定最新分析源表，不以旧hash或截图声称本轮验收。
- 歌词timing保留，但没有自备歌曲与实际听音：AUDIO REVIEW PENDING。
- R01–03原游戏画面/build核对未做；事实、推论、作者隐喻边界保持分开。
- 任何后续艺术实施需在用户另行启动的独立轮中，由用户作为art gate把关；当前不自动进入。
- 原baseline75个Python文件、LICENSE、NOTICE.md和默认build未改；未使用任何reset/paid/additional credit。

## 当前重现

```powershell
python tools/design_deltarune_plan.py
python tools/validate_deltarune_plan.py
```

当前验收是分析结构、数据连续和事实引用；不运行渲染或--require-full。源表中的历史mechanism路径只用于定位参考，不是本轮实施任务。档案v01/v02及历史00–05/07/08/09_DIRECTOR_REVIEW的旧镜数、计划、画面研究不能覆盖当前上位设计。
