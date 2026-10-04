> 历史设计/研究记录（v0.1或暂停v0.2）：保留材料，不是当前上位分镜。当前歌词导演依据见09_LYRIC_DIRECTOR_LEDGER、10_DIRECTOR_REWRITE、06 v0.3与STATUS。旧镜数/排期/PoC范围不代表当前状态。

# 从镜头稿到可执行画面

2026-10-01。先完成00–06再进入此映射。全部67镜的复用源、待建函数、assets、关键帧在JSON中逐镜记录；本文规定这些符号如何落地，避免把“planned”读成“已实现”。原renderer、DSH frontend、patch和许可文件保留，不把DR编号当旧ALL index。

## 技术选择

新建独立 `film/deltarune_poc/` 作为最小实验入口，使用PIL生成原创图形。`frame(n)` 接收整数帧，禁止依赖上一帧；每次从同一scene状态重新合成。先验证K08/K09/K10/K11，再决定生产section入口，不先改顶层build.py。

| 工作层 | 直接复用/换数据 | 新组件及边界 | 不适用之处 |
|---|---|---|---|
| clock | 原24fps、word_onset→整数帧、4970硬切 | `dr_timeline`：shot lookup、事件区间、无状态插值 | 原211s/5064帧历史值不能混入5086帧DR版本 |
| 画布/文字 | PIL、tuikit的字体/alpha/post接口可选 | `dr_ui`：choice、SAVE、dialogue、主体pane；先本机字体不打包 | 旧DeepSeek字号/品牌/原聊天文本不用换皮沿用 |
| 角色/世界 | kit透明carrier与固定锚点原则 | `dr_layers`：身体/手、SOUL、world、chrome分别合成 | 不调用原H3 dancer，也不以鲸鱼placeholder充当Kris |
| transitions | cuts的content/over分离、FULL_ART滑入、SPLIT读区思路 | `dr_timeline`输出固定几何，carrier跨界不被内屏裁掉 | 旧scene名REPLACE和旧ALL index不属于新shot身份 |
| post | tuikit低强scanline/glow可以复用 | 每镜可关闭，黑场无post残影；使用同一输入时刻 | 原finish vignette/聊天提示/高亮不能默认套用 |
| frontend | 原Playwright截帧的固定viewport、等待font/image机制 | 只有长排版/嵌套网页真的需要时另建DR HTML | 当前选项框和几何世界用PIL更直接；保留旧HTML作为历史参照 |
| encode | 原lossless master与BT.709 delivery流程后期可复用 | DR入口显式frame_count与自备音频；字幕本地恢复 | 先不render全片，不自动导入原song+chime混音 |

旧组件需要的monkey patch：**本轮为零**。若生产阶段接入v2，先新增独立SECTIONS和ALL，再逐项审查是否需要OWN/OVERLAY；禁止用所有旧patch_install堆栈给新片自动注入原叙事。可以在新adapter中调用稳定工具函数，无需重写旧v2。

## 每镜执行路线

下表按连续镜头组给出路线；逐镜细节取JSON的 `original_repo_components_reused` / `new_code_required` / `assets_required`。所有组都保留本机still校验，暂无必须由HTML实现的镜头。section按关系变化分组，避免章节成为剪辑顺序。

