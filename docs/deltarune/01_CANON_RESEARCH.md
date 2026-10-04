# 剧情证据库：Who executes whom?

查证日 2026-10-01；范围 Chapter 1–5（全部已发布，[官网](https://deltarune.com/)、[Chapter 5 官方发布公告](https://toby.fangamer.com/newsletters/ch5-release-date/)）。全文是研究笔记，有完整剧透。

## 证据纪律与查证边界

CANON=可见游戏事件、可定位游戏文本/机制或官方确认；STRONG_INFERENCE=多项事实支持但未直说；INTERPRETATION=本 PV 的主题解释；THEORY=社区可争论模型；SPECULATIVE=证据不足。**命题类别与本次验证强度是两条轴**：Wiki 转录的游戏事实可登记为 CANON，但不假装已经亲自游玩/看完录像。以下 confidence 高/中指检索证据可靠度，不是角色动机的概率。

本机没有游戏本体，未购买/下载游戏，未对游戏进行操作。已读官方页面、独立 Wiki 的章节/人物/机制页及其脚本引用链；Chapter 5 湖边三个脚本已直接读取公开 script viewer（社区托管的反编译游戏代码，不是官方源码，平台/构建号未明确），关键机制已交叉核对。游戏录像仅作为待验收 locator，未宣称视觉观看已完成。最终角色动作/对白/场景布局前仍需指定版本的画面核对；几何 PoC 可先验证设计。

不要从 Wiki 的叙述主语自动推导角色的本体论。Noelle 区分声音是事实；Noelle 知道人类玩家/显示器/游戏外世界则不是同一个命题。Kris 拒绝动作不自动证明 Kris 知道人类玩家；Shadow Mantle holder 的指控也不是全知叙述者的认证。

## 可追溯记录

来源代码见下一节。每行均提供 Chapter / Route / Scene / Fact / Evidence locator / Source / Confidence / 主题作用。

| ID | Ch / Route / Scene | Fact（只陈述可见或文本事实） | Evidence locator / Source | 等级 / Confidence | Narrative relevance |
|---|---|---|---|---|---|
| E01 | 1 / opening / vessel | 自定义 vessel 后，被告知舍弃；随后切到 Kris 的卧室 | Introduction Survey/Conclusion，S01 | CANON / 高（转录） | 输入可定制形体，却不能选择本片主体 |
| E02 | 1 / normal / first SAVE | 首次保存前 slot 显示 Kris，首次 SAVE 改为 creator name | SAVE Trivia，S02 | CANON / 高（转录） | 名字写入不等于身份合并 |
| E03 | 1 / normal / initial battles | Susie 初期自动攻击，不接受其他战斗命令；加入后可指挥 | Susie In battle，S03 | CANON / 高（转录） | Character agency 会变，不是永久免控 |
| E04 | 1 / ending / bedroom | Kris 拔出 SOUL 放入鸟笼；玩家仍可移动心，不能指挥 Kris | SOUL Ch1，S04 | CANON / 高（转录） | 控制对象和角色身体可分离 |
| E05 | 2 / normal / sink and ending | Kris 将 SOUL 暂时藏于水槽下；章末自主取出，随后创建 Fountain | SOUL Ch2，S04 | CANON / 高（转录） | 不依赖输入的行动不一定善良/反抗 |
| E06 | 2 / normal / NEO wires | 切最后一根线后 NEO 身体坠落，随后变为可用装备 | NEO Main story，S05 | CANON / 高（转录） | 去掉约束不保证可行动，保留自由的代价 |
| E07 | 2 / normal / NEO aftermath | Kris 对战后问题的回应带明显情绪；Susie 察觉异常 | Kris 人物行为/NEO aftermath，S06 | CANON / 中（人物页汇总） | 同一个被选答案存在角色表达差异 |
| E08 | 2 / weird / backtracking | 路线要求返回、规定 IceShock finishing 与指定选择；其他解法会中止 | WR2 Method/Requirements，S07 | CANON / 高（转录） | 偏离主线仍遵循严格程序 |
| E09 | 2 / weird / Berdly battle | Kris DOWN 时 Noelle 仍说听到声音 | WR2 Stage6，S07 | CANON / 高（转录） | 声音不能简单等同身体状态；非 Player 身份确认 |
| E10 | 2 / weird / SnowGrave | 多次命令越过 Noelle 拒绝，最终冰封 Berdly，章内路线锁定 | WR2 Stage6/7，S07 | CANON / 高（转录） | 控制通过 Kris 施加给他人；不画作死亡确证 |
| E11 | 2 / weird / NEO ending | 战斗 narration 从 Kris 求助转为第二人称低声呼唤 Noelle | NEO Weird Route narration，S05 | CANON / 高（转录） | UI 的叙述主语变化；不可擅自配成人类玩家声音 |
| E12 | 2 / weird / Light World Noelle | Noelle 的内心转录明确形容命令声不同于 Kris | Noelle reference70，S08 | CANON / 高（转录） | 声音区分≠完整外部 Player 认知 |
| E13 | 3 / common / TV Time | 角色进入 Tenna 的节目/游戏；比赛规则决定进程 | Chapter3 synopsis，S09 | CANON / 高（转录） | 控制者之上仍有舞台和规则 |
| E14 | 3 / sword / Original Game | 此支线可独立进行；不要求 Chapter2 Weird 成功 | Sword Method 与 WR4 prerequisites，S10/S11 | CANON / 高（转录） | 不误称 Ch3 Snowgrave continuation |
| E15 | 3 / sword / map edge | 通过 LV、障碍、钥匙才能离开通常 board 边界 | Sword first/second stages，S10 | CANON / 高（转录） | out-of-bounds 也被实现并设门槛 |
| E16 | 3 / sword / shelter approach | HERO_SWORD 向 shelter 时出现向上远离的移动阻力 | Sword third stage5；Player video17:42，S10/S12 | CANON / 中（未看录像） | 输入与 Kris 意向冲突；不猜 shelter 身份真相 |
| E17 | 3 / sword / holder dialogue | holder 对 Kris 的享受/责任提出指控；WR2 后有条件追加 | holder pre-battle，S13 | CANON（说出指控）/ 高；指控为真=THEORY | Kris 不被预先写成纯受害者，也不采信反派指控 |
| E18 | 3 / sword / screen crossing | HERO_SWORD 走出小游戏屏幕，控制暂留在它身上；Kris 后退 | Sword third stage7/8，S10 | CANON / 高（转录） | Player control 与 Kris 位置第一次视觉分岔 |
| E19 | 3 / sword / Susie interruption | 若攻击 Susie，Kris 拉开她；某分支 Susie 拔 controller，HERO 消失 | Sword main story，S10；Player video00:04，S12 | CANON / 中（未看录像） | Kris 可保护别人，Susie 可介入控制链 |
| E20 | 4 / common / house SOUL | Kris 暂藏 SOUL，玩家可沿通风口活动，身体另行动 | Chapter4/Player，S14/S12 | CANON / 高（转录） | 自主性有物理通道限制，不是抽象人格开关 |
| E21 | 4 / normal / organ | Kris 可以在 Player 存在时奏 organ；若说永不弹奏，另有咳嗽等阻断表达 | Kris piano/Player references，S06/S12 | CANON / 中（转录） | 输入存在也不意味着 Kris 全无技能/意愿 |
| E22 | 4 / common / prophecy | Ralsei 说先前版本为 summary；玻璃图文与其摘要不同 | Prophecy references4–6，S15 | CANON（角色陈述）/ 高 | 角色也面对 Story，但“不变命运”仍待结局验证 |
| E23 | 4 / weird / Noelle private talk | Noelle 回忆此前 Kris 来道歉，形容熟悉的含混声音 | WR4 Story changes，S11；Noelle ref68，S08 | CANON（Noelle 回忆）/ 高 | 有离开输入时的行为证据；事件由她叙述，非镜头目击 |
| E24 | 4 / weird / vent-choice-body | choice 位置让 SOUL 从 vent 进入房间；需要及时重入 Kris，否则中止 | WR4 Method2/3，S11 | CANON / 高（转录） | 菜单是一扇物理门；控制恢复是玩家动作 |
| E25 | 4 / weird / inner thoughts | Noelle 对回答其内心内容的声音做测试并反应 | WR4 Story changes，S11 | CANON / 高（转录） | 支持对非普通 Kris 声音的察觉；不画“我看见现实玩家” |
| E26 | 4 / weird / ring and bathroom | 指定对话后锁定本章；ring 后 Kris 丢 SOUL、踢垃圾桶，随后重入 | WR4 Method/Story，S11 | CANON / 高（转录） | 连接被敌视仍暂时恢复；原因不简化为获得完整自由 |
| E27 | 4 / weird / Susie asks | 四个空白选项，随后剧情继续 | WR4 Hometown，S11 | CANON / 高（转录） | 输入列表存在但表达不可读 |
| E28 | 4 / weird / later reactions | 指令祈祷 Noelle 时踢 candles；说永不弹琴时咬手 | Player references25/26，S12 | CANON / 高（转录） | 不执行所选句子的可见例子；自伤不作浪漫化自由象征 |
| E29 | 5 / normal / opening | Kris 回到被布覆盖的 cage，取回 SOUL 后状态变化 | Player Ch5/SOUL Ch5，S12/S04 | CANON / 高（转录） | 分离并非永远可持续；具体生存条件未知 |
| E30 | 5 / normal / Susie home | 连续拒绝送 Susie 后，Kris 把 SOUL 放进 balloon，自行送行 | SOUL Ch5，S04 | CANON / 中（转录） | Kris 自主可服务友谊，不限暴力抵抗 |
| E31 | 5 / weird / bed | 起床要重复方向输入；Kris 行动迟缓 | Player Ch5，S12 | CANON / 高（转录） | Player 的动作成本增加；动机推断单独列 T05 |
| E32 | 5 / weird / lake monologue | Noelle 主动引导 Kris 入湖，向其索要命令 | WR5 method/story，S16 | CANON / 高（转录） | 受控者开始主动要求控制；不等于安全/自由 |
| E33 | 5 / weird / lake choices | 前6组中拒绝仍推进，拒绝另计数并有回应；第7组两选项相同 | handoff Step0 script13–18/45–70，S17；Create stopActions91–111，S18 | CANON / 高（公开脚本+转录） | local choice 可留差异却不改变当前方向；避免“完全无效” |
| E34 | 5 / weird / submerged prompts | 14起进入可超时失败段；后期允许输入等待时限缩短，显示趋白 | handoff Create2/14，S18；Step2 script60–86，S19 | CANON / 高（公开脚本+转录） | 玩家被要求持续执行，但仍可停止输入退出这段 |
| E35 | 5 / weird / early chapter end | 成功后 CRT 要求 Chapter7 SideB，回 chapter select；不展示未来内容 | WR5 ending，S16；Create223–225，S18（只确认生成 end object） | CANON / 中高（显示文本转录） | 偏离被 chapter/interface 接住；不是已玩 Chapter7 |
| E36 | 5 / interrupted weird / continuation | 等待超时后回后续剧情但保留异常/关切；不能称全部重置 | WR5 Aborted，S16；Step0 con99，S17 | CANON / 中高 | 保留拒绝/不行动的可能和已有后果 |

以上不是章节逐场总结；只纳入会影响控制关系设计的事实。未列入 Pink/Flowery 战斗全流程、角色身份猜测、Egg/Shadow Crystal 全收集流程，因为当前镜头不需要它们。

## Source register

所有检索日期均为2026-10-01。oldid 是本次页面返回的 revision locator，内容制作前再次核对；source class 是资料渠道，不是命题等级。

| ID | 已读取来源与定位 | 来源类型 / 注意 |
|---|---|---|
| S01 | [Introduction rev195679](https://deltarune.wiki/w/Introduction?oldid=195679) | Wiki 游戏转录；不认定 opening voice 身份 |
| S02 | [SAVE](https://deltarune.wiki/w/SAVE) | Wiki 机制/脚本引用；slot 与 Completion FILE 分开 |
| S03 | [Susie](https://deltarune.wiki/w/Susie) § In battle | Wiki 机制，章节状态有限定 |
| S04 | [SOUL](https://deltarune.wiki/w/SOUL) § Main story | Wiki 事件，推论段不直接搬作 canon |
| S05 | [Spamton NEO rev193430](https://deltarune.wiki/w/Spamton_NEO?oldid=193430) | 含战斗 narration 转录 |
| S06 | [Kris rev195593](https://deltarune.wiki/w/Kris?oldid=195593) | 人物页含行为/脚本/对白定位 |
| S07 | [WR Chapter2 rev194219](https://deltarune.wiki/w/Weird_Route/Chapter_2?oldid=194219) | 方法、阶段、机制 |
| S08 | [Noelle](https://deltarune.wiki/w/Noelle_Holiday) ref68/70 | 明确分别定位 Chapter4 回忆声与 Chapter2 内心声音 |
| S09 | [Chapter3](https://deltarune.wiki/w/Chapter_3) | 重新读取，节目与 Sword 支线分开 |
| S10 | [Sword Route](https://deltarune.wiki/w/Sword_Route) | 三阶段/出屏幕；不把 minigame deaths 等同现实角色死亡 |
| S11 | [WR Chapter4 rev194401](https://deltarune.wiki/w/Weird_Route/Chapter_4?oldid=194401) | revision2026-09-25；包含版本变化 |
| S12 | [Player rev193513](https://deltarune.wiki/w/Player?oldid=193513) | 委托/抵抗/录像引用，不能照搬其本体论解释 |
| S13 | [Shadow Mantle holder rev195640](https://deltarune.wiki/w/Shadow_Mantle_holder?oldid=195640) | 敌方指控与它为真分开 |
| S14 | [Chapter4](https://deltarune.wiki/w/Chapter_4) | Normal 与 Weird 入口关系 |
| S15 | [Prophecy rev195158](https://deltarune.wiki/w/Prophecy?oldid=195158) | 角色说必然发生≠作品已证实全知 |
| S16 | [WR Chapter5 rev195512](https://deltarune.wiki/w/Weird_Route/Chapter_5?oldid=195512) | revision2026-09-28；计时/终屏/中止分支；最新研究入口 |
| S17 | [Ch5 handoff Step0](https://code.deltarune.wiki/ch5/gml_object_obj_ch5_lw20w_handoff_step_0) | 社区反编译；13–18,45–70,220–276；未确认 build hash |
| S18 | [Ch5 handoff Create0](https://code.deltarune.wiki/ch5/gml_object_obj_ch5_lw20w_handoff_create_0) | script2,14,67–68,91–111,223–225；未拷贝源码入仓库 |
| S19 | [Ch5 handoff Step2](https://code.deltarune.wiki/ch5/gml_object_obj_ch5_lw20w_handoff_step_2) | script45–86：颜色/失败时限；计数不是 PV 24fps 帧数 |

交叉链 locator：[Chapter3 Sword 录像引用](https://deltarune.wiki/w/Player#Chapter_3) 17:42/23:01；[Chapter4 全互动录像](https://www.youtube.com/watch?v=fr20uhuU48M) 0:00、7:49、8:08、8:38（2025-06-06）；[Chapter4 多分支录像](https://www.youtube.com/watch?v=Uc6_eW9phEI) 2025-06-11。它们不同日期可能采用不同 patch；未观看验收，不能拿首发素材覆盖当前红裂纹视觉。

## Chapter3–5 纠错与版本敏感事项

- Ch3 不是新的 Noelle Snowgrave 杀敌路线。Sword 是可独立触发的内部游戏支线；它与 Weird 呼应/条件对白和“必须完成 Ch3 才能导入 Ch4”是不同命题。
- Ch4 ring 插入视觉经过 flower→pixel→red crack 更新。当前规划用红裂纹，不把某一旧动画当隐藏 canon 真相；精确形状待 build 画面 QA。
- Ch5 的 Stop 不决定立即逆向，但有特定回应/计数；它不是“玩家没有任何差异”。后半超时可进入保留异常的续章，作品必须承认这条反证。
- Ch5 终屏涉及未发布后续章的要求，不意味着后续 SideB 内容/结局已经存在可验证剧情。PV 不能演出 Chapter6/7。
- 不从 Noelle 的兴奋证明“控制使她真正自由”；不从 Kris 入湖时未抵抗证明赞同；不把 Prophecy 视作拥有意识的反派。Story 在 PV 中是受实现规则约束的第四种力量的可视化隐喻。

## 实现前画面验收仍待项

R01：核对 Ch3 shelter resistance 与出屏幕控制切换连续录像；R02：核对 Ch4 当前补丁 ring/re-entry/blank choices；R03：核对 Ch5 床、Stop 回应、第7组、超时后续、CRT，记录平台/version/timecode。E33/E34 已有直接公开脚本依据，可用于机制 PoC；具体美术还不能称最终复刻。
