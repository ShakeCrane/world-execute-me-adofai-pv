# 《world.execute(me);》×《DELTARUNE》｜全曲导演主稿

> **本文件是导演层唯一编辑入口**：将歌曲时间、三个固定框体、Kris / Player 主线、人物留痕和镜头调度合入一处，供作者直接修改；不代表 Art 定稿、动画已完成或游戏谜题已获解答。原剧情基线 [CORE_STORY_BASELINE](deltarune/CORE_STORY_BASELINE.md) 高于本文；小细节候选见 [DETAIL_IDEA_LIBRARY](deltarune/DETAIL_IDEA_LIBRARY.md)。历史 v1.2 的重大剧情判断（SOUL、Noelle、Player 自由、开放 Execution）保留，但其“正常可重组三框”规则已被作者明确覆盖。
>
> **歌曲为第一顺序**。时间轴：211.916667s / 5086 帧 / 24fps；歌词从本机 [input/lyrics.lrc](../input/lyrics.lrc) 及 [逐词数据](../film/world_execute_word_timing_20260927/word_timeline.json) 读取。下表逐词数据处于 **AUTOMATIC_DRAFT_REQUIRES_LISTENING_REVIEW**；本稿所有细切点为导演候选，正式贴词需要配乐听审。对话、动作、角色、Chapter 和 Route 的使用都须服从歌词的语气、音乐速度和叙事事实。
>
> **空间被作者锁定**：三框保持原作形态与相对位置；正常状态永不随歌曲大幅缩放、换位、合并或消失。左框 CODE / MODEL、右上最大 WORLD、下方 LYRICS 三条独立导演轨道在同一歌曲时间并行。只有文内明确标为 **CROSSING** 的镜头可以越框；普通的图像押韵与数据呼应不算越框。原布局与逐词技术可继承 [MisakaZentai/world-execute-me-dsh-pv](https://github.com/MisakaZentai/world-execute-me-dsh-pv)；改编后的剧情、美术素材不能冒充原作已存在的实现。

## 导航

[三框语法](#panel-rules) · [全曲时间轴](#scene-map) · [逐句歌词定位](#lyric-index) · [导演镜头正文](#storyboard) · [角色留痕索引](#cast-index) · [核心名场面与边界](#critical-motifs) · [作者原始镜头](#author-originals)

<a id="panel-rules"></a>
## 1. 三框导演语法｜永久稳定的舞台

原作 1280×720 / 24fps 的固定三个内容区域：左 x24–384、y56–604；右 x404–1164、y56–604；歌词 x24–1256、y616–680（实际叠层与画边以源工程为准）。改编不是直接使用原片的 dsh 聊天剧情；是**借用其框体布局和 compositor，将左侧换成代码海与模型、右侧换成 DELTARUNE 剧情**。

| 固定框 | 负责什么 | 导演的景别与节奏 | 明确不做什么 |
|---|---|---|---|
| **右上 WORLD** | Kris 的身体、伙伴动作、具体场景、游戏叙事、视点/摄影机 | 正常生活/关系用长呼吸与同框；剧情硬证据用固定机位；命令压力可用快速切 | 不每逢歌词名词就出现物品、奇观；不让角色在框里被背景数学淹没 |
| **左 CODE / MODEL** | 参数、点阵/字符 Kris、输入载体、状态与采样、抽象代码海、路线条件与响应时差 | 点云近景、代码海纵深、短促采样、双轨追踪、未知处真正静止；右窗重要时退成低密度 | 不假装读取 Kris 思想、官方游戏源代码、Dess 位置或 Knight 身份；不常态越框 |
| **下 LYRICS** | 真正按歌声逐词显示的歌词，是歌词与音乐的唯一稳定屏幕层 | 稳定基线与字间节奏；少量 DELTARUNE 选项箭头/SOUL 小点/SAVE 星点；适时留空 | 不每句换字体、不把歌词整框拆成游戏地形、不新增器乐中不存在的唱词 |

**注意力守则**：右窗的人物需要读情绪时，左窗与下框降低噪声但保持可识别；左窗的数学/代码镜头可以精彩，但只在右窗适合留空间时主导。三框在绝大多数镜头里只**同义不同物**：右窗发生，左窗分析，下窗歌唱。

**两个可追认的原作母题**：
- 横向同构：右窗 Kris/受控对象三次由 x≈0.18W 向 0.72W，脚底 y≈0.68H，中心参照≈0.50W，约54±6f；第一次 C 跟随 Kris、第二次 M 摄影跟丢、第三次 R 真正受控的是 HERO_SWORD，Kris 留在另一位置。
- 同一输入载体：D 正常有效、E 稍微多留半拍、L 脱钩、S 迟缓、W 才允许 Kris 进行一次局部接触；MODEL 的测量永远不是人格证书。

**音乐与人物的主从**：歌词默认 \`I = Kris, you = Player\`，不能临时变成 Noelle / Spamton 的第一人称；\`them\` 约164.661s 表示这份关系影响第三者。第一次 execution 首先是“运行”，后半仍保留强制执行/处决双义；最后不写唯一 executor。Player 比 Kris **确实更自由**，可停止/退出，但参与游戏的动作仍经合法界面与 Route 条件。

<a id="scene-map"></a>
## 2. A–Y 全曲时间轴｜一眼可改的 25 条导演命题

| 时间 | 单元 | 右框的一个关键事实 / 动作 | 左框的关键抽象 | 角色与越界 |
|---|---|---|---|---|
| 00:00–00:16 | [A 创建](#scene-A) | 两线交汇；Vessel 滚动，Kris 坠入花 | 初始化/形体参数 | Kris、Vessel |
| 00:16–00:30 | [B 初遇](#scene-B) | Hometown 生活→Susie 关系 | 输入与行为的正常对位 | Toriel、Alphys、同学、Susie |
| 00:30–00:44 | [C 参数](#scene-C) | Kris 连续横移/实体与点阵 | 数学点云→字符肖像 | Ralsei 影像、1225 种子 |
| 00:44–00:55 | [D 接口](#scene-D) | 改变观看方式的冒险片段 | AC/DC、视域、时间索引 | Queen、Sweet Cap'n Cakes、Tenna 影像 |
| 00:55–00:59 | [E 余温](#scene-E) | Kris 对同伴多停半拍 | 输入停止但姿态持续 | 伙伴无抢戏 |
| 00:59–01:06 | [F 可能](#scene-F) | 多种正常可能与一个选择 | 合法分支走向 | Jevil、Lancer、King 的反讽回声 |
| 01:06–01:14 | [G 执行Ⅰ](#scene-G) | 封印喷泉→回身越左框→代码海 | 代码海被局部冲乱 | Kris，**CROSSING G** |
| 01:14–01:25 | [H 日常](#scene-H) | Kris/Susie 共享 moss | 给予/回应抽象 | Susie，主打人物 |
| 01:25–01:29 | [I 存在](#scene-I) | SAVE 名字、花店记忆 | name ≠ person | Asgore、Toriel 痕迹 |
| 01:29–01:39 | [J 标签](#scene-J) | Kris 连续存在、Spamton 提线 | 角色字段换位 | Spamton、Swatch、Rouxls、Tasque Manager |
| 01:39–01:50 | [K 完成](#scene-K) | Kris/Susie/Ralsei 共同经历 | 三框同拍而不相融 | Ralsei、Lancer、Seam、Castle Town 人群 |
| 01:50–01:58 | [L 分离](#scene-L) | Kris 取出 SOUL，SOUL 可控、身体自行动 | 两条轨迹不再重合 | Kris、SOUL，完整呈现 |
| 01:58–02:06 | [M 盲区](#scene-M) | 摄影跟丢 Kris | 缺测，不凭空知晓 | Kris |
| 02:06–02:15 | [N 条件](#scene-N) | Weird 路线压力，PROCEED | 可执行条件逐渐收窄 | Noelle、Berdly、Queen 记忆 |
| 02:15–02:28 | [O 缺席](#scene-O) | Noelle 与 Dess 过去/现在的位置差 | 不可补写的信息空位 | Dess、Noelle、Rudy；1225 回声 |
| 02:28–02:39 | [P 执行×12](#scene-P) | Noelle 的犹豫、力量、代价 | 同条命令十二次 | Noelle、Berdly / SnowGrave |
| 02:39–02:43 | [Q 计数](#scene-Q) | 下次动作更熟练却不自在 | 习惯化命令 | Noelle |
| 02:43–02:50 | [R 保护](#scene-R) | HERO_SWORD 受控，Kris 主动拉开 Susie | 受控对象不再是 Kris | Kris、Susie、HERO_SWORD |
| 02:50–02:57 | [S 迟缓](#scene-S) | Ch5 Kris 起床，身体响应延迟 | input ≠ body | Kris，Toriel 家庭物件 |
| 02:57–03:05 | [T 索求](#scene-T) | Noelle 先领路，后询问命令 | 她的愿望先于接口请求 | Noelle、Kris |
| 03:05–03:08 | [U 回答](#scene-U) | Ch4 完整选择与 Kris 咬手 | 语句 ≠ 身体反应 | Gerson、Alvin 的场景痕迹 |
| 03:08–03:14 | [V 自由](#scene-V) | Player 真的可离开，Kris 留在 WORLD | 输入停止而世界仍在 | Kris、Player |
| 03:14–03:25 | [W 反作用](#scene-W) | 指剑→局部开口→抓词捏碎 | carrier 一次偏转 | Kris，**CROSSING W** |
| 03:25–03:27 | [X 末次执行](#scene-X) | 新条件、新动作、新结果 | 精简运行状态 | executor 不揭示 |
| 03:27–03:31.917 | [Y 余白](#scene-Y) | Kris 与未闭合边界，归黑 | 留白 | 不新增谜题人物 |

<a id="lyric-index"></a>
## 3. 逐句歌词 → 精确镜头索引

> 下表由同仓库歌词文件自动核对生成。**一行歌词不等于一个切镜**，表格里的镜头 ID 可以直接跳到第4节修改导演描述。声学起点小数与歌曲段落边界可能相差几百毫秒，属歌词预入/延音，并非矛盾。器乐空白另由 B、O、W、Y 承担。**L045 有一处本地歌词 LRC 与逐词草案的措辞差异：LRC 为 “Oh, my switch role”，逐词草案为 “Oh, switch my role”；此处显示 LRC 原文，待听审确认。**

<!-- AUTO_LYRIC_ROWS_START -->
| 原歌词行 ID | 人声估计起点 | 歌词原文 | 镜头（点开直接改） |
|---|---:|---|---|
| <a id="line-L000"></a>L000 | 00:00.060 | Switch on the power line | [A01 · 接通与保护](#shot-A01) |
| <a id="line-L001"></a>L001 | 00:01.792 | Remember to put on protection | [A01 · 接通与保护](#shot-A01) |
| <a id="line-L002"></a>L002 | 00:03.863 | Lay down your pieces | [A02 · 部件选择](#shot-A02) |
| <a id="line-L003"></a>L003 | 00:05.418 | And let's begin object creation | [A02 · 部件选择](#shot-A02) |
| <a id="line-L004"></a>L004 | 00:07.380 | Fill in my data parameters | [A02 · 部件选择](#shot-A02) |
| <a id="line-L005"></a>L005 | 00:10.134 | Initialization | [A03 · 确认造成误认](#shot-A03) |
| <a id="line-L006"></a>L006 | 00:11.205 | Set up our new world | [A03 · 确认造成误认](#shot-A03) |
| <a id="line-L007"></a>L007 | 00:12.756 | And let's begin the simulation | [A04 · 模拟落地](#shot-A04) |
| <a id="line-L009"></a>L009 | 00:29.772 | If I'm a set of point | [C01 · 点集与维度](#shot-C01) |
| <a id="line-L010"></a>L010 | 00:31.293 | Then I will give you my dimension | [C01 · 点集与维度](#shot-C01) |
| <a id="line-L011"></a>L011 | 00:33.453 | If I'm a circle | [C02 · 圆与周长](#shot-C02) |
| <a id="line-L012"></a>L012 | 00:34.989 | Then I will give you my circumference | [C02 · 圆与周长](#shot-C02) |
| <a id="line-L013"></a>L013 | 00:37.102 | If I'm a sine wave | [C03 · 正弦与切线](#shot-C03) |
| <a id="line-L014"></a>L014 | 00:38.685 | Then you can sit on all my tangents | [C03 · 正弦与切线](#shot-C03) |
| <a id="line-L015"></a>L015 | 00:40.817 | If I approach infinity | [C04 · 无穷与极限](#shot-C04) |
| <a id="line-L016"></a>L016 | 00:42.256 | Then you can be my limitations | [C04 · 无穷与极限](#shot-C04) |
| <a id="line-L017"></a>L017 | 00:44.412 | Switch my current | [D01 · AC/DC](#shot-D01) |
| <a id="line-L018"></a>L018 | 00:45.763 | To AC, to DC | [D01 · AC/DC](#shot-D01) |
| <a id="line-L019"></a>L019 | 00:47.706 | And then blind my vision | [D02 · 视觉与晕眩](#shot-D02) |
| <a id="line-L020"></a>L020 | 00:49.684 | So dizzy, so dizzy | [D02 · 视觉与晕眩](#shot-D02) |
| <a id="line-L021"></a>L021 | 00:51.447 | Oh, we can travel | [D03 · 时代切换](#shot-D03) |
| <a id="line-L022"></a>L022 | 00:53.372 | To AD, to BC | [D03 · 时代切换](#shot-D03) |
| <a id="line-L023"></a>L023 | 00:55.084 | And we can unite | [E01 · 共同结果](#shot-E01) |
| <a id="line-L024"></a>L024 | 00:57.114 | So deeply, so deeply | [E02 · 未移动的余温](#shot-E02) |
| <a id="line-L025"></a>L025 | 00:59.056 | If I can, if I can | [F01 · 分岔](#shot-F01) |
| <a id="line-L026"></a>L026 | 01:00.986 | Give you all the simulations | [F01 · 分岔](#shot-F01) |
| <a id="line-L027"></a>L027 | 01:03.053 | Then I can, then I can | [F02 · 囚笼里的自由](#shot-F02) |
| <a id="line-L028"></a>L028 | 01:04.639 | Be your only satisfaction | [F03 · 获得一个结果](#shot-F03) |
| <a id="line-L029"></a>L029 | 01:06.286 | If I can make you happy | [G01 · 让结果值得相信](#shot-G01) |
| <a id="line-L030"></a>L030 | 01:08.201 | I will run the execution | [G02 · 封印](#shot-G02) |
| <a id="line-L031"></a>L031 | 01:10.123 | Though we are trapped | [G03 · CROSSING G：右→左](#shot-G03) |
| <a id="line-L032"></a>L032 | 01:11.588 | In this strange, strange simulation | [G03 · CROSSING G：右→左](#shot-G03) |
| <a id="line-L033"></a>L033 | 01:13.926 | If I'm an eggplant | [H01 · 共同发现](#shot-H01) |
| <a id="line-L034"></a>L034 | 01:15.596 | Then I will give you my nutrients | [H01 · 共同发现](#shot-H01) |
| <a id="line-L035"></a>L035 | 01:17.709 | If I'm a tomato | [H02 · Susie 有自己的快乐](#shot-H02) |
| <a id="line-L036"></a>L036 | 01:19.243 | Then I will give you antioxidants | [H02 · Susie 有自己的快乐](#shot-H02) |
| <a id="line-L037"></a>L037 | 01:21.276 | If I'm a tabby cat | [H03 · 两个人确实共享过](#shot-H03) |
| <a id="line-L038"></a>L038 | 01:22.958 | Then I will purr for your enjoyment | [H03 · 两个人确实共享过](#shot-H03) |
| <a id="line-L039"></a>L039 | 01:25.132 | If I'm the only God | [I01 · 名字的痕迹](#shot-I01) |
| <a id="line-L040"></a>L040 | 01:26.653 | Then you're the proof of my existence | [I02 · 花与家庭](#shot-I02) |
| <a id="line-L041"></a>L041 | 01:28.540 | Switch my gender | [J01 · 标签闪回](#shot-J01) |
| <a id="line-L042"></a>L042 | 01:30.277 | To F, to M | [J01 · 标签闪回](#shot-J01) |
| <a id="line-L043"></a>L043 | 01:31.888 | And then do whatever | [J02 · Spamton 的提线](#shot-J02) |
| <a id="line-L044"></a>L044 | 01:33.935 | From AM to PM | [J02 · Spamton 的提线](#shot-J02) |
| <a id="line-L045"></a>L045 | 01:35.628 | Oh, my switch role （歌词文件与逐词草案措辞有差异，待听审） | [J03 · 角色不是名字](#shot-J03) |
| <a id="line-L046"></a>L046 | 01:37.696 | To S, to M | [J03 · 角色不是名字](#shot-J03) |
| <a id="line-L047"></a>L047 | 01:39.257 | So we can enter | [K01 · 角色归位](#shot-K01) |
| <a id="line-L048"></a>L048 | 01:41.281 | The trance, the trance | [K01 · 角色归位](#shot-K01) |
| <a id="line-L049"></a>L049 | 01:43.522 | If I can, if I can | [K02 · 城镇有居民](#shot-K02) |
| <a id="line-L050"></a>L050 | 01:45.292 | Feel your vibrations | [K02 · 城镇有居民](#shot-K02) |
| <a id="line-L051"></a>L051 | 01:47.142 | Then I can, then I can | [K03 · 最后一次完全合拍](#shot-K03) |
| <a id="line-L052"></a>L052 | 01:48.984 | Finally be completion | [K03 · 最后一次完全合拍](#shot-K03) |
| <a id="line-L053"></a>L053 | 01:50.405 | Though you have left | [L01 · 场景失去热度](#shot-L01) |
| <a id="line-L054"></a>L054 | 01:52.198 | You have left | [L01 · 场景失去热度](#shot-L01) |
| <a id="line-L055"></a>L055 | 01:53.251 | You have left | [L02 · 掏心](#shot-L02) |
| <a id="line-L056"></a>L056 | 01:53.930 | You have left | [L02 · 掏心](#shot-L02) |
| <a id="line-L057"></a>L057 | 01:54.760 | You have left | [L02 · 掏心](#shot-L02) |
| <a id="line-L058"></a>L058 | 01:56.012 | You have left me in isolation | [L03 · 一个控制不了另一个](#shot-L03) |
| <a id="line-L059"></a>L059 | 01:58.236 | If I can, if I can | [M01 · 第二遍同构](#shot-M01) |
| <a id="line-L060"></a>L060 | 02:00.212 | Erase all the pointless fragments | [M02 · 视觉真正不知道](#shot-M02) |
| <a id="line-L061"></a>L061 | 02:02.008 | Then maybe, then maybe | [M02 · 视觉真正不知道](#shot-M02) |
| <a id="line-L062"></a>L062 | 02:03.828 | You won't leave me so disheartened | [M03 · 仍无答案](#shot-M03) |
| <a id="line-L063"></a>L063 | 02:05.582 | Challenging your God | [N01 · 普通的界面](#shot-N01) |
| <a id="line-L064"></a>L064 | 02:08.870 | You have made some | [N02 · PROCEED](#shot-N02) |
| <a id="line-L065"></a>L065 | 02:11.207 | Illegal arguments | [N03 · 某条路的边界变窄](#shot-N03) |
| <a id="line-L067"></a>L067 | 02:27.891 | Execution | [P01 · 第一次要完整看见](#shot-P01) |
| <a id="line-L068"></a>L068 | 02:28.716 | Execution | [P01 · 第一次要完整看见](#shot-P01) |
| <a id="line-L069"></a>L069 | 02:29.730 | Execution | [P01 · 第一次要完整看见](#shot-P01) |
| <a id="line-L070"></a>L070 | 02:30.736 | Execution | [P02 · 反馈属于 Noelle](#shot-P02) |
| <a id="line-L071"></a>L071 | 02:31.662 | Execution | [P02 · 反馈属于 Noelle](#shot-P02) |
| <a id="line-L072"></a>L072 | 02:32.597 | Execution | [P02 · 反馈属于 Noelle](#shot-P02) |
| <a id="line-L073"></a>L073 | 02:33.431 | Execution | [P03 · PROCEED 变成习惯](#shot-P03) |
| <a id="line-L074"></a>L074 | 02:34.361 | Execution | [P03 · PROCEED 变成习惯](#shot-P03) |
| <a id="line-L075"></a>L075 | 02:35.272 | Execution | [P03 · PROCEED 变成习惯](#shot-P03) |
| <a id="line-L076"></a>L076 | 02:36.211 | Execution | [P03 · PROCEED 变成习惯](#shot-P03) |
| <a id="line-L077"></a>L077 | 02:37.197 | Execution | [P04 · SnowGrave 的不可挽回](#shot-P04) |
| <a id="line-L078"></a>L078 | 02:38.120 | Execution | [P04 · SnowGrave 的不可挽回](#shot-P04) |
| <a id="line-L079"></a>L079 | 02:39.204 | Ein, dos | [Q01 · 数字同拍](#shot-Q01) |
| <a id="line-L080"></a>L080 | 02:39.791 | Trios, ne | [Q01 · 数字同拍](#shot-Q01) |
| <a id="line-L081"></a>L081 | 02:40.656 | Fem, liu | [Q01 · 数字同拍](#shot-Q01) |
| <a id="line-L082"></a>L082 | 02:41.666 | Execution | [Q02 · 再一次执行](#shot-Q02) |
| <a id="line-L083"></a>L083 | 02:42.595 | If I can, if I can | [R01 · 重新建立 Ch3 场地](#shot-R01) |
| <a id="line-L084"></a>L084 | 02:44.324 | Give them all the execution | [R02 · 第三次同构](#shot-R02) |
| <a id="line-L085"></a>L085 | 02:46.184 | Then I can, then I can | [R03 · 本能的保护](#shot-R03) |
| <a id="line-L086"></a>L086 | 02:47.945 | Be your only execution | [R03 · 本能的保护](#shot-R03) |
| <a id="line-L087"></a>L087 | 02:49.680 | If I can have you back | [S01 · 熟悉的房间](#shot-S01) |
| <a id="line-L088"></a>L088 | 02:51.860 | I will run the execution | [S02 · 让时间真的过去](#shot-S02) |
| <a id="line-L089"></a>L089 | 02:53.491 | Though we are trapped | [S02 · 让时间真的过去](#shot-S02) |
| <a id="line-L090"></a>L090 | 02:55.011 | We are trapped, ah | [S03 · 行动不代表原因揭晓](#shot-S03) |
| <a id="line-L091"></a>L091 | 02:57.442 | I've studied, I've studied | [T01 · 她先迈步](#shot-T01) |
| <a id="line-L092"></a>L092 | 02:59.202 | How to properly lo-o-ove | [T01 · 她先迈步](#shot-T01) |
| <a id="line-L093"></a>L093 | 03:01.018 | Question me, question me | [T02 · 不能独自完成的部分](#shot-T02) |
| <a id="line-L094"></a>L094 | 03:02.752 | I can answer all lo-o-ove | [T03 · 请求再次成立](#shot-T03) |
| <a id="line-L095"></a>L095 | 03:04.601 | I know the algebraic expression of lo-o-ove | [U01 · 一句完整的话](#shot-U01) |
| <a id="line-L096"></a>L096 | 03:08.294 | Though you are free | [V01 · freedom 先成立](#shot-V01) |
| <a id="line-L097"></a>L097 | 03:09.582 | I am trapped | [V02 · 留下的 Kris](#shot-V02) |
| <a id="line-L098"></a>L098 | 03:10.604 | Trapped in lo-o-ove | [V02 · 留下的 Kris](#shot-V02) |
| <a id="line-L100"></a>L100 | 03:25.372 | Execution | [X01 · 条件→行动→结果](#shot-X01) |
<!-- AUTO_LYRIC_ROWS_END -->

<a id="storyboard"></a>
## 4. 逐场景导演卡｜按右框／左框／下框分别修改

下方每张卡有**一句话画面目的、镜头及秒数、各框表现、角色留痕、事实等级**。秒数是歌曲级导演候选；需要触发原游戏事件时，需核验章节/路线及具体前提。闪现不等于“该角色与相邻片段曾在同一 canon 时刻同场”。

<a id="scene-A"></a>
### A · 00:00.000–00:16.042｜Creation｜「一个人仿佛被造出来」

**一句话**：黑暗两束光交会，Vessel 选择越转越快，中央留下一具仿佛成功生成的 Kris；Kris 落进只有一小块花的世界，观众自然把 Vessel 与他误认成同一角色。

- <a id="shot-A01"></a>**A01 00:00.000–00:03.583｜接通与保护**：RIGHT 原始黑色场面内两道细光从左右汇合，交点才形成可承载物体的保护框；LEFT 原点、两次脉冲与保护边界以极稀疏终端图形回应；BOTTOM 开始逐词唱通电/保护。不用恐怖闪屏和“ERROR”。
- <a id="shot-A02"></a>**A02 00:03.583–00:09.750｜部件选择**：RIGHT 真正可辨的 Vessel 头、躯干、腿在三条错向横向轨道中排列，先看得清候选，再在参数语义下加速形成套印残影；LEFT 以合法部件槽与参数状态同步，不出现“Kris 生成失败”。BOTTOM 逐词推进创建/填写参数。
- <a id="shot-A03"></a>**A03 00:09.750–00:12.471｜确认造成误认**：初始化词时短促凝定，残影中心用轮廓匹配一剪变为 Kris，而**没有展示 Vessel 实体变成 Kris**；LEFT 只锁住可读数据，保留 creator 与 vessel 两个名字字段各自独立。
- <a id="shot-A04"></a>**A04 00:12.471–00:16.042｜模拟落地**：RIGHT 场景获得深度，Kris 由暗处坠落、脚触及小花丛，花朵受力回弹，之后站稳；LEFT 不是“制造 Kris”的编码画面，只记录可观察运动；BOTTOM 随唱句结束回归正常字幕。
- **人物 / 连续性**：Ch1 Vessel 与 Kris 的连接是 **ORIGINAL 蒙太奇谎言**；花与坠落也是作者意象，不写 canon 创生事实。未出现 Player 的真实面孔。

<a id="scene-B"></a>
### B · 00:16.042–00:29.792｜Connection｜「这是一个值得进入的生活世界」

**一句话**：用三四个有呼吸的日常切片让观众认识 Kris 的家庭、学校和 Susie，最后把“操作带来同行”的游戏契约拍得自然可信。

- <a id="shot-B01"></a>**B01 00:16.042–00:19.500｜家门**：RIGHT Kris 离开家，Toriel 送行的关切只由一个实际动作/视线体现，别让“羊妈登场”成为独立海报；LEFT 从 Vessel 参数页转为普通 input / movement；BOTTOM 是器乐空白。
- <a id="shot-B02"></a>**B02 00:19.500–00:22.500｜教室**：RIGHT 明确的时间/地点剪接，Alphys 招呼学生，Catti、Jockington、Temmie、Snowy、Berdly、Noelle 可各作为教室座位、剪影或背景动作，不要求人人独占一秒；LEFT 只记录地点/普通互动状态。**任何人物同时在场须与选择的游戏场景相容**。
- <a id="shot-B03"></a>**B03 00:22.500–00:26.100｜初次冲突**：RIGHT Susie 的一个不受 Kris 输入直接决定的行为/拒绝，角色性格通过空间站位而非字幕介绍成立；LEFT 对 Kris 的 input 有记录，但无从推导 Susie 的意愿。
- <a id="shot-B04"></a>**B04 00:26.100–00:29.792｜后来同行**：经过**清楚可辨的 Ch1 同章时空省略**，Susie 后来主动与 Kris 同向移动；低速跟拍，让观众觉得合作是真实的。此段不能演成连按几次选项让她立刻服从。
- **音乐/角色**：器乐不编词；全员留痕以生活空间自然而非 NPC 走马灯完成。B 的“亲近”会在 H/K 和 R 成为情绪证据。

<a id="scene-C"></a>
### C · 00:29.792–00:44.417｜Model｜「描述一个人的快乐，并不等于拥有那个人」

**一句话**：右框继续看到一个活着的 Kris，左框则把同一段行动精确采成点阵、字符肖像和数学关系，让歌曲的八句数学许诺成为一次连贯的双窗演出。

- <a id="shot-C01"></a>**C01 00:29.792–00:33.453｜点集与维度**：RIGHT Kris 沿同一真实地面完成**第一次横移 DNA**（x≈.18→.72W，54±6f），镜头自然跟随；LEFT 从一两个采样点逐渐形成能辨认 Kris 站姿/发型特征的点云，立体坐标只在代码框里面成长；BOTTOM 逐词显示点、维度，不搬出歌词栏。
- <a id="shot-C02"></a>**C02 00:33.453–00:37.102｜圆与周长**：RIGHT 拍一次简单绕行，角色仍占据主要情绪阅读；LEFT 从已采得的脚步轨迹得到圆形和可见行走长度，几何线不是随机浮在右侧的 HUD。
- <a id="shot-C03"></a>**C03 00:37.102–00:40.817｜正弦与切线**：RIGHT 在一段具有天然起伏的冒险路径前进，允许一帧/一局部出现原身体像素→字符转译，但不可把角色整体常态抹掉；LEFT 将相同步态的垂直分量画成一条波形、某个时刻得到切线，两框彼此呼应**不穿框**。
- <a id="shot-C04"></a>**C04 00:40.817–00:44.417｜无穷与极限**：RIGHT Kris 穿出采样视野仍可见地行动；LEFT 的可测数据到边界就停止，说明 MODEL 能捕获的是观察的一部分。一个极弱的 1225 可以作为普通数字匆匆划过（COMMUNITY READING，不解释来源或结果）。
- **人物留痕**：可在 RIGHT 的道路转场借 Ralsei 一次明确的引导/同行姿势，让他不是单纯 K 段客串；但 C 不偷换歌词 I 主体，也不把 Ralsei 数学化成新解谜对象。

<a id="scene-D"></a>
### D · 00:44.417–00:55.083｜Interface｜「我们一直通过某种接口互相触及」

**一句话**：歌曲关于电流、视觉和时间的词依次改变左窗的操作方式，同时右窗只用几次清楚场景变换展示“接口不同，看到的世界也不同”。

- <a id="shot-D01"></a>**D01 00:44.417–00:47.706｜AC/DC**：RIGHT 保留一个仍可理解的动作/结果，不切成电学科普；LEFT 同一个 input carrier 在交流/定向脉冲之间切换节律，以后 S/W 将沿用它的形状；BOTTOM token 小幅改变节拍重心。
- <a id="shot-D02"></a>**D02 00:47.706–00:51.447｜视觉与晕眩**：RIGHT 镜头前景遮挡视野/局部镜头变焦，仅观看者短暂不知方向，Kris 并未被声明失明；LEFT 对应观测窗口变窄。**不抖动整张三框，也不制造彩虹模糊滤镜。**
- <a id="shot-D03"></a>**D03 00:51.447–00:55.083｜时代切换**：RIGHT 不伪装 Kris 真的时间穿越，以城镇/舞台/电视的**明确 THEMATIC 剪接**闪过 Queen、Sweet Cap'n Cakes、Tenna 的媒体化表演或痕迹；LEFT 切换索引状态；BOTTOM 保留 AD/BC 等原词。各章客串必须有可溯源原作素材，不连成同一舞台 canon。
- **边界**：D 的媒介切换全部发生**各自框内**，不是第一次越框。

<a id="scene-E"></a>
### E · 00:55.083–00:59.042｜Aftertaste｜「输入已经结束，那份注意还在」

**一句话**：在极普通的共同动作结束后，Player 停止输入，但 Kris 的原有朝向和视线比摄影机预期多留半拍。

- <a id="shot-E01"></a>**E01 00:55.083–00:57.300｜共同结果**：RIGHT 合作已经发生，角色做完一件很小的事，伙伴先有自己的回应；LEFT 的 input pulse 回落，BOTTOM 在“结合/深入”的歌词上正常延音。
- <a id="shot-E02"></a>**E02 00:57.300–00:59.042｜未移动的余温**：镜头准备离开，但 Kris 不再另外转头、不向新目标移动，只**维持刚才已经存在的注意方向**，新的输入到来后自然继续；LEFT 数据记录稍迟于 pulse 定格。回看有意味，初看没有恐怖感。
- **角色**：此处不额外插叙；让亲密相处本身成为镜头。

<a id="scene-F"></a>
### F · 00:59.042–01:06.292｜Possibilities｜「如果我能给你所有选择」

**一句话**：音乐第一次热烈地抬起，Kris 体验正常游戏里“可以试一试”的快乐；自由主题第一次由 Jevil 的牢笼形成短促反讽。

- <a id="shot-F01"></a>**F01 00:59.042–01:02.583｜分岔**：RIGHT 一个普通决定点前 Kris 短暂停留，同章若干可能结果以明确**选择回忆/分镜假设**而非实际同时存在的分身依次闪现；LEFT 合法分支简短展开；BOTTOM 两次条件句用相似的字形节奏呼应。
- <a id="shot-F02"></a>**F02 01:02.583–01:04.650｜囚笼里的自由**：RIGHT 一两个极短 THEMATIC INSERT：Jevil 在牢笼/战场中旋转，Lancer 的玩闹与 King 的压迫只作为可核验不同状态短闪；他们不与此刻的 Kris 实际同时战斗。LEFT 的分支显示有些路径走得通、有些不行，不宣称“Jevil 揭晓了宇宙真相”。
- <a id="shot-F03"></a>**F03 01:04.650–01:06.292｜获得一个结果**：RIGHT 回到 Kris 的有效操作和一个自然的人物回应；LEFT 一条轨迹确认成功，其余安静退去。第一次满足是有道理的，不预先把 Player 表现为恶人。
- **字符客串**：Jevil 必须可凭动势认出，而不是抽象乱转的眼球；Lancer/King 优先用独立瞬间、非虚构共时画面。

<a id="scene-G"></a>
### G · 01:06.292–01:13.917｜Execution Ⅰ｜「运行成功之后，谁能碰那条边？」

**一句话**：第一次 Execution 随 Kris 封印喷泉产生可靠的游戏结果，随后在一次明确的原创越框演出里，Kris 回身砍开左右窗缝、跃入左侧代码海。

- <a id="shot-G01"></a>**G01 01:06.292–01:08.400｜让结果值得相信**：RIGHT 喷泉在右侧，Kris 有脚下真实空间与此前行动结果；摄影机从可感纵深向横向侧剖面变换，越像二维越能看见左右框缝；LEFT 原本自洽的代码海保持稳定；BOTTOM 按第一次 execution 正常出字，先理解“运行/完成”。
- <a id="shot-G02"></a>**G02 01:08.400–01:10.050｜封印**：RIGHT Kris 的动作使喷泉光束收束；LEFT 对应一次已发生的事件记录，不提前涌出乱码。这里封印是游戏母题的 ORIGINAL 压缩演出，实际章节/前提须在素材选择时核实。
- <a id="shot-G03"></a>**G03 01:10.050–01:12.550｜CROSSING G：右→左**：RIGHT Kris 回头望向 **右窗左边界**，短准备后斩向那里；刀弧切开两框原有分隔，Kris 或其连续可识的人物表示真正跨入左框。LEFT 的字符海按遮挡层级前后让路，再被其行动拨乱；**底栏仍独立**。不能只是右框里放一张代码海壁纸冒充跨框。
- <a id="shot-G04"></a>**G04 01:12.550–01:13.917｜短暂失去秩序**：LEFT 残留一次真实有方向的代码波动，RIGHT 保持边界位置可辨；下一 H 用明确跨场切镜恢复正常三框。歌词 trapped 使观众对刚才“越出一框”的有限性产生疑问，但不宣布 Kris canon 修改程序或已经绝对自由。
- **重要开放冲突**：这是作者指定的大型越框镜头，超出旧 v1.2 只在 W 局部接触的权限封板；本版明确将它标作 **ORIGINAL 主导演候选**。若放进成片，需作者在 rough 中确认不会吞掉 W 的终极力度。

<a id="scene-H"></a>
### H · 01:13.917–01:25.125｜The Small Gift｜「给予的许诺落在一个可笑而真实的小事上」

**一句话**：茄子、番茄、猫的歌词不拍成三个变身卡，而是 Kris 与 Susie 在 Ch2 Normal 共享 moss，轻松、带一点荒诞、但确实有人际温度。

- <a id="shot-H01"></a>**H01 01:13.917–01:17.300｜共同发现**：RIGHT 用明显 Ch2 Normal 场景切断 G 的原创冒险空间，Kris 接近 moss；LEFT 从代码海波动恢复为低密度的生命/响应形态；BOTTOM 保留食物比喻的轻快，最多出现一次小小游戏选项箭头。
- <a id="shot-H02"></a>**H02 01:17.300–01:21.150｜Susie 有自己的快乐**：RIGHT Susie 对 moss 作出属于她自己的实际反应，摄像机暂时给她时间，不把她拍成“按钮已触发”的 NPC；LEFT 不输出 Susie 的服从数值。短短一处小幽默足够抵住三句荒诞歌词。
- <a id="shot-H03"></a>**H03 01:21.150–01:25.125｜两个人确实共享过**：RIGHT 两人对同一件小东西留下共同经历，随后 Susie 自己先走半步；LEFT 仅有微量记录，BOTTOM 正常过渡“存在”词群。此处不因为下句谈 God 就让 Kris 立刻成神。
- **事实**：moss 需保持其正确 Normal Route 触发条件，不把 Weird 的 Noelle 片段混作同一冒险连续时间。

<a id="scene-I"></a>
### I · 01:25.125–01:28.542｜Proof｜「记录证明发生过，却不证明它是谁」

**一句话**：一个普通的 SAVE/name 记录与 Kris 的背影错开，Asgore 的花店作为对开场花的家庭记忆闪过。

- <a id="shot-I01"></a>**I01 01:25.125–01:27.000｜名字的痕迹**：RIGHT 右窗中的一角出现合法 SAVE 或名字记录，而 Kris 已经继续移动；LEFT 记录可看见的名字/位置，却对主体身份不作解释；BOTTOM 让“存在证明”相关词完整停够一瞬。
- <a id="shot-I02"></a>**I02 01:27.000–01:28.542｜花与家庭**：RIGHT 镜头以花瓣/形状匹配切进 Asgore 花店一个照料花朵的真实细节，Toriel 的家庭物件作为不同地点的极短回声；**不把两人拍成已经和好**。LEFT 保持同一淡淡的名字记录。
- **角色**：Asgore 有生活行动，不只是对着镜头亮相；歌曲的“God”不能被拿来盖章他就是幕后角色。

<a id="scene-J"></a>
### J · 01:28.542–01:39.250｜Role ≠ Person｜「标签可以换，一个人的经历不会按标签重排」

**一句话**：歌曲快速切换 F/M、AM/PM、S/M 的过程由左框角色字段承担，右框的 Kris 仍连续行动，Spamton 的提线与其他人物的职业面貌构成反证。

- <a id="shot-J01"></a>**J01 01:28.542–01:32.000｜标签闪回**：RIGHT Kris 沿熟悉的路线走，几帧间接进不同人物的相似姿态/角色位置（不要宣布 Kris canon 性别可改）；LEFT 字段在同一个槽里快速替换；BOTTOM 逐词显示原文，少量焦点反色，禁做单词图鉴。
- <a id="shot-J02"></a>**J02 01:32.000–01:35.500｜Spamton 的提线**：RIGHT Spamton NEO 在明确可辨认的提线关系里短闪，线的方向与左框的控制轨迹产生视觉押韵，但**线不真的延长跨越窗框**；补一处 Swatch/Tasque Manager 的招牌/服装或有依据的动作作为 NPC 留痕。
- <a id="shot-J03"></a>**J03 01:35.500–01:39.250｜角色不是名字**：RIGHT Rouxls Kaard 的夸张姿态在片刻中闪现又离开，Kris 的动作节奏未断；LEFT 极轻掠过未归属 KNIGHT 职能及 1225 作为可删的社区读法，不填身份候选，不与 Dess 空位配对。
- **要求**：本段是角色主题回声，不展示 Spamton 真与 Kris 在同一个物理时间中被两框共同控制；THEMATIC 的剪切应可辨认。

<a id="scene-K"></a>
### K · 01:39.250–01:50.417｜Completion｜「当三人真的在一起，谁还在乎自己在被操作？」

**一句话**：Kris、Susie 与 Ralsei 一次顺畅而具体的合作令观众真心相信这份关系，三框在音乐上达到最和谐的同步，直到 L 的第一次彻底分离。

- <a id="shot-K01"></a>**K01 01:39.250–01:43.000｜角色归位**：RIGHT 一段明确的 Castle Town / Dark World 合法场景，同框 Kris、Susie 与 Ralsei；Ralsei 引导一处问题，Susie 以自己的方式回应，Kris 有可辨动作；LEFT 刚才跳动的角色字段安静回到一套普通稳定记录；BOTTOM 进入 trance 词群时回收节奏，不出现巨大的 LOVE。
- <a id="shot-K02"></a>**K02 01:43.000–01:47.300｜城镇有居民**：RIGHT 跟随三人的共同动作，Seam 的店、Lancer 的小动作、Rouxls/Top Chef/Starwalker/Nubert 等可根据所选合法 Castle Town 场景以路过、招牌或回忆卡一闪留痕；不强制所有角色出现在同一帧。LEFT 的代码流按行动节奏逐步对齐。
- <a id="shot-K03"></a>**K03 01:47.300–01:50.417｜最后一次完全合拍**：RIGHT 留一次共同发现→Ralsei/ Susie 各自反应→Kris 跟上，镜头不急切离开；LEFT 采样与 WORLD 运动近乎同步；BOTTOM 的 completion 正常落完。**三框不是物理融合，只是观众觉得三者恰好同一心跳**。
- **角色纪律**：Ralsei 不是背景彩蛋：必须有至少一个能称为他自己的互动动作。若群像过密，先删除 Nubert/Starwalker 一类补充闪现，保留三人事件。

<a id="scene-L"></a>
### L · 01:50.417–01:58.250｜SOUL Separation｜「你离开了，我还在这里」

**一句话**：连续六次离开歌词中，不靠故障惊吓而用一次安静完整的身体行为展示 Kris 主动取出 SOUL、Player 仍操纵 SOUL、Kris 身体仍能自行行动。

- <a id="shot-L01"></a>**L01 01:50.417–01:52.850｜场景失去热度**：RIGHT 从 K 的温暖共同场景**清楚切到 Ch1 房间与相应原作条件**；Kris 处于一段正常的真实时间，镜头稳定。LEFT 先保留普通 input 轨迹，不先显示断联警报；BOTTOM 前几次重复相同位置出字、亮度慢慢改变。
- <a id="shot-L02"></a>**L02 01:52.850–01:55.300｜掏心**：RIGHT Kris 本人**主动**取出 SOUL；手、胸口、SOUL、身体彼此空间位置必须同时读清；镜头不靠冲击近景代替事实。LEFT 轨迹初次分叉；BOTTOM 继续按原声连唱，不加“No freedom”解释牌。
- <a id="shot-L03"></a>**L03 01:55.300–01:58.250｜一个控制不了另一个**：RIGHT SOUL 仍对 Player 有响应，Kris 的身体却执行属于身体的独立行动；观众至少在一个清晰构图里辨认出两者未同步。LEFT 显示身体/ SOUL 两条可观察轨迹，但不能直接说出 Kris 的内心动机。尾帧留给空静，不用惊吓音效。
- **必须保留的 CANON 三事实**：自主掏心、SOUL 仍可被操作、身体行动可继续。不是 Kris 在此刻才长出独立意志；Player 不等于那颗心的全部本体。

<a id="scene-M"></a>
### M · 01:58.250–02:05.583｜Observation Loss｜「擦掉碎片，也不能凭空找回看不到的事」

**一句话**：第二次相同的横移由 Kris 的身体完成，但摄影机惯性跟随可见 SOUL，真的错过了 Kris 的部分行为，左框也诚实地缺少对应数据。

- <a id="shot-M01"></a>**M01 01:58.250–02:00.600｜第二遍同构**：RIGHT 使用 C 的进点、地面、中心参照和 54±6f 横移，在后半摄像机开始按 SOUL 运动方向走，Kris 身体脱离构图；LEFT 已有身体轨迹中断采样。不可改变动作距离来凑“相似”。
- <a id="shot-M02"></a>**M02 02:00.600–02:03.350｜视觉真正不知道**：RIGHT 镜头经过前景遮挡/门，观众不能看到 Kris 被遮住的具体私下行动；LEFT 不能用漂亮线图“补录像”。BOTTOM 在 erase/fragments 一组词上做逐词淡失。
- <a id="shot-M03"></a>**M03 02:03.350–02:05.583｜仍无答案**：RIGHT 最后只剩一片正常却不完整的空间，摄影机仍找不到该找的人；LEFT 给一段未测字段而非 Error；BOTTOM 将悲伤留给歌曲声音。
- **限制**：摄影机不是故意剪去已经看见的“真相”；真正的不知情不能用叠屏/倒带作弊。

<a id="scene-N"></a>
### N · 02:05.583–02:14.667｜Illegal Arguments｜「可以选择，但并非所有命令都没有代价」

**一句话**：一项看似普通的 Weird Route 操作在重复要求中变得越来越像施压，PROCEED 是实在的交互选择而非悬浮在半空的巨字特效。

- <a id="shot-N01"></a>**N01 02:05.583–02:08.420｜普通的界面**：RIGHT 可辨认的 Ch2 Weird 相关情境中 Player 面对一个真实指令/选择，Noelle 是有反应的人，不是终端；LEFT 显示合法条件与一次命令入口，BOTTOM 对应“challenge”语义正常唱。
- <a id="shot-N02"></a>**N02 02:08.420–02:11.100｜PROCEED**：RIGHT 按原作条件呈现关键选择及 Noelle 的实际回应/停顿；LEFT 同一合法命令线反复通过，别变成无理由“无法解析”红报错；BOTTOM 歌词 unchanged，只在反色/字距上产生压迫。
- <a id="shot-N03"></a>**N03 02:11.100–02:14.667｜某条路的边界变窄**：RIGHT 以画内可以读到的实际 Route 变化承接结果，人物仍存在；LEFT 某些分支被条件关掉，框只在本框中收窄，固定三框外框不动。若无可核验原作前提，以 THEMATIC 两镜处理，而非编一段连续剧情。
- **注意**：PROCEED 不是 Player 与 Kris 的某种 canon 私人对话；不要把 Ch5 Stop/Proceed 机制未经证实地拼成 Ch2 的即时结果。

<a id="scene-O"></a>
### O · 02:14.667–02:27.875｜Absence｜「留下的不是谜题，是曾经在这里的人」

**一句话**：器乐交给 Noelle 与 Dess 的关系，一段童年相伴与一段现实空位采用同构摄影，仅在左框远处有一个无人解释的 1225。

- <a id="shot-O01"></a>**O01 02:14.667–02:18.000｜曾经的关系**：RIGHT 从可核验的家庭/童年回忆材料切入，让 Noelle 与 Dess 曾经共享过空间的事实先站住；若需要新绘同框画面，明确为 ORIGINAL 的记忆图像，不假装原游戏逐帧存在。LEFT 相应两个位置很短地同时可辨；BOTTOM 器乐空白。
- <a id="shot-O02"></a>**O02 02:18.000–02:22.300｜相同位置，缺一个人**：RIGHT 用同样摄影机运动返回现在 Noelle 所站的位置，另一端没有回应；可借 Rudy 的医院/家庭牵挂背景增加人间现实感，但不能伪造 Dess 的确切去向。LEFT 留一段没有可填数据的距离，**不是一个待计算的失踪坐标**。
- <a id="shot-O03"></a>**O03 02:22.300–02:27.875｜没有答案的回声**：RIGHT Noelle 从空处转回现实方向，观众先感到思念；LEFT 1225 或类似未完数据只闪一次，未解释，也不组成密码解析过程。**器乐中不要加歌没唱的“Where are you?”**。进入 P 前 Noelle 仍然是有过去、目标和感情的人。
- **认识论**：Dess 的存在/亲属关系与失踪材料有依据；“1225 指向 Dess 位置 / Knight”不是 canon。社区梗可删，不因反复出现自动成为答案。

<a id="scene-P"></a>
### P · 02:27.875–02:39.208｜Execution ×12｜「她真的获得了力量，也真的失去了某种东西」

**一句话**：十二次 Execution 不是十二个击杀画面，而是 Noelle 一次完成的犹豫—命令—施法—感受结果逐渐被越来越短的执行间隔吞没；SnowGrave 的重量在后半才抵达。

- <a id="shot-P01"></a>**P01 02:27.875–02:30.300｜第一次要完整看见**：RIGHT 清楚地给 Noelle 的位置、面前情况、接到的 Weird 命令、短暂停顿、自己的动作和结果；LEFT 的 token 一次经过输入口，结果在 WORD/命令之后才被记下；BOTTOM 逐个 Execution 按歌声显示，不把十二行叠为排行榜。
- <a id="shot-P02"></a>**P02 02:30.300–02:33.800｜反馈属于 Noelle**：RIGHT 施法确实改变可行动空间，Noelle 对自己做成的事有一瞬真实感知，允许力量带来的诱惑和对力量的复杂情绪，不能只是一串痛苦哭脸；LEFT 两次执行的间隔微微压缩，但她的反应让数据短暂停止刷新。
- <a id="shot-P03"></a>**P03 02:33.800–02:37.100｜PROCEED 变成习惯**：RIGHT 用可追踪的同机位/相似行为压缩不同经历，反复命令更容易抵达、行动停顿更短，但同一画面内人物仍有差异；LEFT 重复通道可辨，BOTTOM 同一 Execution 出字位置可重复，**不代表十二个受害者各被处决**。
- <a id="shot-P04"></a>**P04 02:37.100–02:39.208｜SnowGrave 的不可挽回**：RIGHT Berdly 与 SnowGrave 的关键游戏事件在符合 Ch2 Weird 条件的 THEMATIC 证据镜头中出现，首先看见 Noelle 作为实际施法者和结果，而非一块“死亡证书”或无证实的最终生死判定；LEFT 短促凝固为一个结果状态，不公布未知命运；BOTTOM 最后一次 Execution 收住。
- **角色/Route**：Noelle 并非被动傀儡，也非已经彻底自由的胜利者；她有恐惧、力量体验与被要求继续的混合。Ch2 的条件须核验，跨时段反复允许压缩，不冒充十几秒真实游戏连续操作。

<a id="scene-Q"></a>
### Q · 02:39.208–02:42.583｜Count｜「重复突然听起来如此熟练」

**一句话**：多语言计数把上一段原本需要思考和停顿的选择压缩成节奏，在 Noelle 的下一步中留下对命令的期待。

- <a id="shot-Q01"></a>**Q01 02:39.208–02:41.300｜数字同拍**：RIGHT Noelle 仍身处她可辨的行动空间，动作开始与音乐计数接近；LEFT 多种文字系统的数字依次只占同一个小记录位，而不是变成一副新世界地图；BOTTOM 完整保留原唱词的语言/字母。
- <a id="shot-Q02"></a>**Q02 02:41.300–02:42.583｜再一次执行**：RIGHT 留一瞬她在真正行动前的停顿；LEFT 命令的下一个入口已经准备就绪；这段不是“所有语言都有魔法力量”的新设定。
- **转场**：Q→R 必须硬切到不同 Chapter / 事件，不能让 Ch2 冰路一脚踩进 Ch3 HERO_SWORD。

<a id="scene-R"></a>
### R · 02:42.583–02:49.667｜Them / Protection｜「被控制的不是 Kris，保护同伴的却是他」

**一句话**：第三次相同的左→右横移由 HERO_SWORD 完成，Kris 在并未受到该输入直接驱使时主动保护 Susie，成为全片最短也最硬的主体性证据。

- <a id="shot-R01"></a>**R01 02:42.583–02:43.350｜重新建立 Ch3 场地**：RIGHT 看清 HERO_SWORD、Kris、Susie、潜在攻击方向已经在场；LEFT 当前受控目标字段改变，不把 Hero Sword 拍成 Kris 正在挥舞的武器；BOTTOM 当前 I/you 的歌声关系继续，只在 them 一词附近提示被波及的第三者。
- <a id="shot-R02"></a>**R02 02:43.350–02:45.650｜第三次同构**：RIGHT 与 C/M 尽可能同源的进入点、地面、空间中心与 54±6f 横移，但**真的跟输入移动的是 HERO_SWORD**，Kris 维持位置；LEFT 轨迹与 Kris body 脱钩，语法比解释字卡更明确。
- <a id="shot-R03"></a>**R03 02:45.650–02:49.667｜本能的保护**：RIGHT 一道真实可见威胁指向 Susie，Kris 主动把她拉开，给动作必要的准备、接触和人物结果，不做“自主性解锁”大爆字；LEFT **只能观察**这次不同于受控目标的行动，不能把它标成任意可知的 Kris 内心意愿。K/H 的关系回声在一个动作里兑现。
- **CANON / 位置**：Ch3 可选 HERO_SWORD 段落须检查“当前控制回到 Sword”及 Susie 受威胁的先后条件，不重写成所有玩家必见的事件。

<a id="scene-S"></a>
### S · 02:49.667–02:57.458｜Input / Body｜「一样的输入，身体不再按同一节奏跟上」

**一句话**：Ch5 另一场景里 Kris 起床的迟缓不靠大字 RESIST 来解释，而让右框身体动作和左框正常 input pulse 的距离越来越难以忽视。

- <a id="shot-S01"></a>**S01 02:49.667–02:52.050｜熟悉的房间**：RIGHT 正常 Hometown 房间、Kris 在床上的重力与停顿，Toriel 家庭物件/房间布置极轻回收 B 的生活感；LEFT 一次普通输入来到，右侧尚无对应动作。
- <a id="shot-S02"></a>**S02 02:52.050–02:55.100｜让时间真的过去**：RIGHT 身体稍迟仍不按第一次期待反应，再到迟缓起身；LEFT 输入轨迹按原有形状重复，身体轨迹落后；BOTTOM 原声持续前行，自身制造错拍，不要强行抖字幕。
- <a id="shot-S03"></a>**S03 02:55.100–02:57.458｜行动不代表原因揭晓**：RIGHT 终于行动，但镜头不做仇视 Player 的凝视定格；LEFT 只能写可见延时，不写 fatigue/resentment 的唯一原因；下个 T 需清楚切换场景。
- **CANON 边界**：身体迟缓的实际成因尚未确认，不能接成“R 受伤所以 S 爬不起来”。

<a id="scene-T"></a>
### T · 02:57.458–03:04.583｜Request｜「她先有自己的目标，然后主动来询问命令」

**一句话**：Noelle 在 Ch5 湖边先牵引 Kris 朝自己想抵达的方向走，直到遇到困难才向熟悉的指令关系求助——求助不抹杀此前的主动性。

- <a id="shot-T01"></a>**T01 02:57.458–03:00.150｜她先迈步**：RIGHT Noelle 清楚带领 Kris 朝湖/要到达的位置移动，镜头允许她短暂停在自己看见的目的地上；LEFT 不预先生成命令，先记录她自主开始的路线；BOTTOM 歌词是 Kris 对 Player 的关系隐喻，不能把 I 改归 Noelle。
- <a id="shot-T02"></a>**T02 03:00.150–03:02.550｜不能独自完成的部分**：RIGHT 她面对障碍，动作和目光表达真实期待；LEFT 命令接口仍空缺，镜头不写“被人操纵了才有意志”；BOTTOM 在 question/answer 主题下轻微改变提问/回答两词的字距。
- <a id="shot-T03"></a>**T03 03:02.550–03:04.583｜请求再次成立**：RIGHT Noelle 转而向 Kris 期待指令，镜头停在两人的空间关系中；LEFT 请求入口此刻才出现，不虚构她已直接知道现实 Player 的身份。转 U 必须是另一个 Chapter 的明确镜头断点。
- **对比**：T 的意图不是证明 Noelle 已彻底脱离控制，而是表现她的需求与依赖同时真实存在。

<a id="scene-U"></a>
### U · 03:04.583–03:08.292｜Expression｜「说出口的句子无法穷尽身体的反应」

**一句话**：完整的原作对话选项确实由 Player 提交，但 Kris 随后以不能被单纯逐字读作选项的身体动作回应；语言能被选择，不等于能读透一个人。

- <a id="shot-U01"></a>**U01 03:04.583–03:06.300｜一句完整的话**：RIGHT 明确切换到 Ch4 Weird 的教堂/钢琴相关场景和前提，展示原作可核验的完整选择 “I'll never play again”，不截去任意半句；LEFT 仅记下“用户已提交一项完整句子”，BOTTOM 歌词继续唱代数式的爱，不把原歌改写成 Kris 的游戏对话。
- <a id="shot-U02"></a>**U02 03:06.300–03:08.292｜身体另有回应**：RIGHT 让观众看清 Kris 咬手的先后与身体重量；LEFT 没有权力把这个反应翻译成单一的心思；BOTTOM 不加巨大 LOVE 方程。Gerson/Alvin 的教堂、钢琴或纪念物可作为背景痕迹而非他们 canon 当场出现。
- **权限**：完整 choice 仍然提交了；不能因视觉配合而拍成 Kris 实际删除或重写了这个选项。跨 U→V 不伪造 Ch4 与 Ch5 同一连续事件。

<a id="scene-V"></a>
### V · 03:08.292–03:13.917｜Relative Freedom｜「你真的有离开的自由，我没有」

**一句话**：镜头第一次完整允许 Player 的视线停留在 WORLD 之外，而 Kris 留在自己无法直接离开的游戏世界内；不要马上反转成“Player 其实也被绝对监禁”。

- <a id="shot-V01"></a>**V01 03:08.292–03:09.600｜freedom 先成立**：RIGHT **在原有右上固定框内**从 Kris 稍退到完整 WORLD 取景，给 Player 能停手和不继续观看的想象空间，原三大框的物理轮廓仍稳固；LEFT input 可停、没有惩罚；BOTTOM free 一词约 189.364s 用正常留白让意义落地。
- <a id="shot-V02"></a>**V02 03:09.600–03:11.350｜留下的 Kris**：RIGHT 角色没有因输入停止而消失，身体、房间与已经发生的关系都还在；LEFT 不加隐藏监狱、无限循环、假管理员；BOTTOM trapped 自身的书写与 free 的自然间隔形成痛感。
- <a id="shot-V03"></a>**V03 03:11.350–03:13.917｜不继续真的可能**：RIGHT 至少给一个没有新操作的真实呼吸，再用一次**清晰可感的 Player 选择继续**把视线引入 W，不能暗示所有人无法停止玩游戏；LEFT 从静止准备恢复熟悉 carrier。
- **相对性**：Player 在游戏内受已实现 Route/接口限制，不等于 Player 像 Kris 一样无法离开；本段不偷换自由的真实存在。

<a id="scene-W"></a>
### W · 03:13.917–03:25.375｜Counteraction｜「他第一次伸手触及一直在定义他的东西」

**一句话**：Player 在能够离开之后选择继续，一条熟悉的输入载体再次影响 WORLD；Kris 看见、剑指观看者、只切开局部边界并向下攥碎一个真正留下的歌词词语，而三框在动作结束后恢复可辨的固定形式。

- <a id="shot-W01"></a>**W01 03:13.917–03:17.800｜继续与结果**：RIGHT 一次合法输入造成一个小而具体的世界动作/结果，让观众认出 D/S 出现过的关系线确实有作用；LEFT 完全同形的 carrier 经过合法接口；BOTTOM 此处是**器乐，没有新歌词**，只能留之前 V 段一个确实唱过的词的导演式回声（若使用，必须明示它不是本段新唱词）。
- <a id="shot-W02"></a>**W02 03:17.800–03:20.150｜剑指屏幕**：RIGHT Kris 看到了结果与自己无法直接触及的外来作用，剑尖正对摄像机；**先给他的动机——想碰到影响自己的东西——再给持剑动作**。LEFT 稳定维持载体，不提前崩坏。观看者突然成为被人物观看的一方。
- <a id="shot-W03"></a>**W03 03:20.150–03:23.100｜CROSSING W：右→下**：RIGHT Kris 以一次短暂的刀/手配合切开**局部边界**，从右框探手到下方歌词框，确实握住 V 段 trapped 等真实声学来源的回声词，捏碎成少量字符光点；BOTTOM 原词可读直到抓握，一次后变形，不让整条歌词栏碎掉；LEFT 只出现这次接触造成的**一次局部 carrier 偏转**，不是软件界面被全面黑客入侵。
- <a id="shot-W04"></a>**W04 03:23.100–03:25.375｜退后一眼**：RIGHT Kris 身体仍留在 WORLD，手收回，一条曾经不可跨的小缝留下可见痕迹；摄像机沿同一条关系看见 WORLD 是一个更大的可观察结构中的小部分，但**固定三框在全片级别仍原位**。LEFT 字符重新稳定，BOTTOM 回器乐空白。全景静默比出现另一个套娃圆环更好。
- **终极备选（由作者裁决才允许）**：真正刀碎观众**整个画布**、身体跳入左侧代码海、三框永久解体，是一个竞争性高潮方案，会冲突既有局部访问和三框固定原则，**不能同时叠加进 W 主版**。作者原始构想完整保留在文末；如 rough 证明其必要性，再由作者单独改定 W 与 G 的冲击分配。
- **分工**：G 是世界越入代码，W 是主体触碰语言 / 凝视；它们不是两次同样的碎屏。

<a id="scene-X"></a>
### X · 03:25.375–03:27.083｜Final Execution｜「新的一次执行，没有唯一答案」

**一句话**：W 的动作先彻底结束，最后一声 Execution 才在一个新条件下触发一个干净的动作及结果，不给“谁最终执行谁”的标准答案。

- <a id="shot-X01"></a>**X01 03:25.375–03:27.083｜条件→行动→结果**：RIGHT 简短且因果清晰的输入/行动状态：镜头从 W 局部接触**明显换条件**，不给最终 executor 特写；LEFT 只出现一次对应执行与 WORLD 结果的关系；BOTTOM 最后一声 Execution 自动声学 onset 约 **205.372s / f4929**，真实歌词显示一次。**约 f4970 / 207.083333s 硬切**，绝不让 W 的那刀直接导致此处结果。
- **意义**：execution 既是运行，也是具有伦理后果的强制执行；当主体与执行者分层，它不再有唯一答案。

<a id="scene-Y"></a>
### Y · 03:27.083–03:31.917｜After｜「留给一个没有被彻底解释的人」

**一句话**：音乐结束后，只剩 Kris、微小而未闭合的界线与黑暗——回收开场两线交点，却不把整个人物世界删成空白游戏结束卡。

- <a id="shot-Y01"></a>**Y01 03:27.083–03:29.750｜未对上**：RIGHT Kris 与一段未闭合的小亮线/边界，人物稍微偏离完美坐标中心；LEFT 很弱的字符海缓慢停止但三框完整；BOTTOM 无新唱词、不额外补结语。
- <a id="shot-Y02"></a>**Y02 03:29.750–03:31.917｜安静归黑**：三个框都可以随歌曲自然渐暗，**不是结构合并**；若最后问“谁执行谁”，只允许导演层把问题留给观众，不默认放一段英文解释大字。
- **禁止**：不要在此重新召回 Knight / Dess / 1225、一个新幕后人格或任何已被用户否决的唯一结局。

<a id="cast-index"></a>
## 5. 角色留痕索引｜不是轮流报幕的全员剪影

**角色覆盖原则**：重要关系人物需要完整动作；有主题功能的人物可短暂闪现；其他命名 NPC 尽量凭原本场景、家具、店招、背影、职业动作或台词物件被辨认，**而不是强迫观众在几秒内读完 50 张头像**。可见动作优先于报角色名；不能为了凑人数更改角色所属 Chapter / Route / 事件。此索引是导演可调用清单，不声称已核实 Chapter 1–5 所有 NPC 的素材或已为每个人确认一个硬镜头。

| 人物 / 群组 | 首选镜头 / 方式 | 不能失去的角色意义 |
|---|---|---|
| **Kris / Player / SOUL** | A、C、L、M、R、V、W；长期主线 | I=Kris / you=Player；身体、SOUL、输入不自动等同 |
| **Susie** | B 初次拒绝与后来同路，H moss，K 三人合行，R 被保护 | 她有自由回应和真实共同经历 |
| **Ralsei** | C 引路一瞬，K 与两人真实互动 | 是主角团关系中的人，而不只是绿色轮廓 |
| **Noelle** | B 教室，O Dess 缺席，P/Q Weird，T 湖边主动牵引 | 过去、恐惧、力量诱惑、主动目标与命令依赖并存 |
| **Berdly** | B 同班背景，N 交互条件，P SnowGrave 关键瞬间 | 不是单纯被当作数字统计；结局不可擅自宣告 |
| **Toriel（羊妈）** | B 送行、I 生活物件、S 房间 | 生活关系先于“被玩家操纵”的故事 |
| **Asgore（羊爸）** | I 花店/照顾植物、B 家庭回声 | 花与家庭记忆；不虚构 Toriel/Asgore 和好 |
| **Alphys** | B 教室的一次真实招呼 | 一个具体的学校角色 |
| **Catti / Jockington / Temmie / Snowy** | B 教室座位与背景动态，至多选一两个动作特写 | Hometown 社会生活而非无名人群 |
| **Sans、Undyne、其他 Hometown 居民** | B 上学路、I 花店街区可辨店牌/过路，必要时借 R/S 日常回声 | 不是每人都与 Kris 发生强制冲突；只取有原作来源的相容场景 |
| **Rudy** | O 与 Noelle/Dess 家庭或医院记忆 | 给 Dess 的缺席具体的人际重量 |
| **Dess** | O 通过曾经与 Noelle 的共享位置及之后的缺席 | 失踪事实/未知信息与社区联想分开 |
| **Jevil** | F 囚笼中的旋转/自由反讽 | “自由”的不稳定镜像，不给自由理论唯一答案 |
| **Lancer / King** | F 同章单独的玩闹/压迫，K Lancer 城镇回声 | 关系不只有控制和痛苦 |
| **Queen** | D 媒介/舞台的 THEMATIC 插镜，N Weird 条件旁的记忆 | 系统式的表达风格，不让她取代 Player |
| **Sweet、Cap'n、K_K** | D 在音乐/媒体装置里瞬间可辨 | 节奏游戏般的欢快人物层 |
| **Spamton / Spamton NEO** | J 提线与身体，必要时 W 回声只在左框模型象征 | 主体与受控之物的强烈反讽，不代表 Kris = Spamton |
| **Swatch / Swatchlings / Tasque Manager** | J 套进职业/角色切换的背景或姿态 | 不是任意数据标签里的活体样本 |
| **Rouxls Kaard / Seam** | J 夸张姿态、K 商店与熟悉场景 | 王国仍有普通居民、职业和时间 |
| **Starwalker / Nubert / Top Chef / 其他 Castle Town 居民** | K 可辨人物剪影、熟悉道具或同地点短镜 | 可删的层次感，优先确保三人真实互动 |
| **Tenna / 电视世界人物** | D 一次来自 Ch3 的媒介影像，单独 THEMATIC | 媒介与表演主题回声，不写跨章同台事实 |
| **Gerson / Alvin** | U 教堂/钢琴/物件、J 职业角色回声 | 以记忆和遗迹留痕，不擅自作为事件当场人物 |
| **Knight（身份未知）** | J 极轻的职业标签，**不显示人脸候选** | role 有意义，但不回答谁是 Knight |
| **Ch4/Ch5 其他有证据命名角色** | D/J/K/S/T 的源场景真实过路位置；优先预览素材再指定具体帧 | 不因“尽量全员”而虚构出场或身份 |

新增任何角色时，在对应卡写明：具体镜头 ID、来源 Chapter/Route、出现为**在场/回忆/符号/物件**哪一种、其动作对主歌词意义有什么作用。不能仅因某个小 NPC 没被提到就挪走主角的关键表演时间。

<a id="critical-motifs"></a>
## 6. 主镜头与事实界限｜审稿不能误改的地方

| 关键事件 | 唯一/主要位置 | 事实与导演边界 |
|---|---|---|
| **Vessel 的头/身/腿滚动拼接、残影出现 Kris** | A02/A03 | 必须让观众误认为创建成功，但不能声明 Vessel 正式生成 Kris；保留 creator/vessel 两个独立字段 |
| **两条光线交会、Kris 落进小花丛** | A01/A04 | 作者原创开场，花受力；不将“世界刚刚创造 Kris”写作 canon |
| **参数化 Kris 点阵/字符/代码海** | C01–C04 以 LEFT 为主 | MODEL 的数据来自可见身体；description ≠ person |
| **PROCEED** | N02、P03；T 可极弱记忆 | 是有条件的原作交互与心理压迫，不是所有歌词里的 Execute 的同义按钮 |
| **掏心** | L02/L03 | 至少可读三事实；不能仅闪一帧当彩蛋 |
| **Dess / 1225** | O；C/J 低权重种子 | COMMUNITY READING 不能升格为失踪日期/坐标/答案 |
| **SnowGrave / Berdly** | P04 | 剧情触发条件、Noelle 的施法与结果需清楚，不能任意判定 Berdly 的最终状态 |
| **HERO_SWORD / Kris 自主保护 Susie** | R02/R03 | 控制在 Sword、Kris 身体自主保护；必须保留威胁前提与事件身份 |
| **Kris 延迟起床** | S01–S03 | 原因未知；不能拍成单纯仇恨 Player |
| **Noelle 带路再寻求指令** | T01–T03 | agency 先成立，再让依赖成立 |
| **完整选择与 Kris 咬手** | U01/U02 | 完整原选项提交，身体回应不等同字面选择 |
| **Player 能停止/离开** | V01–V03 | 必须真实成立，不能重新塞进绝对监牢 |
| **喷泉后斩左右框/代码海** | G03/G04 | **CROSSING G**，有明确空间通道与字符海后果；是 ORIGINAL 大胆导演版 |
| **Kris 持剑指向观众/抓碎歌词** | W02/W03 | **CROSSING W**，默认局部接触一次、身体留 WORLD；歌词碎字为前文声学词的导演回声 |
| **真正全屏碎裂** | W 的独立冲突候选 | 不与 G/W 主方案无脑叠加；如采用须作者明确裁决改变空间权限 |
| **最终 Execution** | X01 | f4929 / f4970 硬锁；不是 W 那刀的直接结果，不指定唯一执行者 |

**认识论**：CANON（原游戏内可核验）、STRONG INFERENCE（从事实得出但并未说透）、COMMUNITY READING（1225/Knight 等联想）、ORIGINAL（歌曲的原创视觉译法）必须在改镜时保持分层。不同 Route/Chapter 的素材镜头尽量一看就能辨认是 **THEMATIC CUT**，别靠连续动作伪造成因果。

<a id="author-originals"></a>
## 7. 作者原始构想｜保留原文，允许在既有三框前提下寻找更好的落点

> 开屏黑色背景，两条光线交汇，点亮画面，Kris在虚空中坠落，落地，黑色或深色背景，地面只有一小块花丛。
>
> 容器的头，身，腿不同样式左右滚动拼接，越来越快，直到模糊残影，但就在残影中间诞生了真正的kris
>
> 三维转二维，横向构图，右侧是喷泉，Kris封印喷泉，却回头砍碎了左右框体之间的界限，跳进代码的海洋，打乱代码。
>
> Kris从右侧框体探出手，攥住下面的歌词里的一个词，捏碎，歌词变成字符的光点
>
> Kris持剑指向屏幕，砍碎屏幕
>
> Kris的“参数化”在视觉上表达为Kris化为点阵表示、字符图形化表示
>
> 可以在恰当的时候融合三个框中的两个或全部，使得画面成为一个“共同语义”。比如歌词成为冒险布景、坠入歌词深海、左侧参数和代码出现在世界里成为标记和装饰、Kris砍断框体闯入代码世界、Kris捡起歌词词汇然后捏碎等等
>
> 光影细节以合适的方式成为剧情的服务者
>
> 框体是否可以重组或拼接异化？
>
> 一镜到底与意识流碎片化运镜的交替使用？希区柯克变焦？

**本次经作者更新的结构判定**：以上意象不删，但“普通场景框体可自由融合/重组”现在让位于“原 PV 固定三框，只有 G/W 等明确越框行为破例”的更晚决定。右窗导演仍可用长镜、快速碎片切、有限 3D→2D 和有动机的 Hitchcock zoom；光影服务人物，而不迫使三框交换职责。作者若调整 G/W 或批准完整砍屏，应直接编辑本文件对应镜头，不以新旧多份候选稿并存。

---

**素材/时间入口**：[歌词原文](../input/lyrics.lrc) · [逐词草案](../film/world_execute_word_timing_20260927/word_timeline.json) · [核心剧情基线](deltarune/CORE_STORY_BASELINE.md) · [细节库](deltarune/DETAIL_IDEA_LIBRARY.md) · [上游三框源码](https://github.com/MisakaZentai/world-execute-me-dsh-pv)。本文件没有独立拍摄进度、模型日志或技术验收结论。