| Shot | 新section/主要组件 | PIL/TUI实现 | HTML / 预渲染 | 可复用抽象 |
|---|---|---|---|---|
| DR01–08 | `s_dr_connect`、control_pane、vessel、kris_study | 主体拼装/框/心/替换 | 生产原创角色可透明PNG；无网页需要 | identity_transition，同一个SOUL锚点 |
| DR09–12 | `s_dr_normal`、party、save_slot | 动作拒绝/合作/slot名字覆盖 | 以后角色动作可预渲染；不可假造SAVE记忆日志 | party_response、slot/name分层 |
| DR13–20 | `s_dr_identity` / `s_dr_nested` / `s_dr_normal`、choice_ring、inner_game | 身体/数学几何/TV/SAVE空间 | 稀疏图形无HTML价值 | world_clip与carrier独立、control_target |
| DR21–24 | `s_dr_normal`、choice_paths、wire | 合作靠近与最后wire落下 | NEO原创剪影/线动作可预渲染 | path_offer不等于结果，线与角色分层 |
| DR25–28 | `s_dr_care`、organ、party、save_slot | 手/送行/能力/身份叠层 | 创作角色表演PNG序列可替换study | character_action而非只换menu数据 |
| DR29–33 | `s_dr_care` / `s_dr_nested` / `s_dr_normal`、world_palette、party | Light/Dark切换与合拍 | 原创布景asset可选；无原游戏导出 | colour_state、same_character_anchor |
| DR34–39 | `s_dr_separation`、hand、soul、cage/vent | 连续取心/拆UI/心可动身体另动 | 生产手部asset保持同锚点；无HTML | independent_body_input，K02连续事件 |
| DR40–42 | `s_dr_separation` / `s_dr_weird`、dialogue、physical_choice | 门内私话/门外心/重入 | 涉及精确游戏布局前先完成R02画面核对 | choice_object能进入世界而非平面字幕 |
| DR43–45 | `s_dr_weird`、path_gate、ring、recoil | 条件收窄/红裂/反冲 | ring只抽象意象，不导出游戏素材 | gate、contact_crack、K04 |
| DR46–48 | `s_dr_weird` / `s_dr_nested`、DOWN、shelter、outer_frame | 声音与身体来源分离/输入冲突/框越界 | R01前不复刻小游戏动作 | nested_control与背景mask分离 |
| DR49–51 | `s_dr_execution`、pulse_index、subject_label | 原唱词起音驱动12次收窄与计数 | 无12张杀敌截图；无HTML | timing事件索引，跨镜复用同choice对象 |
| DR52–54 | `s_dr_execution`、hero_carrier、protect、blank_choice | 出屏控制保持/拉开Susie/拔线/空选项 | 原创HERO动作序列可选；需R01核对 | under/over/carrier，K06/K07 |
| DR55–58 | `s_dr_reverse`、slow_body、hand、choice | 身体慢移/Noelle引路/同文菜单 | 本轮PoC直接PIL，未来R03核对原布局 | independent selector、K08文字退/入 |
| DR59–60 | `s_dr_reverse`、input_halt、branch_residue | 停输入出口和既往关系留痕 | 图形交叉是作者隐喻，不称游戏菜单 | 选择之外的时限，K09 |
| DR61–63 | `s_dr_boundary`、world_in_frame、chapter | 三层框收束与世界保留 | 以后原创湖面asset可预渲染 | 不缩角色识别尺寸的world缩框 |
| DR64–67 | `s_dr_final`、hard_cut、chapter_boundary、question | 4970全黑→SideB要求→Kris手与心→作者问题 | 无真实Chapter7画面，禁止生成未来剧情 | K10/K11，黑场与末帧hold |

## 最小实现顺序与验收

1. **当前PoC**：DR57–60，连续4344–4654；DR64–67，4929–5086。不声称整片可渲染。固定body/心/choice可读区，保存反转前/中/后、情绪peak4495、停止输入、硬切两侧、最后帧。无音频预览只验画面与原frame timing，听音不标通过。
2. 跨屏控制DR52–53：先两个still看清control_target未变，再24帧短range看Kris保护先于Susie断线；R01核对后才做精确游戏动作。
3. SOUL分离DR34–39及重入DR42：同一心、身体/输入可不同步；黑边/光效不遮手。R02影响的是游戏复刻，抽象机制可先验证。
4. 开头与Normal回访DR01–33：Kris形象、美术接受度与合作气质先验收，再扩成其他section；避免只有Weird镜头实现得精细。
5. 十二pulse、反冲、chapter收束：分别验证音乐锚点/动作/读区，再整段低清review；自备音频到位后听音修订时刻，不擅自下载歌曲。
6. 各section通过后再接生产入口、全片、lossless和delivery。未完成的画面不得以原DSH画面填洞。

每次输出manifest包含shot_id、frame/time、分辨率、renderer源码hash、plan hash、PNG hash、检查结论。随机顺序渲染同帧须同hash；同时检查图像文字/手/心，不把数值通过当艺术验收。`tools/validate_deltarune_plan.py`负责全时间轴和证据引用，PoC工具负责渲染与确定性。

## 已知限制

R01–03尚无本地游戏连续录像核验，研究页记录了已读脚本/转录与未观看视频。没有自备歌曲，所以无声音同步/情绪节奏最终验收。程序轮廓是原创study而非最终角色美术。生产完整211.9s PV仍需继续实现，本轮不更改原build默认入口或发布任何成片。

