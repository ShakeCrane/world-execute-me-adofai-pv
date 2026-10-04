# 211.9秒 Shot Bible v0.1

2026-10-01；导演稿，已完整覆盖5086帧，尚待游戏视觉与听音验收。机器源由 tools/design_deltarune_plan.py 生成，修改设计需同步生成JSON与本文。每镜使用E证据编号，见01；作者隐喻不作canon。

24fps；帧区间均[start,end)，end不画；时刻由frame/24计算。字幕仅在本地恢复，本文只含语义概括。编号不是原v2 ALL index；不把它们直接填CUTS。

## 连续时间线

| Shot | frame | seconds | section | title | evidence |
|---|---|---|---|---|---|
| DR01 | 0–43 | 0.000–1.792 | connect | 连接先于身体 | E01 |
| DR02 | 43–93 | 1.792–3.875 | connect | 保护的双义 | E01/E04 |
| DR03 | 93–130 | 3.875–5.417 | connect | 可以制造的形状 | E01 |
| DR04 | 130–177 | 5.417–7.375 | connect | 接受主体 | E01 |
| DR05 | 177–243 | 7.375–10.125 | connect | 身份表格 | E01/E02 |
| DR06 | 243–269 | 10.125–11.208 | connect | 收回选择 | E01 |
| DR07 | 269–306 | 11.208–12.750 | connect | 世界已有其人 | E01/E02 |
| DR08 | 306–385 | 12.750–16.042 | connect | 输入与行动 | E03 |
| DR09 | 385–476 | 16.042–19.833 | normal | 一起向前 | E03 |
| DR10 | 476–567 | 19.833–23.625 | normal | 不接受命令 | E03 |
| DR11 | 567–655 | 23.625–27.292 | normal | 合作是关系变化 | E03/E19 |
| DR12 | 655–715 | 27.292–29.792 | normal | 谁的存档名 | E02 |
| DR13 | 715–803 | 29.792–33.458 | identity | 点与身体 | E01/E21 |
| DR14 | 803–890 | 33.458–37.083 | identity | 圆内可选 | E04/E33 |
| DR15 | 890–980 | 37.083–40.833 | identity | 同一波不一样的手 | E21 |
| DR16 | 980–1066 | 40.833–44.417 | identity | 无限仍在框内 | E01/E15 |
| DR17 | 1066–1145 | 44.417–47.708 | nested | 切换控制通道 | E13 |
| DR18 | 1145–1235 | 47.708–51.458 | nested | 只能看此处 | E13/E15 |
| DR19 | 1235–1322 | 51.458–55.083 | nested | 时间也是接口 | E02/E15 |
| DR20 | 1322–1417 | 55.083–59.042 | normal | 靠近不是合并 | E03/E19 |
| DR21 | 1417–1513 | 59.042–63.042 | normal | 可提供的可能性 | E06/E07 |
| DR22 | 1513–1591 | 63.042–66.292 | normal | 最后一根 | E06 |
| DR23 | 1591–1683 | 66.292–70.125 | normal | 动作也可以保护 | E19 |
| DR24 | 1683–1774 | 70.125–73.917 | normal | 落空的自由 | E06/E07 |
| DR25 | 1774–1865 | 73.917–77.708 | care | 供给的能力 | E21 |
| DR26 | 1865–1951 | 77.708–81.292 | care | 给予不等于讨好 | E30 |
| DR27 | 1951–2043 | 81.292–85.125 | care | 角色的回应 | E03/E30 |
| DR28 | 2043–2125 | 85.125–88.542 | care | 存在不靠所有权 | E02 |
| DR29 | 2125–2205 | 88.542–91.875 | care | 同一个人 | E01/E05 |
| DR30 | 2205–2295 | 91.875–95.625 | care | 日夜之外的动作 | E05/E29 |
| DR31 | 2295–2382 | 95.625–99.250 | nested | 舞台角色套住输入 | E13 |
| DR32 | 2382–2485 | 99.250–103.542 | care | 能力与输入共存 | E21 |
| DR33 | 2485–2571 | 103.542–107.125 | normal | 共同振动 | E03/E21 |
| DR34 | 2571–2650 | 107.125–110.417 | normal | 完整不是拥有 | E03/E04/E21 |
| DR35 | 2650–2693 | 110.417–112.208 | separation | 离开身体 | E04 |
| DR36 | 2693–2718 | 112.208–113.250 | separation | 输入仍在 | E04 |
| DR37 | 2718–2734 | 113.250–113.917 | separation | 世界不跟输入退场 | E04 |
| DR38 | 2734–2754 | 113.917–114.750 | separation | 保护变容器 | E04 |
| DR39 | 2754–2784 | 114.750–116.000 | separation | 身体独自行动 | E04/E05 |
| DR40 | 2784–2838 | 116.000–118.250 | separation | 隔离是空间问题 | E20/E23 |
| DR41 | 2838–2928 | 118.250–122.000 | separation | 不是菜单制造的声音 | E23/E25 |
| DR42 | 2928–3014 | 122.000–125.583 | weird | 菜单是一扇门 | E24 |
| DR43 | 3014–3093 | 125.583–128.875 | weird | 偏离也有条件 | E08/E24 |
| DR44 | 3093–3149 | 128.875–131.208 | weird | 路线锁定的代价 | E25/E26 |
| DR45 | 3149–3232 | 131.208–134.667 | weird | 反冲到接口 | E26/E28 |
| DR46 | 3232–3323 | 134.667–138.458 | weird | 命令没有随身体倒下 | E09/E12 |
| DR47 | 3323–3412 | 138.458–142.167 | nested | 逃离需先拿到钥匙 | E15/E16 |
| DR48 | 3412–3549 | 142.167–147.875 | nested | 框外还有框 | E15/E16/E18 |
| DR49 | 3549–3682 | 147.875–153.417 | execution | 命令一至六 | E08/E10 |
| DR50 | 3682–3821 | 153.417–159.208 | execution | 命令七至十二 | E10/E11 |
| DR51 | 3821–3902 | 159.208–162.583 | execution | 谁发出最后呼唤 | E11/E18 |
| DR52 | 3902–3988 | 162.583–166.167 | execution | 走出屏幕 | E18 |
| DR53 | 3988–4072 | 166.167–169.667 | execution | Kris会保护别人 | E19 |
| DR54 | 4072–4164 | 169.667–173.500 | execution | 归来的空白 | E27/E28 |
| DR55 | 4164–4259 | 173.500–177.458 | reverse | 起床的阻力 | E31 |
| DR56 | 4259–4344 | 177.458–181.000 | reverse | 她开始索求命令 | E32 |
| DR57 | 4344–4430 | 181.000–184.583 | reverse | 拒绝仍然向前 | E33 |
| DR58 | 4430–4519 | 184.583–188.292 | reverse | 两个位置同一结果 | E33/E34 |
| DR59 | 4519–4574 | 188.292–190.583 | reverse | 停止也是输入的边界 | E34/E36 |
| DR60 | 4574–4654 | 190.583–193.917 | reverse | 继续的代价 | E34/E36 |
| DR61 | 4654–4760 | 193.917–198.333 | boundary | 把湖留在画面里 | E35 |
| DR62 | 4760–4863 | 198.333–202.625 | boundary | 上游也有接口 | E01/E15/E35 |
| DR63 | 4863–4929 | 202.625–205.375 | boundary | 不急于给答案 | E35/E36 |
| DR64 | 4929–4970 | 205.375–207.083 | boundary | 提交至章节边界 | E35 |
| DR65 | 4970–5004 | 207.083–208.500 | final | 要求来自下一层 | E35 |
| DR66 | 5004–5051 | 208.500–210.458 | final | 调用方向未定 | E04/E18/E33/E35/E36 |
| DR67 | 5051–5086 | 210.458–211.917 | final | 谁在执行谁 | E01/E04/E18/E33/E35/E36 |

## 逐镜头元素与实现

### DR01 — 连接先于身体

- 范围：0–43 exclusive；0.000000–1.791667s。
- 音乐：启动供电；line IDs [0]。详细word/frame锚点保存在JSON，不复制歌词。
- Chapter/Route：1 / opening；证据 E01。
- 叙述目的：先让观众体验输入的到来。
- Player：输入可定制，但主体选择最终被收回；Kris：尚未出现；Kris身份将由切换揭露；他者：未出现；Story：creation/discard流程决定可接受主体。
- Camera/Layout：full；世界占满24,56,1164,604；Kris必须在世界中有锚点；控制框可退到边缘，底带固定。
- Foreground：中央一点红心；未出现角色。用途：把主体动作/受输入的对象放在第一阅读层。
- Background：黑色空场与微弱水平线。用途：提供该镜空间边界与关系，避免无意义装饰。
- UI：只有外框四角。用途：显现可选行动、输入归属与当前限制。
- Text：CONTACT（游戏窗口概念）；短菜单/名称或明确作者标记，非歌词/新增角色对白。
- Character：Kris（主体将揭露；vessel不等于Kris）；原创程序化轮廓study；最终美术未验收。
- SOUL：由一点长成几何心；指示同一输入入口的空间位置，不裁定灵魂本体身份。
- In：从黑场显现；Out：水平线变成白框边。
- Colour：#070A14, #E7E9F2, #F04462, #75A58B；Motion：1–8帧红点出现，随后心轻浮；无random glitch；Effects：仅接触点窄glow、低强scanline；冲突段可路线触发glitch，不能遮心/手/选项。
- 复用：film/tui_pv_world_execute_20260926/continuity_full_v2/v2.py: FULL_ART slide staging (design reuse)；film/tui_pv_world_execute_20260926/tuikit.py: post。保留/替换：KEEP分层/读区；ADAPT pane/载体；REPLACE原DSH/模型视觉；REMOVE本片舞者。
- 新代码：dr_layers.full_world, dr_timeline.integer_slide, s_dr_connect.shot_dr01（此处是实现计划，并非已经实现）。
- 技术：PIL/RGBA；直接复用font；旧monkey patch为零；section计划路径 film/deltarune/s_dr_connect.py。HTML不必需；原创透明角色/布景预渲染可选。
- PoC：无；not yet rendered。
- Asset：Kris原创轮廓与该镜几何场景；study可程序化；生产美术与游戏画面核对待完成。
- 待问/限制：首帧是否要0还是首词frame1：目前0黑/1显现。
- Still QA：[0, 6, 21, 42]；关键事件：[]。

### DR02 — 保护的双义

- 范围：43–93 exclusive；1.791667–3.875000s。
- 音乐：安全保护与边界；line IDs [1, 2]。详细word/frame锚点保存在JSON，不复制歌词。
- Chapter/Route：1 / opening / visual foreshadow；证据 E01 E04。
- 叙述目的：保护图形以后回成囚心的cage。
- Player：输入可定制，但主体选择最终被收回；Kris：尚未出现；Kris身份将由切换揭露；他者：未出现；Story：creation/discard流程决定可接受主体。
- Camera/Layout：full；世界占满24,56,1164,604；Kris必须在世界中有锚点；控制框可退到边缘，底带固定。
- Foreground：红心位于未闭合白框。用途：把主体动作/受输入的对象放在第一阅读层。
- Background：四角缓慢连接，无角色。用途：提供该镜空间边界与关系，避免无意义装饰。
- UI：框内输入仍可移动。用途：显现可选行动、输入归属与当前限制。
- Text：无；无。
- Character：Kris（主体将揭露；vessel不等于Kris）；原创程序化轮廓study；最终美术未验收。
- SOUL：中心到左侧，尚无身体连接；指示同一输入入口的空间位置，不裁定灵魂本体身份。
- In：承接DR01：水平线变成白框边；Out：框角拆成vessel零件。
- Colour：#070A14, #E7E9F2, #F04462, #75A58B；Motion：白框从四角闭合，保留一边缺口；Effects：仅接触点窄glow、低强scanline；冲突段可路线触发glitch，不能遮心/手/选项。
- 复用：film/tui_pv_world_execute_20260926/continuity_full_v2/v2.py: FULL_ART slide staging (design reuse)；film/tui_pv_world_execute_20260926/tuikit.py: post。保留/替换：KEEP分层/读区；ADAPT pane/载体；REPLACE原DSH/模型视觉；REMOVE本片舞者。
- 新代码：dr_layers.full_world, dr_timeline.integer_slide, s_dr_connect.shot_dr02（此处是实现计划，并非已经实现）。
- 技术：PIL/RGBA；直接复用font；旧monkey patch为零；section计划路径 film/deltarune/s_dr_connect.py。HTML不必需；原创透明角色/布景预渲染可选。
- PoC：无；not yet rendered。
- Asset：Kris原创轮廓与该镜几何场景；study可程序化；生产美术与游戏画面核对待完成。
- 待问/限制：这是作者预示，不伪装opening实有cage。
- Still QA：[43, 49, 68, 92]；关键事件：[]。

### DR03 — 可以制造的形状

- 范围：93–130 exclusive；3.875000–5.416667s。
- 音乐：零件排列；line IDs [2]。详细word/frame锚点保存在JSON，不复制歌词。
- Chapter/Route：1 / opening；证据 E01。
- 叙述目的：先授予可定制的错觉。
- Player：输入可定制，但主体选择最终被收回；Kris：尚未出现；Kris身份将由切换揭露；他者：未出现；Story：creation/discard流程决定可接受主体。
- Camera/Layout：split；固定1280×720；左主体24,56,384,604，右世界404,56,1164,604；上框/底带不随镜头变换。
- Foreground：灰头/躯干/腿的几何部件。用途：把主体动作/受输入的对象放在第一阅读层。
- Background：左pane形成，右三个部件位置。用途：提供该镜空间边界与关系，避免无意义装饰。
- UI：稀疏选择格。用途：显现可选行动、输入归属与当前限制。
- Text：HEAD / BODY / LEGS（菜单短词）；短菜单/名称或明确作者标记，非歌词/新增角色对白。
- Character：Kris（主体将揭露；vessel不等于Kris）；原创程序化轮廓study；最终美术未验收。
- SOUL：selector依次定位三个部件；指示同一输入入口的空间位置，不裁定灵魂本体身份。
- In：承接DR02：框角拆成vessel零件；Out：零件贴合到左主体槽。
- Colour：#070A14, #E7E9F2, #F04462, #75A58B；Motion：部件按2次beat定位，禁止角色鬼脸；Effects：仅接触点窄glow、低强scanline；冲突段可路线触发glitch，不能遮心/手/选项。
- 复用：film/tui_pv_world_execute_20260926/continuity_full_v2/kit.py: transparent her_layer/chrome separation (design reuse)；film/tui_pv_world_execute_20260926/tuikit.py: font/scale_alpha/post。保留/替换：KEEP分层/读区；ADAPT pane/载体；REPLACE原DSH/模型视觉；REMOVE本片舞者。
- 新代码：dr_ui.control_pane, dr_ui.kris_study, dr_layers.world_body, s_dr_connect.shot_dr03（此处是实现计划，并非已经实现）。
- 技术：PIL/RGBA；直接复用font；旧monkey patch为零；section计划路径 film/deltarune/s_dr_connect.py。HTML不必需；原创透明角色/布景预渲染可选。
- PoC：无；not yet rendered。
- Asset：Kris原创轮廓与该镜几何场景；study可程序化；生产美术与游戏画面核对待完成。
- 待问/限制：vessel不使用导出原sprite。
- Still QA：[93, 99, 111, 129]；关键事件：[]。

### DR04 — 接受主体

- 范围：130–177 exclusive；5.416667–7.375000s。
- 音乐：对象被创建；line IDs [3]。详细word/frame锚点保存在JSON，不复制歌词。
- Chapter/Route：1 / opening；证据 E01。
- 叙述目的：输入只决定临时vessel，不等于Kris。
- Player：输入可定制，但主体选择最终被收回；Kris：尚未出现；Kris身份将由切换揭露；他者：未出现；Story：creation/discard流程决定可接受主体。
- Camera/Layout：split；固定1280×720；左主体24,56,384,604，右世界404,56,1164,604；上框/底带不随镜头变换。
- Foreground：灰色vessel组合轮廓。用途：把主体动作/受输入的对象放在第一阅读层。
- Background：右侧空的角色世界框。用途：提供该镜空间边界与关系，避免无意义装饰。
- UI：接受位置被心指向。用途：显现可选行动、输入归属与当前限制。
- Text：ACCEPT（短菜单）；短菜单/名称或明确作者标记，非歌词/新增角色对白。
- Character：Kris（主体将揭露；vessel不等于Kris）；原创程序化轮廓study；最终美术未验收。
- SOUL：心落在接受项，线连临时身体；指示同一输入入口的空间位置，不裁定灵魂本体身份。
- In：承接DR03：零件贴合到左主体槽；Out：选择格延展为参数行。
- Colour：#070A14, #E7E9F2, #F04462, #75A58B；Motion：轮廓合并，不发胜利闪光；Effects：仅接触点窄glow、低强scanline；冲突段可路线触发glitch，不能遮心/手/选项。
- 复用：film/tui_pv_world_execute_20260926/continuity_full_v2/kit.py: transparent her_layer/chrome separation (design reuse)；film/tui_pv_world_execute_20260926/tuikit.py: font/scale_alpha/post。保留/替换：KEEP分层/读区；ADAPT pane/载体；REPLACE原DSH/模型视觉；REMOVE本片舞者。
- 新代码：dr_ui.control_pane, dr_ui.kris_study, dr_layers.world_body, s_dr_connect.shot_dr04（此处是实现计划，并非已经实现）。
- 技术：PIL/RGBA；直接复用font；旧monkey patch为零；section计划路径 film/deltarune/s_dr_connect.py。HTML不必需；原创透明角色/布景预渲染可选。
- PoC：无；not yet rendered。
- Asset：Kris原创轮廓与该镜几何场景；study可程序化；生产美术与游戏画面核对待完成。
- 待问/限制：不要暗示这个vessel将在本PV拥有自主剧情。
- Still QA：[130, 136, 153, 176]；关键事件：[]。

### DR05 — 身份表格

- 范围：177–243 exclusive；7.375000–10.125000s。
- 音乐：填写参数；line IDs [4]。详细word/frame锚点保存在JSON，不复制歌词。
- Chapter/Route：1 / opening；证据 E01 E02。
- 叙述目的：身体信息和creator name是不同层。
- Player：输入可定制，但主体选择最终被收回；Kris：尚未出现；Kris身份将由切换揭露；他者：未出现；Story：creation/discard流程决定可接受主体。
- Camera/Layout：split；固定1280×720；左主体24,56,384,604，右世界404,56,1164,604；上框/底带不随镜头变换。
- Foreground：左vessel轮廓，右name两栏。用途：把主体动作/受输入的对象放在第一阅读层。
- Background：无DarkWorld截图。用途：提供该镜空间边界与关系，避免无意义装饰。
- UI：名字卡和光标。用途：显现可选行动、输入归属与当前限制。
- Text：VESSEL / CREATOR（作者分类标记）；短菜单/名称或明确作者标记，非歌词/新增角色对白。
- Character：Kris（主体将揭露；vessel不等于Kris）；原创程序化轮廓study；最终美术未验收。
- SOUL：在两行之间移动；指示同一输入入口的空间位置，不裁定灵魂本体身份。
- In：承接DR04：选择格延展为参数行；Out：表格突然失去vessel栏。
- Colour：#070A14, #E7E9F2, #F04462, #75A58B；Motion：name卡滑入，轮廓保持不动；Effects：仅接触点窄glow、低强scanline；冲突段可路线触发glitch，不能遮心/手/选项。
- 复用：film/tui_pv_world_execute_20260926/continuity_full_v2/kit.py: transparent her_layer/chrome separation (design reuse)；film/tui_pv_world_execute_20260926/tuikit.py: font/scale_alpha/post。保留/替换：KEEP分层/读区；ADAPT pane/载体；REPLACE原DSH/模型视觉；REMOVE本片舞者。
- 新代码：dr_ui.control_pane, dr_ui.kris_study, dr_layers.world_body, s_dr_connect.shot_dr05（此处是实现计划，并非已经实现）。
- 技术：PIL/RGBA；直接复用font；旧monkey patch为零；section计划路径 film/deltarune/s_dr_connect.py。HTML不必需；原创透明角色/布景预渲染可选。
- PoC：无；not yet rendered。
- Asset：Kris原创轮廓与该镜几何场景；study可程序化；生产美术与游戏画面核对待完成。
- 待问/限制：不显示虚构输入者姓名。
- Still QA：[177, 183, 210, 242]；关键事件：[]。

### DR06 — 收回选择

- 范围：243–269 exclusive；10.125000–11.208333s。
- 音乐：初始化的断点；line IDs [5, 6]。详细word/frame锚点保存在JSON，不复制歌词。
- Chapter/Route：1 / opening；证据 E01。
- 叙述目的：最早的自由收回发生在路线分歧之前。
- Player：输入可定制，但主体选择最终被收回；Kris：尚未出现；Kris身份将由切换揭露；他者：未出现；Story：creation/discard流程决定可接受主体。
- Camera/Layout：close；右世界占主要面积；左仍留Kris胸/手轮廓；选择框最小字高24px；心不被glow盖住。
- Foreground：vessel槽变空；Kris轮廓接入。用途：把主体动作/受输入的对象放在第一阅读层。
- Background：白框完整而选项消失。用途：提供该镜空间边界与关系，避免无意义装饰。
- UI：输入格退到框外。用途：显现可选行动、输入归属与当前限制。
- Text：KRIS（主体名）；短菜单/名称或明确作者标记，非歌词/新增角色对白。
- Character：Kris（主体将揭露；vessel不等于Kris）；原创程序化轮廓study；最终美术未验收。
- SOUL：原selector停在空格，身体不由它改形；指示同一输入入口的空间位置，不裁定灵魂本体身份。
- In：承接DR05：表格突然失去vessel栏；Out：黑空格扩为房间。
- Colour：#070A14, #E7E9F2, #F04462, #75A58B；Motion：243–248淡去vessel；249–254显Kris；255以后hold；Effects：仅接触点窄glow、低强scanline；冲突段可路线触发glitch，不能遮心/手/选项。
- 复用：film/tui_pv_world_execute_20260926/tuikit.py: font/post；film/pv_dsh_frontend_20260927/dsh_her.py: LEAD readability principle (design reuse)。保留/替换：KEEP分层/读区；ADAPT pane/载体；REPLACE原DSH/模型视觉；REMOVE本片舞者。
- 新代码：dr_ui.choice_box, dr_layers.hand_detail, dr_timeline.choice_events, s_dr_connect.shot_dr06（此处是实现计划，并非已经实现）。
- 技术：PIL/RGBA；直接复用font；旧monkey patch为零；section计划路径 film/deltarune/s_dr_connect.py。HTML不必需；原创透明角色/布景预渲染可选。
- PoC：无；not yet rendered。
- Asset：Kris原创轮廓与该镜几何场景；study可程序化；生产美术与游戏画面核对待完成。
- 待问/限制：discard文字不贴整句原对白。
- Still QA：[243, 249, 256, 268]；关键事件：['K01']。

### DR07 — 世界已有其人

- 范围：269–306 exclusive；11.208333–12.750000s。
- 音乐：新世界建立；line IDs [6]。详细word/frame锚点保存在JSON，不复制歌词。
- Chapter/Route：1 / normal；证据 E01 E02。
- 叙述目的：Kris已有身体/家庭空间，非从零人格。
- Player：可帮助、选择，不能替角色决定所有回应；Kris：有身体/偏好，选择与表达可能不同；他者：可拒绝或主动合作；Story：菜单提供有限行动与已设结果。
- Camera/Layout：split；固定1280×720；左主体24,56,384,604，右世界404,56,1164,604；上框/底带不随镜头变换。
- Foreground：Kris遮眼轮廓与手。用途：把主体动作/受输入的对象放在第一阅读层。
- Background：程序化卧室地面/窗/门。用途：提供该镜空间边界与关系，避免无意义装饰。
- UI：输入小框出现于左上。用途：显现可选行动、输入归属与当前限制。
- Text：无；无。
- Character：Kris；原创程序化轮廓study；最终美术未验收。
- SOUL：心由menu进入胸口位置；指示同一输入入口的空间位置，不裁定灵魂本体身份。
- In：承接DR06：黑空格扩为房间；Out：门的白线延展成道路。
- Colour：#070A14, #E7E9F2, #F04462, #75A58B；Motion：窗光从右进，不把Kris改成噪声；Effects：仅接触点窄glow、低强scanline；冲突段可路线触发glitch，不能遮心/手/选项。
- 复用：film/tui_pv_world_execute_20260926/continuity_full_v2/kit.py: transparent her_layer/chrome separation (design reuse)；film/tui_pv_world_execute_20260926/tuikit.py: font/scale_alpha/post。保留/替换：KEEP分层/读区；ADAPT pane/载体；REPLACE原DSH/模型视觉；REMOVE本片舞者。
- 新代码：dr_ui.control_pane, dr_ui.kris_study, dr_layers.world_body, s_dr_connect.shot_dr07（此处是实现计划，并非已经实现）。
- 技术：PIL/RGBA；直接复用font；旧monkey patch为零；section计划路径 film/deltarune/s_dr_connect.py。HTML不必需；原创透明角色/布景预渲染可选。
- PoC：无；not yet rendered。
- Asset：Kris原创轮廓与该镜几何场景；study可程序化；生产美术与游戏画面核对待完成。
- 待问/限制：房间布局是原创概括，非游戏像素复刻。
- Still QA：[269, 275, 287, 305]；关键事件：[]。

### DR08 — 输入与行动

- 范围：306–385 exclusive；12.750000–16.041667s。
- 音乐：开始可行动的世界；line IDs [7]。详细word/frame锚点保存在JSON，不复制歌词。
- Chapter/Route：1 / normal；证据 E03。
- 叙述目的：先建立控制可带来共同探索。
- Player：可帮助、选择，不能替角色决定所有回应；Kris：有身体/偏好，选择与表达可能不同；他者：可拒绝或主动合作；Story：菜单提供有限行动与已设结果。
- Camera/Layout：split；固定1280×720；左主体24,56,384,604，右世界404,56,1164,604；上框/底带不随镜头变换。
- Foreground：Kris沿右向路径走，左保留主体框。用途：把主体动作/受输入的对象放在第一阅读层。
- Background：门连到一条可走的地图线。用途：提供该镜空间边界与关系，避免无意义装饰。
- UI：四方向点一次，右侧响应一次。用途：显现可选行动、输入归属与当前限制。
- Text：无；无。
- Character：Kris；原创程序化轮廓study；最终美术未验收。
- SOUL：胸口心随身体位置，输入来源在屏外；指示同一输入入口的空间位置，不裁定灵魂本体身份。
- In：承接DR07：门的白线延展成道路；Out：路径延长，镜头驻留。
- Colour：#070A14, #E7E9F2, #F04462, #75A58B；Motion：两次清晰input→step，0.2s以内回应；Effects：仅接触点窄glow、低强scanline；冲突段可路线触发glitch，不能遮心/手/选项。
- 复用：film/tui_pv_world_execute_20260926/continuity_full_v2/kit.py: transparent her_layer/chrome separation (design reuse)；film/tui_pv_world_execute_20260926/tuikit.py: font/scale_alpha/post。保留/替换：KEEP分层/读区；ADAPT pane/载体；REPLACE原DSH/模型视觉；REMOVE本片舞者。
- 新代码：dr_ui.control_pane, dr_ui.kris_study, dr_layers.world_body, s_dr_connect.shot_dr08（此处是实现计划，并非已经实现）。
- 技术：PIL/RGBA；直接复用font；旧monkey patch为零；section计划路径 film/deltarune/s_dr_connect.py。HTML不必需；原创透明角色/布景预渲染可选。
- PoC：无；not yet rendered。
- Asset：Kris原创轮廓与该镜几何场景；study可程序化；生产美术与游戏画面核对待完成。
- 待问/限制：不能把映射延迟说成游戏实际输入延迟。
- Still QA：[306, 312, 345, 384]；关键事件：[]。

### DR09 — 一起向前

- 范围：385–476 exclusive；16.041667–19.833333s。
- 音乐：器乐第一次舒展；line IDs []。详细word/frame锚点保存在JSON，不复制歌词。
- Chapter/Route：1 / normal；证据 E03。
- 叙述目的：在冲突前建立帮助/信任。
- Player：可帮助、选择，不能替角色决定所有回应；Kris：有身体/偏好，选择与表达可能不同；他者：可拒绝或主动合作；Story：菜单提供有限行动与已设结果。
- Camera/Layout：split；固定1280×720；左主体24,56,384,604，右世界404,56,1164,604；上框/底带不随镜头变换。
- Foreground：Kris居中，Susie远端影子。用途：把主体动作/受输入的对象放在第一阅读层。
- Background：DarkWorld简化地面无敌人素材。用途：提供该镜空间边界与关系，避免无意义装饰。
- UI：ACT/SPARE格只作可选动作grammar。用途：显现可选行动、输入归属与当前限制。
- Text：ACT / SPARE；短菜单/名称或明确作者标记，非歌词/新增角色对白。
- Character：Kris；原创程序化轮廓study；最终美术未验收。
- SOUL：心选一项，白线由Kris连到他者；指示同一输入入口的空间位置，不裁定灵魂本体身份。
- In：承接DR08：路径延长，镜头驻留；Out：合作线遇到另一条自发动作线。
- Colour：#070A14, #E7E9F2, #F04462, #75A58B；Motion：角色轮廓相距一pane，不跑动刷屏；Effects：仅接触点窄glow、低强scanline；冲突段可路线触发glitch，不能遮心/手/选项。
- 复用：film/tui_pv_world_execute_20260926/continuity_full_v2/kit.py: transparent her_layer/chrome separation (design reuse)；film/tui_pv_world_execute_20260926/tuikit.py: font/scale_alpha/post。保留/替换：KEEP分层/读区；ADAPT pane/载体；REPLACE原DSH/模型视觉；REMOVE本片舞者。
- 新代码：dr_ui.control_pane, dr_ui.kris_study, dr_layers.world_body, s_dr_normal.shot_dr09（此处是实现计划，并非已经实现）。
- 技术：PIL/RGBA；直接复用font；旧monkey patch为零；section计划路径 film/deltarune/s_dr_normal.py。HTML不必需；原创透明角色/布景预渲染可选。
- PoC：无；not yet rendered。
- Asset：Kris原创轮廓与该镜几何场景；study可程序化；生产美术与游戏画面核对待完成。
- 待问/限制：具体combat复刻等后续游戏QA。
- Still QA：[385, 391, 430, 475]；关键事件：[]。

### DR10 — 不接受命令

- 范围：476–567 exclusive；19.833333–23.625000s。
- 音乐：器乐动作重拍；line IDs []。详细word/frame锚点保存在JSON，不复制歌词。
- Chapter/Route：1 / normal；证据 E03。
- 叙述目的：他者不是永远服从Player。
- Player：可帮助、选择，不能替角色决定所有回应；Kris：有身体/偏好，选择与表达可能不同；他者：可拒绝或主动合作；Story：菜单提供有限行动与已设结果。
- Camera/Layout：split；固定1280×720；左主体24,56,384,604，右世界404,56,1164,604；上框/底带不随镜头变换。
- Foreground：Kris手留在指挥位置；Susie自发前冲。用途：把主体动作/受输入的对象放在第一阅读层。
- Background：battle地面和空目标格。用途：提供该镜空间边界与关系，避免无意义装饰。
- UI：Susie的命令位置退灰，自动攻击轨迹仍亮。用途：显现可选行动、输入归属与当前限制。
- Text：无；无。
- Character：Kris；原创程序化轮廓study；最终美术未验收。
- SOUL：仍指menu，不能随她攻击轨迹走；指示同一输入入口的空间位置，不裁定灵魂本体身份。
- In：承接DR09：合作线遇到另一条自发动作线；Out：两条轨迹分开后重新靠近。
- Colour：#070A14, #E7E9F2, #F04462, #75A58B；Motion：按键闪一次、她从自身位置动作一次；Effects：仅接触点窄glow、低强scanline；冲突段可路线触发glitch，不能遮心/手/选项。
- 复用：film/tui_pv_world_execute_20260926/continuity_full_v2/kit.py: transparent her_layer/chrome separation (design reuse)；film/tui_pv_world_execute_20260926/tuikit.py: font/scale_alpha/post。保留/替换：KEEP分层/读区；ADAPT pane/载体；REPLACE原DSH/模型视觉；REMOVE本片舞者。
- 新代码：dr_ui.control_pane, dr_ui.kris_study, dr_layers.world_body, s_dr_normal.shot_dr10（此处是实现计划，并非已经实现）。
- 技术：PIL/RGBA；直接复用font；旧monkey patch为零；section计划路径 film/deltarune/s_dr_normal.py。HTML不必需；原创透明角色/布景预渲染可选。
- PoC：无；not yet rendered。
- Asset：Kris原创轮廓与该镜几何场景；study可程序化；生产美术与游戏画面核对待完成。
- 待问/限制：不画Susie永远不受控；下一镜必须回合作。
- Still QA：[476, 482, 521, 566]；关键事件：[]。

### DR11 — 合作是关系变化

- 范围：567–655 exclusive；23.625000–27.291667s。
- 音乐：器乐回收；line IDs []。详细word/frame锚点保存在JSON，不复制歌词。
- Chapter/Route：1 / normal；证据 E03 E19。
- 叙述目的：从拒绝到主动共同动作。
- Player：可帮助、选择，不能替角色决定所有回应；Kris：有身体/偏好，选择与表达可能不同；他者：可拒绝或主动合作；Story：菜单提供有限行动与已设结果。
- Camera/Layout：split；固定1280×720；左主体24,56,384,604，右世界404,56,1164,604；上框/底带不随镜头变换。
- Foreground：Kris和Susie轮廓站同一地面。用途：把主体动作/受输入的对象放在第一阅读层。
- Background：右世界框暖光恢复。用途：提供该镜空间边界与关系，避免无意义装饰。
- UI：选择位置可读但不是占有许可。用途：显现可选行动、输入归属与当前限制。
- Text：无；无。
- Character：Kris；原创程序化轮廓study；最终美术未验收。
- SOUL：心回Kris，不新增Susie soul；指示同一输入入口的空间位置，不裁定灵魂本体身份。
- In：承接DR10：两条轨迹分开后重新靠近；Out：双向线落入SAVE卡。
- Colour：#070A14, #E7E9F2, #F04462, #75A58B；Motion：白连接改双向，角色各停一步；Effects：仅接触点窄glow、低强scanline；冲突段可路线触发glitch，不能遮心/手/选项。
- 复用：film/tui_pv_world_execute_20260926/continuity_full_v2/kit.py: transparent her_layer/chrome separation (design reuse)；film/tui_pv_world_execute_20260926/tuikit.py: font/scale_alpha/post。保留/替换：KEEP分层/读区；ADAPT pane/载体；REPLACE原DSH/模型视觉；REMOVE本片舞者。
- 新代码：dr_ui.control_pane, dr_ui.kris_study, dr_layers.world_body, s_dr_normal.shot_dr11（此处是实现计划，并非已经实现）。
- 技术：PIL/RGBA；直接复用font；旧monkey patch为零；section计划路径 film/deltarune/s_dr_normal.py。HTML不必需；原创透明角色/布景预渲染可选。
- PoC：无；not yet rendered。
- Asset：Kris原创轮廓与该镜几何场景；study可程序化；生产美术与游戏画面核对待完成。
- 待问/限制：不要让双向图解变成canon灵魂机制。
- Still QA：[567, 573, 611, 654]；关键事件：[]。

### DR12 — 谁的存档名

- 范围：655–715 exclusive；27.291667–29.791667s。
- 音乐：器乐末尾停驻；line IDs [9]。详细word/frame锚点保存在JSON，不复制歌词。
- Chapter/Route：1 / normal；证据 E02。
- 叙述目的：控制记录不等同身体身份。
- Player：可帮助、选择，不能替角色决定所有回应；Kris：有身体/偏好，选择与表达可能不同；他者：可拒绝或主动合作；Story：菜单提供有限行动与已设结果。
- Camera/Layout：close；右世界占主要面积；左仍留Kris胸/手轮廓；选择框最小字高24px；心不被glow盖住。
- Foreground：Kris仍在卡旁，手不变。用途：把主体动作/受输入的对象放在第一阅读层。
- Background：SAVE单slot从右世界浮出。用途：提供该镜空间边界与关系，避免无意义装饰。
- UI：Kris name层被creator层覆盖。用途：显现可选行动、输入归属与当前限制。
- Text：KRIS → CREATOR（作者示意）；短菜单/名称或明确作者标记，非歌词/新增角色对白。
- Character：Kris；原创程序化轮廓study；最终美术未验收。
- SOUL：心停在SAVE动作位置；指示同一输入入口的空间位置，不裁定灵魂本体身份。
- In：承接DR11：双向线落入SAVE卡；Out：slot像素拆成身体点云。
- Colour：#070A14, #E7E9F2, #F04462, #75A58B；Motion：只做一层名字覆盖，保留身体轮廓；Effects：仅接触点窄glow、低强scanline；冲突段可路线触发glitch，不能遮心/手/选项。
- 复用：film/tui_pv_world_execute_20260926/tuikit.py: font/post；film/pv_dsh_frontend_20260927/dsh_her.py: LEAD readability principle (design reuse)。保留/替换：KEEP分层/读区；ADAPT pane/载体；REPLACE原DSH/模型视觉；REMOVE本片舞者。
- 新代码：dr_ui.choice_box, dr_layers.hand_detail, dr_timeline.choice_events, s_dr_normal.shot_dr12（此处是实现计划，并非已经实现）。
- 技术：PIL/RGBA；直接复用font；旧monkey patch为零；section计划路径 film/deltarune/s_dr_normal.py。HTML不必需；原创透明角色/布景预渲染可选。
- PoC：无；not yet rendered。
- Asset：Kris原创轮廓与该镜几何场景；study可程序化；生产美术与游戏画面核对待完成。
- 待问/限制：首次SAVE概念，非多周目全角色记忆。
- Still QA：[655, 661, 685, 714]；关键事件：[]。

### DR13 — 点与身体

- 范围：715–803 exclusive；29.791667–33.458333s。
- 音乐：以点集定义自己；line IDs [9, 10, 11]。详细word/frame锚点保存在JSON，不复制歌词。
- Chapter/Route：1 / 4 / normal / thematic crosscut；证据 E01 E21。
- 叙述目的：可计算形体不等于可拥有意愿。
- Player：可帮助、选择，不能替角色决定所有回应；Kris：有身体/偏好，选择与表达可能不同；他者：可拒绝或主动合作；Story：菜单提供有限行动与已设结果。
- Camera/Layout：split；固定1280×720；左主体24,56,384,604，右世界404,56,1164,604；上框/底带不随镜头变换。
- Foreground：点落成Kris衣/手，脸无写实表情。用途：把主体动作/受输入的对象放在第一阅读层。
- Background：右pane相同点密度栅格。用途：提供该镜空间边界与关系，避免无意义装饰。
- UI：选中一片点而不是人格面板。用途：显现可选行动、输入归属与当前限制。
- Text：无；无。
- Character：Kris；原创程序化轮廓study；最终美术未验收。
- SOUL：心有具体位置，不随全点归类成模型；指示同一输入入口的空间位置，不裁定灵魂本体身份。
- In：承接DR12：slot像素拆成身体点云；Out：点环绕身体成一个圆。
- Colour：#070A14, #E7E9F2, #F04462, #75A58B；Motion：稀点到实轮廓；手在点归齐前先动；Effects：仅接触点窄glow、低强scanline；冲突段可路线触发glitch，不能遮心/手/选项。
- 复用：film/tui_pv_world_execute_20260926/continuity_full_v2/kit.py: transparent her_layer/chrome separation (design reuse)；film/tui_pv_world_execute_20260926/tuikit.py: font/scale_alpha/post。保留/替换：KEEP分层/读区；ADAPT pane/载体；REPLACE原DSH/模型视觉；REMOVE本片舞者。
- 新代码：dr_ui.control_pane, dr_ui.kris_study, dr_layers.world_body, s_dr_identity.shot_dr13（此处是实现计划，并非已经实现）。
- 技术：PIL/RGBA；直接复用font；旧monkey patch为零；section计划路径 film/deltarune/s_dr_identity.py。HTML不必需；原创透明角色/布景预渲染可选。
- PoC：无；not yet rendered。
- Asset：Kris原创轮廓与该镜几何场景；study可程序化；生产美术与游戏画面核对待完成。
- 待问/限制：不使用旧whale点云采样源。
- Still QA：[715, 721, 759, 802]；关键事件：[]。

### DR14 — 圆内可选

- 范围：803–890 exclusive；33.458333–37.083333s。
- 音乐：圆与边界长度；line IDs [11, 12]。详细word/frame锚点保存在JSON，不复制歌词。
- Chapter/Route：1 / 5 / normal / motif foreshadow；证据 E04 E33。
- 叙述目的：有多个位置未必有多个结果。
- Player：可帮助、选择，不能替角色决定所有回应；Kris：有身体/偏好，选择与表达可能不同；他者：可拒绝或主动合作；Story：菜单提供有限行动与已设结果。
- Camera/Layout：split；固定1280×720；左主体24,56,384,604，右世界404,56,1164,604；上框/底带不随镜头变换。
- Foreground：Kris位于环外、心在环内。用途：把主体动作/受输入的对象放在第一阅读层。
- Background：圆形menu路径。用途：提供该镜空间边界与关系，避免无意义装饰。
- UI：4个位置相同边框，结果暂未露。用途：显现可选行动、输入归属与当前限制。
- Text：无；无。
- Character：Kris；原创程序化轮廓study；最终美术未验收。
- SOUL：沿弧从一端到另一端；指示同一输入入口的空间位置，不裁定灵魂本体身份。
- In：承接DR13：点环绕身体成一个圆；Out：圆展开为两条并行波。
- Colour：#070A14, #E7E9F2, #F04462, #75A58B；Motion：圆旋转但Kris静止，避免眩晕；Effects：仅接触点窄glow、低强scanline；冲突段可路线触发glitch，不能遮心/手/选项。
- 复用：film/tui_pv_world_execute_20260926/continuity_full_v2/kit.py: transparent her_layer/chrome separation (design reuse)；film/tui_pv_world_execute_20260926/tuikit.py: font/scale_alpha/post。保留/替换：KEEP分层/读区；ADAPT pane/载体；REPLACE原DSH/模型视觉；REMOVE本片舞者。
- 新代码：dr_ui.control_pane, dr_ui.kris_study, dr_layers.world_body, s_dr_identity.shot_dr14（此处是实现计划，并非已经实现）。
- 技术：PIL/RGBA；直接复用font；旧monkey patch为零；section计划路径 film/deltarune/s_dr_identity.py。HTML不必需；原创透明角色/布景预渲染可选。
- PoC：无；not yet rendered。
- Asset：Kris原创轮廓与该镜几何场景；study可程序化；生产美术与游戏画面核对待完成。
- 待问/限制：这里仅预示，不能提前宣称所有选项都一样。
- Still QA：[803, 809, 846, 889]；关键事件：[]。

### DR15 — 同一波不一样的手

- 范围：890–980 exclusive；37.083333–40.833333s。
- 音乐：波形和可接触轨道；line IDs [13, 14, 15]。详细word/frame锚点保存在JSON，不复制歌词。
- Chapter/Route：4 / normal；证据 E21。
- 叙述目的：输入与Kris已有能力可共存。
- Player：可帮助、选择，不能替角色决定所有回应；Kris：有身体/偏好，选择与表达可能不同；他者：可拒绝或主动合作；Story：菜单提供有限行动与已设结果。
- Camera/Layout：split；固定1280×720；左主体24,56,384,604，右世界404,56,1164,604；上框/底带不随镜头变换。
- Foreground：Kris手对着简化键盘。用途：把主体动作/受输入的对象放在第一阅读层。
- Background：一条输入波和一条奏乐动作波。用途：提供该镜空间边界与关系，避免无意义装饰。
- UI：小方向格，不放虚构乐谱。用途：显现可选行动、输入归属与当前限制。
- Text：无；无。
- Character：Kris；原创程序化轮廓study；最终美术未验收。
- SOUL：胸口心稳定，手不完全随selector；指示同一输入入口的空间位置，不裁定灵魂本体身份。
- In：承接DR14：圆展开为两条并行波；Out：波延长撞到最右边界。
- Colour：#070A14, #E7E9F2, #F04462, #75A58B；Motion：两波开始同相，后半手的节奏微提前；Effects：仅接触点窄glow、低强scanline；冲突段可路线触发glitch，不能遮心/手/选项。
- 复用：film/tui_pv_world_execute_20260926/continuity_full_v2/kit.py: transparent her_layer/chrome separation (design reuse)；film/tui_pv_world_execute_20260926/tuikit.py: font/scale_alpha/post。保留/替换：KEEP分层/读区；ADAPT pane/载体；REPLACE原DSH/模型视觉；REMOVE本片舞者。
- 新代码：dr_ui.control_pane, dr_ui.kris_study, dr_layers.world_body, s_dr_identity.shot_dr15（此处是实现计划，并非已经实现）。
- 技术：PIL/RGBA；直接复用font；旧monkey patch为零；section计划路径 film/deltarune/s_dr_identity.py。HTML不必需；原创透明角色/布景预渲染可选。
- PoC：无；not yet rendered。
- Asset：Kris原创轮廓与该镜几何场景；study可程序化；生产美术与游戏画面核对待完成。
- 待问/限制：运动提前是作者隐喻，不是游戏时延事实。
- Still QA：[890, 896, 935, 979]；关键事件：[]。

### DR16 — 无限仍在框内

- 范围：980–1066 exclusive；40.833333–44.416667s。
- 音乐：趋向无限与限制；line IDs [15, 16, 17]。详细word/frame锚点保存在JSON，不复制歌词。
- Chapter/Route：1 / 3 / normal / sword motif；证据 E01 E15。
- 叙述目的：扩展可达空间仍受边界。
- Player：可帮助、选择，不能替角色决定所有回应；Kris：有身体/偏好，选择与表达可能不同；他者：可拒绝或主动合作；Story：菜单提供有限行动与已设结果。
- Camera/Layout：full；世界占满24,56,1164,604；Kris必须在世界中有锚点；控制框可退到边缘，底带固定。
- Foreground：Kris沿路径站在左三分之一。用途：把主体动作/受输入的对象放在第一阅读层。
- Background：网格往外伸，外白框再次出现。用途：提供该镜空间边界与关系，避免无意义装饰。
- UI：选择格仅显示当前两格。用途：显现可选行动、输入归属与当前限制。
- Text：无；无。
- Character：Kris；原创程序化轮廓study；最终美术未验收。
- SOUL：心接近框角，身体不穿框；指示同一输入入口的空间位置，不裁定灵魂本体身份。
- In：承接DR15：波延长撞到最右边界；Out：frame1066电路切向内屏幕。
- Colour：#070A14, #E7E9F2, #F04462, #75A58B；Motion：远景增格不增加字号，最终框阻止路径；Effects：仅接触点窄glow、低强scanline；冲突段可路线触发glitch，不能遮心/手/选项。
- 复用：film/tui_pv_world_execute_20260926/continuity_full_v2/v2.py: FULL_ART slide staging (design reuse)；film/tui_pv_world_execute_20260926/tuikit.py: post。保留/替换：KEEP分层/读区；ADAPT pane/载体；REPLACE原DSH/模型视觉；REMOVE本片舞者。
- 新代码：dr_layers.full_world, dr_timeline.integer_slide, s_dr_identity.shot_dr16（此处是实现计划，并非已经实现）。
- 技术：PIL/RGBA；直接复用font；旧monkey patch为零；section计划路径 film/deltarune/s_dr_identity.py。HTML不必需；原创透明角色/布景预渲染可选。
- PoC：无；not yet rendered。
- Asset：Kris原创轮廓与该镜几何场景；study可程序化；生产美术与游戏画面核对待完成。
- 待问/限制：不要把原数学科普参数留在DR画面。
- Still QA：[980, 986, 1023, 1065]；关键事件：[]。

### DR17 — 切换控制通道

- 范围：1066–1145 exclusive；44.416667–47.708333s。
- 音乐：切换电流方向；line IDs [17, 18, 19]。详细word/frame锚点保存在JSON，不复制歌词。
- Chapter/Route：3 / common / nested motif；证据 E13。
- 叙述目的：控制者也坐在别人的规则里。
- Player：在Kris与小游戏之间切换控制对象；Kris：可抵抗输入、保护他人、退出某控制链；他者：Susie可介入；舞台规则也约束角色；Story：越界须经过游戏已有障碍与触发器。
- Camera/Layout：nested；右侧世界内再置TV内框；左侧Kris维持同尺寸；跨界对象不缩放chrome。
- Foreground：左Kris手握抽象controller。用途：把主体动作/受输入的对象放在第一阅读层。
- Background：右世界里一台无品牌TV框。用途：提供该镜空间边界与关系，避免无意义装饰。
- UI：屏外input→Kris→内游戏连接。用途：显现可选行动、输入归属与当前限制。
- Text：无；无。
- Character：Kris；原创程序化轮廓study；最终美术未验收。
- SOUL：由胸到TV中心的示意连线，不多出第二颗主心；指示同一输入入口的空间位置，不裁定灵魂本体身份。
- In：承接DR16：frame1066电路切向内屏幕；Out：TV边框加粗挡住外侧信息。
- Colour：#070A14, #E7E9F2, #F04462, #75A58B；Motion：连线方向分段点亮；Effects：仅接触点窄glow、低强scanline；冲突段可路线触发glitch，不能遮心/手/选项。
- 复用：film/tui_pv_world_execute_20260926/continuity_full_v2/cuts.py: Frame/content/over concept；film/tui_pv_world_execute_20260926/continuity_full_v2/kit.py: carrier positioning (design reuse)。保留/替换：KEEP分层/读区；ADAPT pane/载体；REPLACE原DSH/模型视觉；REMOVE本片舞者。
- 新代码：dr_layers.inner_game, dr_layers.hero_carrier, dr_timeline.control_target, s_dr_nested.shot_dr17（此处是实现计划，并非已经实现）。
- 技术：PIL/RGBA；直接复用font；旧monkey patch为零；section计划路径 film/deltarune/s_dr_nested.py。HTML不必需；原创透明角色/布景预渲染可选。
- PoC：无；not yet rendered。
- Asset：Kris原创轮廓与该镜几何场景；study可程序化；生产美术与游戏画面核对待完成。
- 待问/限制：controller图形原创，不打包游戏道具sprite。
- Still QA：[1066, 1072, 1105, 1144]；关键事件：[]。

### DR18 — 只能看此处

- 范围：1145–1235 exclusive；47.708333–51.458333s。
- 音乐：视野关闭与眩晕；line IDs [19, 20, 21]。详细word/frame锚点保存在JSON，不复制歌词。
- Chapter/Route：3 / sword；证据 E13 E15。
- 叙述目的：局部视角不能等于世界全貌。
- Player：在Kris与小游戏之间切换控制对象；Kris：可抵抗输入、保护他人、退出某控制链；他者：Susie可介入；舞台规则也约束角色；Story：越界须经过游戏已有障碍与触发器。
- Camera/Layout：nested；右侧世界内再置TV内框；左侧Kris维持同尺寸；跨界对象不缩放chrome。
- Foreground：Kris仍可见，内游戏角色往边缘走。用途：把主体动作/受输入的对象放在第一阅读层。
- Background：TV内小地图、TV外DarkWorld地面。用途：提供该镜空间边界与关系，避免无意义装饰。
- UI：内框裁掉越界方向。用途：显现可选行动、输入归属与当前限制。
- Text：无；无。
- Character：Kris；原创程序化轮廓study；最终美术未验收。
- SOUL：小心留在内selector位置，主身体层不全黑；指示同一输入入口的空间位置，不裁定灵魂本体身份。
- In：承接DR17：TV边框加粗挡住外侧信息；Out：小地图展开为SAVE时间格。
- Colour：#070A14, #E7E9F2, #F04462, #75A58B；Motion：TV内轻旋≤2度，外层稳定；Effects：仅接触点窄glow、低强scanline；冲突段可路线触发glitch，不能遮心/手/选项。
- 复用：film/tui_pv_world_execute_20260926/continuity_full_v2/cuts.py: Frame/content/over concept；film/tui_pv_world_execute_20260926/continuity_full_v2/kit.py: carrier positioning (design reuse)。保留/替换：KEEP分层/读区；ADAPT pane/载体；REPLACE原DSH/模型视觉；REMOVE本片舞者。
- 新代码：dr_layers.inner_game, dr_layers.hero_carrier, dr_timeline.control_target, s_dr_nested.shot_dr18（此处是实现计划，并非已经实现）。
- 技术：PIL/RGBA；直接复用font；旧monkey patch为零；section计划路径 film/deltarune/s_dr_nested.py。HTML不必需；原创透明角色/布景预渲染可选。
- PoC：无；not yet rendered。
- Asset：Kris原创轮廓与该镜几何场景；study可程序化；生产美术与游戏画面核对待完成。
- 待问/限制：旋转是作者视觉语法，不复刻角色晕眩事实。
- Still QA：[1145, 1151, 1190, 1234]；关键事件：[]。

### DR19 — 时间也是接口

- 范围：1235–1322 exclusive；51.458333–55.083333s。
- 音乐：前后时间位置的旅行；line IDs [21, 22]。详细word/frame锚点保存在JSON，不复制歌词。
- Chapter/Route：1 / 3 / normal / thematic crosscut；证据 E02 E15。
- 叙述目的：改变记录受slot/route条件限定。
- Player：在Kris与小游戏之间切换控制对象；Kris：可抵抗输入、保护他人、退出某控制链；他者：Susie可介入；舞台规则也约束角色；Story：越界须经过游戏已有障碍与触发器。
- Camera/Layout：split；固定1280×720；左主体24,56,384,604，右世界404,56,1164,604；上框/底带不随镜头变换。
- Foreground：Kris在固定身体位置。用途：把主体动作/受输入的对象放在第一阅读层。
- Background：两张相同slot先后覆盖。用途：提供该镜空间边界与关系，避免无意义装饰。
- UI：SAVE时刻格不显示虚构chapter6。用途：显现可选行动、输入归属与当前限制。
- Text：SAVE（短词）；短菜单/名称或明确作者标记，非歌词/新增角色对白。
- Character：Kris；原创程序化轮廓study；最终美术未验收。
- SOUL：停在当前slot，不分裂成多玩家；指示同一输入入口的空间位置，不裁定灵魂本体身份。
- In：承接DR18：小地图展开为SAVE时间格；Out：时间格变成party连接位。
- Colour：#070A14, #E7E9F2, #F04462, #75A58B；Motion：已选路径留下淡线，回退卡不让他者苏醒；Effects：仅接触点窄glow、低强scanline；冲突段可路线触发glitch，不能遮心/手/选项。
- 复用：film/tui_pv_world_execute_20260926/continuity_full_v2/kit.py: transparent her_layer/chrome separation (design reuse)；film/tui_pv_world_execute_20260926/tuikit.py: font/scale_alpha/post。保留/替换：KEEP分层/读区；ADAPT pane/载体；REPLACE原DSH/模型视觉；REMOVE本片舞者。
- 新代码：dr_ui.control_pane, dr_ui.kris_study, dr_layers.world_body, s_dr_nested.shot_dr19（此处是实现计划，并非已经实现）。
- 技术：PIL/RGBA；直接复用font；旧monkey patch为零；section计划路径 film/deltarune/s_dr_nested.py。HTML不必需；原创透明角色/布景预渲染可选。
- PoC：无；not yet rendered。
- Asset：Kris原创轮廓与该镜几何场景；study可程序化；生产美术与游戏画面核对待完成。
- 待问/限制：不得暗示Kris记得每次reload。
- Still QA：[1235, 1241, 1278, 1321]；关键事件：[]。

### DR20 — 靠近不是合并

- 范围：1322–1417 exclusive；55.083333–59.041667s。
- 音乐：结合与亲近；line IDs [23, 24]。详细word/frame锚点保存在JSON，不复制歌词。
- Chapter/Route：1 / 3 / normal / thematic crosscut；证据 E03 E19。
- 叙述目的：三人仍有各自行动方向。
- Player：可帮助、选择，不能替角色决定所有回应；Kris：有身体/偏好，选择与表达可能不同；他者：可拒绝或主动合作；Story：菜单提供有限行动与已设结果。
- Camera/Layout：split；固定1280×720；左主体24,56,384,604，右世界404,56,1164,604；上框/底带不随镜头变换。
- Foreground：Kris前景，Susie/Ralsei小影子。用途：把主体动作/受输入的对象放在第一阅读层。
- Background：同一地面，没有舞台统计。用途：提供该镜空间边界与关系，避免无意义装饰。
- UI：菜单退到边缘，世界略亮。用途：显现可选行动、输入归属与当前限制。
- Text：无；无。
- Character：Kris；原创程序化轮廓study；最终美术未验收。
- SOUL：留Kris胸口，线能回馈却不吞并角色；指示同一输入入口的空间位置，不裁定灵魂本体身份。
- In：承接DR19：时间格变成party连接位；Out：三条线成为并列可能性。
- Colour：#070A14, #E7E9F2, #F04462, #75A58B；Motion：角色靠近后保持一身宽间距；Effects：仅接触点窄glow、低强scanline；冲突段可路线触发glitch，不能遮心/手/选项。
- 复用：film/tui_pv_world_execute_20260926/continuity_full_v2/kit.py: transparent her_layer/chrome separation (design reuse)；film/tui_pv_world_execute_20260926/tuikit.py: font/scale_alpha/post。保留/替换：KEEP分层/读区；ADAPT pane/载体；REPLACE原DSH/模型视觉；REMOVE本片舞者。
- 新代码：dr_ui.control_pane, dr_ui.kris_study, dr_layers.world_body, s_dr_normal.shot_dr20（此处是实现计划，并非已经实现）。
- 技术：PIL/RGBA；直接复用font；旧monkey patch为零；section计划路径 film/deltarune/s_dr_normal.py。HTML不必需；原创透明角色/布景预渲染可选。
- PoC：无；not yet rendered。
- Asset：Kris原创轮廓与该镜几何场景；study可程序化；生产美术与游戏画面核对待完成。
- 待问/限制：Ralsei只承担合作，不加管理员暗示。
- Still QA：[1322, 1328, 1369, 1416]；关键事件：[]。

### DR21 — 可提供的可能性

- 范围：1417–1513 exclusive；59.041667–63.041667s。
- 音乐：可能世界与满足；line IDs [25, 26]。详细word/frame锚点保存在JSON，不复制歌词。
- Chapter/Route：2 / normal；证据 E06 E07。
- 叙述目的：Player想帮助也可能误判结果。
- Player：可帮助、选择，不能替角色决定所有回应；Kris：有身体/偏好，选择与表达可能不同；他者：可拒绝或主动合作；Story：菜单提供有限行动与已设结果。
- Camera/Layout：split；固定1280×720；左主体24,56,384,604，右世界404,56,1164,604；上框/底带不随镜头变换。
- Foreground：Kris手对着三条候选细线。用途：把主体动作/受输入的对象放在第一阅读层。
- Background：NEO线的原创新几何轮廓，只一镜前示。用途：提供该镜空间边界与关系，避免无意义装饰。
- UI：ACT选择浮出，其他格淡退。用途：显现可选行动、输入归属与当前限制。
- Text：无；无。
- Character：Kris；原创程序化轮廓study；最终美术未验收。
- SOUL：心选snap概念位置；指示同一输入入口的空间位置，不裁定灵魂本体身份。
- In：承接DR20：三条线成为并列可能性；Out：选中的线抬起，其他线退。
- Colour：#070A14, #E7E9F2, #F04462, #75A58B；Motion：候选线依次伸至同一身体轮廓；Effects：仅接触点窄glow、低强scanline；冲突段可路线触发glitch，不能遮心/手/选项。
- 复用：film/tui_pv_world_execute_20260926/continuity_full_v2/kit.py: transparent her_layer/chrome separation (design reuse)；film/tui_pv_world_execute_20260926/tuikit.py: font/scale_alpha/post。保留/替换：KEEP分层/读区；ADAPT pane/载体；REPLACE原DSH/模型视觉；REMOVE本片舞者。
- 新代码：dr_ui.control_pane, dr_ui.kris_study, dr_layers.world_body, s_dr_normal.shot_dr21（此处是实现计划，并非已经实现）。
- 技术：PIL/RGBA；直接复用font；旧monkey patch为零；section计划路径 film/deltarune/s_dr_normal.py。HTML不必需；原创透明角色/布景预渲染可选。
- PoC：无；not yet rendered。
- Asset：Kris原创轮廓与该镜几何场景；study可程序化；生产美术与游戏画面核对待完成。
- 待问/限制：NEO是主题镜子，不发展成boss介绍。
- Still QA：[1417, 1423, 1465, 1512]；关键事件：[]。

### DR22 — 最后一根

- 范围：1513–1591 exclusive；63.041667–66.291667s。
- 音乐：满足的条件；line IDs [27, 28, 29]。详细word/frame锚点保存在JSON，不复制歌词。
- Chapter/Route：2 / normal；证据 E06。
- 叙述目的：操作上成功不保证自由有支撑。
- Player：可帮助、选择，不能替角色决定所有回应；Kris：有身体/偏好，选择与表达可能不同；他者：可拒绝或主动合作；Story：菜单提供有限行动与已设结果。
- Camera/Layout：close；右世界占主要面积；左仍留Kris胸/手轮廓；选择框最小字高24px；心不被glow盖住。
- Foreground：Kris手/心与一个悬吊小轮廓。用途：把主体动作/受输入的对象放在第一阅读层。
- Background：只剩一根绿白细线，非Kris实物线。用途：提供该镜空间边界与关系，避免无意义装饰。
- UI：确认位置在左，线在右。用途：显现可选行动、输入归属与当前限制。
- Text：无；无。
- Character：Kris；原创程序化轮廓study；最终美术未验收。
- SOUL：selector接近确认，未消失；指示同一输入入口的空间位置，不裁定灵魂本体身份。
- In：承接DR21：选中的线抬起，其他线退；Out：断线末端落进Kris手边。
- Colour：#070A14, #E7E9F2, #F04462, #75A58B；Motion：hold至少12帧后断线；下坠不加blood；Effects：仅接触点窄glow、低强scanline；冲突段可路线触发glitch，不能遮心/手/选项。
- 复用：film/tui_pv_world_execute_20260926/tuikit.py: font/post；film/pv_dsh_frontend_20260927/dsh_her.py: LEAD readability principle (design reuse)。保留/替换：KEEP分层/读区；ADAPT pane/载体；REPLACE原DSH/模型视觉；REMOVE本片舞者。
- 新代码：dr_ui.choice_box, dr_layers.hand_detail, dr_timeline.choice_events, s_dr_normal.shot_dr22（此处是实现计划，并非已经实现）。
- 技术：PIL/RGBA；直接复用font；旧monkey patch为零；section计划路径 film/deltarune/s_dr_normal.py。HTML不必需；原创透明角色/布景预渲染可选。
- PoC：无；not yet rendered。
- Asset：Kris原创轮廓与该镜几何场景；study可程序化；生产美术与游戏画面核对待完成。
- 待问/限制：不配胜利banner。
- Still QA：[1513, 1519, 1552, 1590]；关键事件：[]。

### DR23 — 动作也可以保护

- 范围：1591–1683 exclusive；66.291667–70.125000s。
- 音乐：快乐与运行行动；line IDs [29, 30, 31]。详细word/frame锚点保存在JSON，不复制歌词。
- Chapter/Route：3 / sword / thematic crosscut；证据 E19。
- 叙述目的：Kris不是所有命令的顺从延长线。
- Player：可帮助、选择，不能替角色决定所有回应；Kris：有身体/偏好，选择与表达可能不同；他者：可拒绝或主动合作；Story：菜单提供有限行动与已设结果。
- Camera/Layout：split；固定1280×720；左主体24,56,384,604，右世界404,56,1164,604；上框/底带不随镜头变换。
- Foreground：Kris手拉Susie离开内游戏攻击路径。用途：把主体动作/受输入的对象放在第一阅读层。
- Background：小TV框保留淡边，标此处是重访。用途：提供该镜空间边界与关系，避免无意义装饰。
- UI：危险轨迹与拉开轨迹分色。用途：显现可选行动、输入归属与当前限制。
- Text：无；无。
- Character：Kris；原创程序化轮廓study；最终美术未验收。
- SOUL：在攻击接口，身体手另行动；指示同一输入入口的空间位置，不裁定灵魂本体身份。
- In：承接DR22：断线末端落进Kris手边；Out：保护的线回成NEO断线。
- Colour：#070A14, #E7E9F2, #F04462, #75A58B；Motion：攻击线到达前手先横向带走他者；Effects：仅接触点窄glow、低强scanline；冲突段可路线触发glitch，不能遮心/手/选项。
- 复用：film/tui_pv_world_execute_20260926/continuity_full_v2/kit.py: transparent her_layer/chrome separation (design reuse)；film/tui_pv_world_execute_20260926/tuikit.py: font/scale_alpha/post。保留/替换：KEEP分层/读区；ADAPT pane/载体；REPLACE原DSH/模型视觉；REMOVE本片舞者。
- 新代码：dr_ui.control_pane, dr_ui.kris_study, dr_layers.world_body, s_dr_normal.shot_dr23（此处是实现计划，并非已经实现）。
- 技术：PIL/RGBA；直接复用font；旧monkey patch为零；section计划路径 film/deltarune/s_dr_normal.py。HTML不必需；原创透明角色/布景预渲染可选。
- PoC：无；not yet rendered。
- Asset：Kris原创轮廓与该镜几何场景；study可程序化；生产美术与游戏画面核对待完成。
- 待问/限制：不同章节交叉，不声称发生于同场战斗。
- Still QA：[1591, 1597, 1637, 1682]；关键事件：[]。

### DR24 — 落空的自由

- 范围：1683–1774 exclusive；70.125000–73.916667s。
- 音乐：仍受困的模型；line IDs [31, 32]。详细word/frame锚点保存在JSON，不复制歌词。
- Chapter/Route：2 / normal；证据 E06 E07。
- 叙述目的：解绑与可行动不是同一个变量。
- Player：可帮助、选择，不能替角色决定所有回应；Kris：有身体/偏好，选择与表达可能不同；他者：可拒绝或主动合作；Story：菜单提供有限行动与已设结果。
- Camera/Layout：full；世界占满24,56,1164,604；Kris必须在世界中有锚点；控制框可退到边缘，底带固定。
- Foreground：NEO轮廓小幅坠落；Kris接住视线非身体。用途：把主体动作/受输入的对象放在第一阅读层。
- Background：DarkWorld地面，断线在上。用途：提供该镜空间边界与关系，避免无意义装饰。
- UI：控制menu仍在边缘，不假装关闭世界。用途：显现可选行动、输入归属与当前限制。
- Text：无；无。
- Character：Kris；原创程序化轮廓study；最终美术未验收。
- SOUL：停在已按位置，Kris胸口示意不叠第二心；指示同一输入入口的空间位置，不裁定灵魂本体身份。
- In：承接DR23：保护的线回成NEO断线；Out：断线重组成键盘线。
- Colour：#070A14, #E7E9F2, #F04462, #75A58B；Motion：坠落12帧、后停留；无随机碎片；Effects：仅接触点窄glow、低强scanline；冲突段可路线触发glitch，不能遮心/手/选项。
- 复用：film/tui_pv_world_execute_20260926/continuity_full_v2/v2.py: FULL_ART slide staging (design reuse)；film/tui_pv_world_execute_20260926/tuikit.py: post。保留/替换：KEEP分层/读区；ADAPT pane/载体；REPLACE原DSH/模型视觉；REMOVE本片舞者。
- 新代码：dr_layers.full_world, dr_timeline.integer_slide, s_dr_normal.shot_dr24（此处是实现计划，并非已经实现）。
- 技术：PIL/RGBA；直接复用font；旧monkey patch为零；section计划路径 film/deltarune/s_dr_normal.py。HTML不必需；原创透明角色/布景预渲染可选。
- PoC：无；not yet rendered。
- Asset：Kris原创轮廓与该镜几何场景；study可程序化；生产美术与游戏画面核对待完成。
- 待问/限制：不是角色死亡/虚无的断言。
- Still QA：[1683, 1689, 1728, 1773]；关键事件：[]。

### DR25 — 供给的能力

- 范围：1774–1865 exclusive；73.916667–77.708333s。
- 音乐：给予营养的功能；line IDs [33, 34]。详细word/frame锚点保存在JSON，不复制歌词。
- Chapter/Route：4 / normal；证据 E21。
- 叙述目的：供给词被映射为有个性的能力。
- Player：可帮助、选择，不能替角色决定所有回应；Kris：有身体/偏好，选择与表达可能不同；他者：可拒绝或主动合作；Story：菜单提供有限行动与已设结果。
- Camera/Layout：split；固定1280×720；左主体24,56,384,604，右世界404,56,1164,604；上框/底带不随镜头变换。
- Foreground：Kris奏乐手与遮眼头。用途：把主体动作/受输入的对象放在第一阅读层。
- Background：原创organ键格，音波进入右世界。用途：提供该镜空间边界与关系，避免无意义装饰。
- UI：输入格很小、可退。用途：显现可选行动、输入归属与当前限制。
- Text：无；无。
- Character：Kris；原创程序化轮廓study；最终美术未验收。
- SOUL：稳定留在Kris层；指示同一输入入口的空间位置，不裁定灵魂本体身份。
- In：承接DR24：断线重组成键盘线；Out：波纹变成另一人的返向光。
- Colour：#070A14, #E7E9F2, #F04462, #75A58B；Motion：手指按两键、身体不消失于谱线；Effects：仅接触点窄glow、低强scanline；冲突段可路线触发glitch，不能遮心/手/选项。
- 复用：film/tui_pv_world_execute_20260926/continuity_full_v2/kit.py: transparent her_layer/chrome separation (design reuse)；film/tui_pv_world_execute_20260926/tuikit.py: font/scale_alpha/post。保留/替换：KEEP分层/读区；ADAPT pane/载体；REPLACE原DSH/模型视觉；REMOVE本片舞者。
- 新代码：dr_ui.control_pane, dr_ui.kris_study, dr_layers.world_body, s_dr_care.shot_dr25（此处是实现计划，并非已经实现）。
- 技术：PIL/RGBA；直接复用font；旧monkey patch为零；section计划路径 film/deltarune/s_dr_care.py。HTML不必需；原创透明角色/布景预渲染可选。
- PoC：无；not yet rendered。
- Asset：Kris原创轮廓与该镜几何场景；study可程序化；生产美术与游戏画面核对待完成。
- 待问/限制：不逐字复制蔬果素材，不虚构喂食情节。
- Still QA：[1774, 1780, 1819, 1864]；关键事件：[]。

### DR26 — 给予不等于讨好

- 范围：1865–1951 exclusive；77.708333–81.291667s。
- 音乐：供给保护的功能；line IDs [35, 36, 37]。详细word/frame锚点保存在JSON，不复制歌词。
- Chapter/Route：5 / normal；证据 E30。
- 叙述目的：自主行为也能关照友谊。
- Player：可帮助、选择，不能替角色决定所有回应；Kris：有身体/偏好，选择与表达可能不同；他者：可拒绝或主动合作；Story：菜单提供有限行动与已设结果。
- Camera/Layout：split；固定1280×720；左主体24,56,384,604，右世界404,56,1164,604；上框/底带不随镜头变换。
- Foreground：Kris与Susie小轮廓走在同一地面。用途：把主体动作/受输入的对象放在第一阅读层。
- Background：原创新街道/归家路径。用途：提供该镜空间边界与关系，避免无意义装饰。
- UI：拒绝格淡于世界路径。用途：显现可选行动、输入归属与当前限制。
- Text：无；无。
- Character：Kris；原创程序化轮廓study；最终美术未验收。
- SOUL：漂浮于一只轮廓balloon中，身体另走；指示同一输入入口的空间位置，不裁定灵魂本体身份。
- In：承接DR25：波纹变成另一人的返向光；Out：路径弧变成回波纹。
- Colour：#070A14, #E7E9F2, #F04462, #75A58B；Motion：balloon随风轻移，Kris步伐稳定；Effects：仅接触点窄glow、低强scanline；冲突段可路线触发glitch，不能遮心/手/选项。
- 复用：film/tui_pv_world_execute_20260926/continuity_full_v2/kit.py: transparent her_layer/chrome separation (design reuse)；film/tui_pv_world_execute_20260926/tuikit.py: font/scale_alpha/post。保留/替换：KEEP分层/读区；ADAPT pane/载体；REPLACE原DSH/模型视觉；REMOVE本片舞者。
- 新代码：dr_ui.control_pane, dr_ui.kris_study, dr_layers.world_body, s_dr_care.shot_dr26（此处是实现计划，并非已经实现）。
- 技术：PIL/RGBA；直接复用font；旧monkey patch为零；section计划路径 film/deltarune/s_dr_care.py。HTML不必需；原创透明角色/布景预渲染可选。
- PoC：无；not yet rendered。
- Asset：Kris原创轮廓与该镜几何场景；study可程序化；生产美术与游戏画面核对待完成。
- 待问/限制：属于normal条件分支，不放在weird lake同一时间。
- Still QA：[1865, 1871, 1908, 1950]；关键事件：[]。

### DR27 — 角色的回应

- 范围：1951–2043 exclusive；81.291667–85.125000s。
- 音乐：让他人快乐的功能；line IDs [37, 38]。详细word/frame锚点保存在JSON，不复制歌词。
- Chapter/Route：1 / 5 / normal / thematic crosscut；证据 E03 E30。
- 叙述目的：别人可以回应Player也可以回应Kris。
- Player：可帮助、选择，不能替角色决定所有回应；Kris：有身体/偏好，选择与表达可能不同；他者：可拒绝或主动合作；Story：菜单提供有限行动与已设结果。
- Camera/Layout：split；固定1280×720；左主体24,56,384,604，右世界404,56,1164,604；上框/底带不随镜头变换。
- Foreground：Kris左、Susie回头的小动作。用途：把主体动作/受输入的对象放在第一阅读层。
- Background：温灰地面替代恐怖氛围。用途：提供该镜空间边界与关系，避免无意义装饰。
- UI：可用选项不持续滚动。用途：显现可选行动、输入归属与当前限制。
- Text：无；无。
- Character：Kris；原创程序化轮廓study；最终美术未验收。
- SOUL：低亮但不降到看不见；指示同一输入入口的空间位置，不裁定灵魂本体身份。
- In：承接DR26：路径弧变成回波纹；Out：回波进入SAVE名字框。
- Colour：#070A14, #E7E9F2, #F04462, #75A58B；Motion：回波从他者到Kris手，主体先回应再UI；Effects：仅接触点窄glow、低强scanline；冲突段可路线触发glitch，不能遮心/手/选项。
- 复用：film/tui_pv_world_execute_20260926/continuity_full_v2/kit.py: transparent her_layer/chrome separation (design reuse)；film/tui_pv_world_execute_20260926/tuikit.py: font/scale_alpha/post。保留/替换：KEEP分层/读区；ADAPT pane/载体；REPLACE原DSH/模型视觉；REMOVE本片舞者。
- 新代码：dr_ui.control_pane, dr_ui.kris_study, dr_layers.world_body, s_dr_care.shot_dr27（此处是实现计划，并非已经实现）。
- 技术：PIL/RGBA；直接复用font；旧monkey patch为零；section计划路径 film/deltarune/s_dr_care.py。HTML不必需；原创透明角色/布景预渲染可选。
- PoC：无；not yet rendered。
- Asset：Kris原创轮廓与该镜几何场景；study可程序化；生产美术与游戏画面核对待完成。
- 待问/限制：不编写新游戏对白或love confession。
- Still QA：[1951, 1957, 1997, 2042]；关键事件：[]。

### DR28 — 存在不靠所有权

- 范围：2043–2125 exclusive；85.125000–88.541667s。
- 音乐：唯一存在与证明；line IDs [39, 40, 41]。详细word/frame锚点保存在JSON，不复制歌词。
- Chapter/Route：1 / normal / author metaphor；证据 E02。
- 叙述目的：creator和角色不能互相吞没。
- Player：可帮助、选择，不能替角色决定所有回应；Kris：有身体/偏好，选择与表达可能不同；他者：可拒绝或主动合作；Story：菜单提供有限行动与已设结果。
- Camera/Layout：close；右世界占主要面积；左仍留Kris胸/手轮廓；选择框最小字高24px；心不被glow盖住。
- Foreground：Kris轮廓与两张name卡。用途：把主体动作/受输入的对象放在第一阅读层。
- Background：卡下保留身体影子。用途：提供该镜空间边界与关系，避免无意义装饰。
- UI：SAVE卡上下两层。用途：显现可选行动、输入归属与当前限制。
- Text：KRIS / CREATOR（作者标记）；短菜单/名称或明确作者标记，非歌词/新增角色对白。
- Character：Kris；原创程序化轮廓study；最终美术未验收。
- SOUL：在保存位置，不能把名字变成脸；指示同一输入入口的空间位置，不裁定灵魂本体身份。
- In：承接DR27：回波进入SAVE名字框；Out：name卡白边变衣服色带。
- Colour：#070A14, #E7E9F2, #F04462, #75A58B；Motion：两name层接近但保持2px缝；Effects：仅接触点窄glow、低强scanline；冲突段可路线触发glitch，不能遮心/手/选项。
- 复用：film/tui_pv_world_execute_20260926/tuikit.py: font/post；film/pv_dsh_frontend_20260927/dsh_her.py: LEAD readability principle (design reuse)。保留/替换：KEEP分层/读区；ADAPT pane/载体；REPLACE原DSH/模型视觉；REMOVE本片舞者。
- 新代码：dr_ui.choice_box, dr_layers.hand_detail, dr_timeline.choice_events, s_dr_care.shot_dr28（此处是实现计划，并非已经实现）。
- 技术：PIL/RGBA；直接复用font；旧monkey patch为零；section计划路径 film/deltarune/s_dr_care.py。HTML不必需；原创透明角色/布景预渲染可选。
- PoC：无；not yet rendered。
- Asset：Kris原创轮廓与该镜几何场景；study可程序化；生产美术与游戏画面核对待完成。
- 待问/限制：Player不是本作创世神的canon结论。
- Still QA：[2043, 2049, 2084, 2124]；关键事件：[]。

### DR29 — 同一个人

- 范围：2125–2205 exclusive；88.541667–91.875000s。
- 音乐：身份属性切换；line IDs [41, 42]。详细word/frame锚点保存在JSON，不复制歌词。
- Chapter/Route：1 / 2 / normal / author metaphor；证据 E01 E05。
- 叙述目的：不让歌曲身份词抹掉Kris。
- Player：可帮助、选择，不能替角色决定所有回应；Kris：有身体/偏好，选择与表达可能不同；他者：可拒绝或主动合作；Story：菜单提供有限行动与已设结果。
- Camera/Layout：split；固定1280×720；左主体24,56,384,604，右世界404,56,1164,604；上框/底带不随镜头变换。
- Foreground：Kris同一遮眼/手，衣色域变化。用途：把主体动作/受输入的对象放在第一阅读层。
- Background：Light暖灰与Dark靛蓝分界。用途：提供该镜空间边界与关系，避免无意义装饰。
- UI：输入没有gender selector。用途：显现可选行动、输入归属与当前限制。
- Text：无；无。
- Character：Kris；原创程序化轮廓study；最终美术未验收。
- SOUL：留同一身体锚点；指示同一输入入口的空间位置，不裁定灵魂本体身份。
- In：承接DR28：name卡白边变衣服色带；Out：窗光从亮切暗。
- Colour：#070A14, #E7E9F2, #F04462, #75A58B；Motion：只切环境与衣色，不切身体身份/性别；Effects：仅接触点窄glow、低强scanline；冲突段可路线触发glitch，不能遮心/手/选项。
- 复用：film/tui_pv_world_execute_20260926/continuity_full_v2/kit.py: transparent her_layer/chrome separation (design reuse)；film/tui_pv_world_execute_20260926/tuikit.py: font/scale_alpha/post。保留/替换：KEEP分层/读区；ADAPT pane/载体；REPLACE原DSH/模型视觉；REMOVE本片舞者。
- 新代码：dr_ui.control_pane, dr_ui.kris_study, dr_layers.world_body, s_dr_care.shot_dr29（此处是实现计划，并非已经实现）。
- 技术：PIL/RGBA；直接复用font；旧monkey patch为零；section计划路径 film/deltarune/s_dr_care.py。HTML不必需；原创透明角色/布景预渲染可选。
- PoC：无；not yet rendered。
- Asset：Kris原创轮廓与该镜几何场景；study可程序化；生产美术与游戏画面核对待完成。
- 待问/限制：Light/Dark具体角色美术待原创新设计。
- Still QA：[2125, 2131, 2165, 2204]；关键事件：[]。

### DR30 — 日夜之外的动作

- 范围：2205–2295 exclusive；91.875000–95.625000s。
- 音乐：一天时段与不同活动；line IDs [43, 44]。详细word/frame锚点保存在JSON，不复制歌词。
- Chapter/Route：2 / 5 / normal / thematic crosscut；证据 E05 E29。
- 叙述目的：Kris在输入间隙仍有动作。
- Player：可帮助、选择，不能替角色决定所有回应；Kris：有身体/偏好，选择与表达可能不同；他者：可拒绝或主动合作；Story：菜单提供有限行动与已设结果。
- Camera/Layout：split；固定1280×720；左主体24,56,384,604，右世界404,56,1164,604；上框/底带不随镜头变换。
- Foreground：Kris手靠窗，另一手暂藏SOUL。用途：把主体动作/受输入的对象放在第一阅读层。
- Background：夜窗/日窗只作时间背景。用途：提供该镜空间边界与关系，避免无意义装饰。
- UI：输入框暗下，世界继续。用途：显现可选行动、输入归属与当前限制。
- Text：无；无。
- Character：Kris；原创程序化轮廓study；最终美术未验收。
- SOUL：局部被布边遮，但不画彻底断电死亡；指示同一输入入口的空间位置，不裁定灵魂本体身份。
- In：承接DR29：窗光从亮切暗；Out：窗外框变TV舞台框。
- Colour：#070A14, #E7E9F2, #F04462, #75A58B；Motion：手关窗6帧，心漂移受容器限制；Effects：仅接触点窄glow、低强scanline；冲突段可路线触发glitch，不能遮心/手/选项。
- 复用：film/tui_pv_world_execute_20260926/continuity_full_v2/kit.py: transparent her_layer/chrome separation (design reuse)；film/tui_pv_world_execute_20260926/tuikit.py: font/scale_alpha/post。保留/替换：KEEP分层/读区；ADAPT pane/载体；REPLACE原DSH/模型视觉；REMOVE本片舞者。
- 新代码：dr_ui.control_pane, dr_ui.kris_study, dr_layers.world_body, s_dr_care.shot_dr30（此处是实现计划，并非已经实现）。
- 技术：PIL/RGBA；直接复用font；旧monkey patch为零；section计划路径 film/deltarune/s_dr_care.py。HTML不必需；原创透明角色/布景预渲染可选。
- PoC：无；not yet rendered。
- Asset：Kris原创轮廓与该镜几何场景；study可程序化；生产美术与游戏画面核对待完成。
- 待问/限制：不要给离体时长具体生理解释。
- Still QA：[2205, 2211, 2250, 2294]；关键事件：[]。

### DR31 — 舞台角色套住输入

- 范围：2295–2382 exclusive；95.625000–99.250000s。
- 音乐：角色切换的关系；line IDs [45, 46]。详细word/frame锚点保存在JSON，不复制歌词。
- Chapter/Route：3 / common；证据 E13。
- 叙述目的：Player进入Kris、Kris又被节目定位。
- Player：在Kris与小游戏之间切换控制对象；Kris：可抵抗输入、保护他人、退出某控制链；他者：Susie可介入；舞台规则也约束角色；Story：越界须经过游戏已有障碍与触发器。
- Camera/Layout：nested；右侧世界内再置TV内框；左侧Kris维持同尺寸；跨界对象不缩放chrome。
- Foreground：Kris留左，内TV的角色格在右。用途：把主体动作/受输入的对象放在第一阅读层。
- Background：节目舞台只有框/聚光，无Tenna整幅图。用途：提供该镜空间边界与关系，避免无意义装饰。
- UI：内层controller状态。用途：显现可选行动、输入归属与当前限制。
- Text：无；无。
- Character：Kris；原创程序化轮廓study；最终美术未验收。
- SOUL：输入轨迹依次经过三个框；指示同一输入入口的空间位置，不裁定灵魂本体身份。
- In：承接DR30：窗外框变TV舞台框；Out：舞台轨迹变奏乐键格。
- Colour：#070A14, #E7E9F2, #F04462, #75A58B；Motion：同一move分三层显示，不三心分裂；Effects：仅接触点窄glow、低强scanline；冲突段可路线触发glitch，不能遮心/手/选项。
- 复用：film/tui_pv_world_execute_20260926/continuity_full_v2/cuts.py: Frame/content/over concept；film/tui_pv_world_execute_20260926/continuity_full_v2/kit.py: carrier positioning (design reuse)。保留/替换：KEEP分层/读区；ADAPT pane/载体；REPLACE原DSH/模型视觉；REMOVE本片舞者。
- 新代码：dr_layers.inner_game, dr_layers.hero_carrier, dr_timeline.control_target, s_dr_nested.shot_dr31（此处是实现计划，并非已经实现）。
- 技术：PIL/RGBA；直接复用font；旧monkey patch为零；section计划路径 film/deltarune/s_dr_nested.py。HTML不必需；原创透明角色/布景预渲染可选。
- PoC：无；not yet rendered。
- Asset：Kris原创轮廓与该镜几何场景；study可程序化；生产美术与游戏画面核对待完成。
- 待问/限制：不保留原S/M直译，更不重写角色性别。
- Still QA：[2295, 2301, 2338, 2381]；关键事件：[]。

### DR32 — 能力与输入共存

- 范围：2382–2485 exclusive；99.250000–103.541667s。
- 音乐：进入感应与专注；line IDs [47, 48, 49]。详细word/frame锚点保存在JSON，不复制歌词。
- Chapter/Route：4 / normal；证据 E21。
- 叙述目的：角色不是无输入就无能力的空壳。
- Player：可帮助、选择，不能替角色决定所有回应；Kris：有身体/偏好，选择与表达可能不同；他者：可拒绝或主动合作；Story：菜单提供有限行动与已设结果。
- Camera/Layout：split；固定1280×720；左主体24,56,384,604，右世界404,56,1164,604；上框/底带不随镜头变换。
- Foreground：Kris手按organ，肩姿与input不同步。用途：把主体动作/受输入的对象放在第一阅读层。
- Background：只两道音波，背景空净。用途：提供该镜空间边界与关系，避免无意义装饰。
- UI：choice框退后，不写AI参数。用途：显现可选行动、输入归属与当前限制。
- Text：无；无。
- Character：Kris；原创程序化轮廓study；最终美术未验收。
- SOUL：胸前亮、手主动动作；指示同一输入入口的空间位置，不裁定灵魂本体身份。
- In：承接DR31：舞台轨迹变奏乐键格；Out：两个节奏逐渐同相。
- Colour：#070A14, #E7E9F2, #F04462, #75A58B；Motion：每beat肩动1px、手独立按键；Effects：仅接触点窄glow、低强scanline；冲突段可路线触发glitch，不能遮心/手/选项。
- 复用：film/tui_pv_world_execute_20260926/continuity_full_v2/kit.py: transparent her_layer/chrome separation (design reuse)；film/tui_pv_world_execute_20260926/tuikit.py: font/scale_alpha/post。保留/替换：KEEP分层/读区；ADAPT pane/载体；REPLACE原DSH/模型视觉；REMOVE本片舞者。
- 新代码：dr_ui.control_pane, dr_ui.kris_study, dr_layers.world_body, s_dr_care.shot_dr32（此处是实现计划，并非已经实现）。
- 技术：PIL/RGBA；直接复用font；旧monkey patch为零；section计划路径 film/deltarune/s_dr_care.py。HTML不必需；原创透明角色/布景预渲染可选。
- PoC：无；not yet rendered。
- Asset：Kris原创轮廓与该镜几何场景；study可程序化；生产美术与游戏画面核对待完成。
- 待问/限制：不是声称Ch4全部演奏无Player作用。
- Still QA：[2382, 2388, 2433, 2484]；关键事件：[]。

### DR33 — 共同振动

- 范围：2485–2571 exclusive；103.541667–107.125000s。
- 音乐：感应与共振；line IDs [49, 50]。详细word/frame锚点保存在JSON，不复制歌词。
- Chapter/Route：1 / 4 / normal / thematic crosscut；证据 E03 E21。
- 叙述目的：合作可以发生，不需要消灭一方意志。
- Player：可帮助、选择，不能替角色决定所有回应；Kris：有身体/偏好，选择与表达可能不同；他者：可拒绝或主动合作；Story：菜单提供有限行动与已设结果。
- Camera/Layout：split；固定1280×720；左主体24,56,384,604，右世界404,56,1164,604；上框/底带不随镜头变换。
- Foreground：Kris手与伙伴轨迹。用途：把主体动作/受输入的对象放在第一阅读层。
- Background：右世界有可走的地面。用途：提供该镜空间边界与关系，避免无意义装饰。
- UI：菜单保留两种不同选项。用途：显现可选行动、输入归属与当前限制。
- Text：无；无。
- Character：Kris；原创程序化轮廓study；最终美术未验收。
- SOUL：身体心和menu选择只用接触闪示意；指示同一输入入口的空间位置，不裁定灵魂本体身份。
- In：承接DR32：两个节奏逐渐同相；Out：连线包围身体成为完整轮廓。
- Colour：#070A14, #E7E9F2, #F04462, #75A58B；Motion：input波落时动作波相接，hold6帧；Effects：仅接触点窄glow、低强scanline；冲突段可路线触发glitch，不能遮心/手/选项。
- 复用：film/tui_pv_world_execute_20260926/continuity_full_v2/kit.py: transparent her_layer/chrome separation (design reuse)；film/tui_pv_world_execute_20260926/tuikit.py: font/scale_alpha/post。保留/替换：KEEP分层/读区；ADAPT pane/载体；REPLACE原DSH/模型视觉；REMOVE本片舞者。
- 新代码：dr_ui.control_pane, dr_ui.kris_study, dr_layers.world_body, s_dr_normal.shot_dr33（此处是实现计划，并非已经实现）。
- 技术：PIL/RGBA；直接复用font；旧monkey patch为零；section计划路径 film/deltarune/s_dr_normal.py。HTML不必需；原创透明角色/布景预渲染可选。
- PoC：无；not yet rendered。
- Asset：Kris原创轮廓与该镜几何场景；study可程序化；生产美术与游戏画面核对待完成。
- 待问/限制：保留作者比喻标记于metadata。
- Still QA：[2485, 2491, 2528, 2570]；关键事件：[]。

### DR34 — 完整不是拥有

- 范围：2571–2650 exclusive；107.125000–110.416667s。
- 音乐：完成的感觉；line IDs [51, 52, 53]。详细word/frame锚点保存在JSON，不复制歌词。
- Chapter/Route：1 / 4 / normal / thematic crosscut；证据 E03 E04 E21。
- 叙述目的：在分离前给连接真实情感重量。
- Player：可帮助、选择，不能替角色决定所有回应；Kris：有身体/偏好，选择与表达可能不同；他者：可拒绝或主动合作；Story：菜单提供有限行动与已设结果。
- Camera/Layout：full；世界占满24,56,1164,604；Kris必须在世界中有锚点；控制框可退到边缘，底带固定。
- Foreground：Kris完整轮廓站右世界近中心。用途：把主体动作/受输入的对象放在第一阅读层。
- Background：暖细光与空地面，无人数统计。用途：提供该镜空间边界与关系，避免无意义装饰。
- UI：menu存在但弱亮。用途：显现可选行动、输入归属与当前限制。
- Text：无；无。
- Character：Kris；原创程序化轮廓study；最终美术未验收。
- SOUL：胸口亮，接触边缘不放大满屏心；指示同一输入入口的空间位置，不裁定灵魂本体身份。
- In：承接DR33：连线包围身体成为完整轮廓；Out：进入分离手势，场景暖色退。
- Colour：#070A14, #E7E9F2, #F04462, #75A58B；Motion：身体停一拍，最后6帧手靠胸；Effects：仅接触点窄glow、低强scanline；冲突段可路线触发glitch，不能遮心/手/选项。
- 复用：film/tui_pv_world_execute_20260926/continuity_full_v2/v2.py: FULL_ART slide staging (design reuse)；film/tui_pv_world_execute_20260926/tuikit.py: post。保留/替换：KEEP分层/读区；ADAPT pane/载体；REPLACE原DSH/模型视觉；REMOVE本片舞者。
- 新代码：dr_layers.full_world, dr_timeline.integer_slide, s_dr_normal.shot_dr34（此处是实现计划，并非已经实现）。
- 技术：PIL/RGBA；直接复用font；旧monkey patch为零；section计划路径 film/deltarune/s_dr_normal.py。HTML不必需；原创透明角色/布景预渲染可选。
- PoC：无；not yet rendered。
- Asset：Kris原创轮廓与该镜几何场景；study可程序化；生产美术与游戏画面核对待完成。
- 待问/限制：此处非宣称游戏特定chapter终局。
- Still QA：[2571, 2577, 2610, 2649]；关键事件：['K02']。

### DR35 — 离开身体

- 范围：2650–2693 exclusive；110.416667–112.208333s。
- 音乐：第一次离开；line IDs [53, 54]。详细word/frame锚点保存在JSON，不复制歌词。
- Chapter/Route：1 / ending；证据 E04。
- 叙述目的：失去control并不让Kris消失。
- Player：仍可移动SOUL，暂不能指挥Kris身体；Kris：身体继续自主行动，动机不替其裁定；他者：私话/世界动作不由当前输入直接操纵；Story：scene/空间边界仍规定SOUL可达范围。
- Camera/Layout：close；右世界占主要面积；左仍留Kris胸/手轮廓；选择框最小字高24px；心不被glow盖住。
- Foreground：Kris的手抽出红心。用途：把主体动作/受输入的对象放在第一阅读层。
- Background：左pane仍有身体轮廓。用途：提供该镜空间边界与关系，避免无意义装饰。
- UI：输入框与身体间连线断一段。用途：显现可选行动、输入归属与当前限制。
- Text：无；无。
- Character：Kris；原创程序化轮廓study；最终美术未验收。
- SOUL：从胸口到手外，手比selector先运动；指示同一输入入口的空间位置，不裁定灵魂本体身份。
- In：承接DR34：进入分离手势，场景暖色退；Out：输入框停止响应身体。
- Colour：#070A14, #E7E9F2, #F04462, #75A58B；Motion：2650–2655拉出；2656–2661离胸；之后hold；Effects：仅接触点窄glow、低强scanline；冲突段可路线触发glitch，不能遮心/手/选项。
- 复用：film/tui_pv_world_execute_20260926/tuikit.py: font/post；film/pv_dsh_frontend_20260927/dsh_her.py: LEAD readability principle (design reuse)。保留/替换：KEEP分层/读区；ADAPT pane/载体；REPLACE原DSH/模型视觉；REMOVE本片舞者。
- 新代码：dr_ui.choice_box, dr_layers.hand_detail, dr_timeline.choice_events, s_dr_separation.shot_dr35（此处是实现计划，并非已经实现）。
- 技术：PIL/RGBA；直接复用font；旧monkey patch为零；section计划路径 film/deltarune/s_dr_separation.py。HTML不必需；原创透明角色/布景预渲染可选。
- PoC：无；not yet rendered。
- Asset：Kris原创轮廓与该镜几何场景；study可程序化；生产美术与游戏画面核对待完成。
- 待问/限制：不是宣布Kris认识现实Player。
- Still QA：[2650, 2656, 2671, 2692]；关键事件：['K02']。

### DR36 — 输入仍在

- 范围：2693–2718 exclusive；112.208333–113.250000s。
- 音乐：再次离开；line IDs [54]。详细word/frame锚点保存在JSON，不复制歌词。
- Chapter/Route：1 / ending / author staging；证据 E04。
- 叙述目的：观众仍能操作心的位置却不能身体。
- Player：仍可移动SOUL，暂不能指挥Kris身体；Kris：身体继续自主行动，动机不替其裁定；他者：私话/世界动作不由当前输入直接操纵；Story：scene/空间边界仍规定SOUL可达范围。
- Camera/Layout：split；固定1280×720；左主体24,56,384,604，右世界404,56,1164,604；上框/底带不随镜头变换。
- Foreground：Kris保持右向朝向。用途：把主体动作/受输入的对象放在第一阅读层。
- Background：左主体pane轮廓/右心的空间不同。用途：提供该镜空间边界与关系，避免无意义装饰。
- UI：小方向input仍亮，身体行不亮。用途：显现可选行动、输入归属与当前限制。
- Text：无；无。
- Character：Kris；原创程序化轮廓study；最终美术未验收。
- SOUL：右移一步，Kris不跟随；指示同一输入入口的空间位置，不裁定灵魂本体身份。
- In：承接DR35：输入框停止响应身体；Out：身体和心的两个区间分开。
- Colour：#070A14, #E7E9F2, #F04462, #75A58B；Motion：方向格闪一下只移动心；Effects：仅接触点窄glow、低强scanline；冲突段可路线触发glitch，不能遮心/手/选项。
- 复用：film/tui_pv_world_execute_20260926/continuity_full_v2/kit.py: transparent her_layer/chrome separation (design reuse)；film/tui_pv_world_execute_20260926/tuikit.py: font/scale_alpha/post。保留/替换：KEEP分层/读区；ADAPT pane/载体；REPLACE原DSH/模型视觉；REMOVE本片舞者。
- 新代码：dr_ui.control_pane, dr_ui.kris_study, dr_layers.world_body, s_dr_separation.shot_dr36（此处是实现计划，并非已经实现）。
- 技术：PIL/RGBA；直接复用font；旧monkey patch为零；section计划路径 film/deltarune/s_dr_separation.py。HTML不必需；原创透明角色/布景预渲染可选。
- PoC：无；not yet rendered。
- Asset：Kris原创轮廓与该镜几何场景；study可程序化；生产美术与游戏画面核对待完成。
- 待问/限制：UI拆除是作者结构，不是游戏实际CSS。
- Still QA：[2693, 2699, 2705, 2717]；关键事件：['K02']。

### DR37 — 世界不跟输入退场

- 范围：2718–2734 exclusive；113.250000–113.916667s。
- 音乐：第三次离开；line IDs [55]。详细word/frame锚点保存在JSON，不复制歌词。
- Chapter/Route：1 / ending / author staging；证据 E04。
- 叙述目的：连接断裂不是整个角色世界结束。
- Player：仍可移动SOUL，暂不能指挥Kris身体；Kris：身体继续自主行动，动机不替其裁定；他者：私话/世界动作不由当前输入直接操纵；Story：scene/空间边界仍规定SOUL可达范围。
- Camera/Layout：split；固定1280×720；左主体24,56,384,604，右世界404,56,1164,604；上框/底带不随镜头变换。
- Foreground：Kris肩和手仍有动作。用途：把主体动作/受输入的对象放在第一阅读层。
- Background：世界地面留下，输入pane边线收回。用途：提供该镜空间边界与关系，避免无意义装饰。
- UI：退一个框角，底带保留。用途：显现可选行动、输入归属与当前限制。
- Text：无；无。
- Character：Kris；原创程序化轮廓study；最终美术未验收。
- SOUL：悬于右边，不能变箭头样另一心；指示同一输入入口的空间位置，不裁定灵魂本体身份。
- In：承接DR36：身体和心的两个区间分开；Out：心进入实体容器轮廓。
- Colour：#070A14, #E7E9F2, #F04462, #75A58B；Motion：框角8帧退去，身体保持；Effects：仅接触点窄glow、低强scanline；冲突段可路线触发glitch，不能遮心/手/选项。
- 复用：film/tui_pv_world_execute_20260926/continuity_full_v2/kit.py: transparent her_layer/chrome separation (design reuse)；film/tui_pv_world_execute_20260926/tuikit.py: font/scale_alpha/post。保留/替换：KEEP分层/读区；ADAPT pane/载体；REPLACE原DSH/模型视觉；REMOVE本片舞者。
- 新代码：dr_ui.control_pane, dr_ui.kris_study, dr_layers.world_body, s_dr_separation.shot_dr37（此处是实现计划，并非已经实现）。
- 技术：PIL/RGBA；直接复用font；旧monkey patch为零；section计划路径 film/deltarune/s_dr_separation.py。HTML不必需；原创透明角色/布景预渲染可选。
- PoC：无；not yet rendered。
- Asset：Kris原创轮廓与该镜几何场景；study可程序化；生产美术与游戏画面核对待完成。
- 待问/限制：不能把黑场叫Kris死亡。
- Still QA：[2718, 2724, 2726, 2733]；关键事件：[]。

### DR38 — 保护变容器

- 范围：2734–2754 exclusive；113.916667–114.750000s。
- 音乐：第四次离开；line IDs [55, 56]。详细word/frame锚点保存在JSON，不复制歌词。
- Chapter/Route：1 / ending；证据 E04。
- 叙述目的：回扣开头白框的双义。
- Player：仍可移动SOUL，暂不能指挥Kris身体；Kris：身体继续自主行动，动机不替其裁定；他者：私话/世界动作不由当前输入直接操纵；Story：scene/空间边界仍规定SOUL可达范围。
- Camera/Layout：close；右世界占主要面积；左仍留Kris胸/手轮廓；选择框最小字高24px；心不被glow盖住。
- Foreground：Kris轮廓在cage外。用途：把主体动作/受输入的对象放在第一阅读层。
- Background：与02相同四角变cage格线。用途：提供该镜空间边界与关系，避免无意义装饰。
- UI：menu框让位给物理cage。用途：显现可选行动、输入归属与当前限制。
- Text：无；无。
- Character：Kris；原创程序化轮廓study；最终美术未验收。
- SOUL：在cage内可左右移不穿边；指示同一输入入口的空间位置，不裁定灵魂本体身份。
- In：承接DR37：心进入实体容器轮廓；Out：Kris手离开cage，身体向外。
- Colour：#070A14, #E7E9F2, #F04462, #75A58B；Motion：十帧心移向边、边阻住；Effects：仅接触点窄glow、低强scanline；冲突段可路线触发glitch，不能遮心/手/选项。
- 复用：film/tui_pv_world_execute_20260926/tuikit.py: font/post；film/pv_dsh_frontend_20260927/dsh_her.py: LEAD readability principle (design reuse)。保留/替换：KEEP分层/读区；ADAPT pane/载体；REPLACE原DSH/模型视觉；REMOVE本片舞者。
- 新代码：dr_ui.choice_box, dr_layers.hand_detail, dr_timeline.choice_events, s_dr_separation.shot_dr38（此处是实现计划，并非已经实现）。
- 技术：PIL/RGBA；直接复用font；旧monkey patch为零；section计划路径 film/deltarune/s_dr_separation.py。HTML不必需；原创透明角色/布景预渲染可选。
- PoC：无；not yet rendered。
- Asset：Kris原创轮廓与该镜几何场景；study可程序化；生产美术与游戏画面核对待完成。
- 待问/限制：原game birdcage形状以后原创新美术。
- Still QA：[2734, 2740, 2744, 2753]；关键事件：[]。

### DR39 — 身体独自行动

- 范围：2754–2784 exclusive；114.750000–116.000000s。
- 音乐：第五次离开；line IDs [56, 57]。详细word/frame锚点保存在JSON，不复制歌词。
- Chapter/Route：1 / 2 / ending / thematic crosscut；证据 E04 E05。
- 叙述目的：离开输入不等于善良/邪恶判决。
- Player：仍可移动SOUL，暂不能指挥Kris身体；Kris：身体继续自主行动，动机不替其裁定；他者：私话/世界动作不由当前输入直接操纵；Story：scene/空间边界仍规定SOUL可达范围。
- Camera/Layout：full；世界占满24,56,1164,604；Kris必须在世界中有锚点；控制框可退到边缘，底带固定。
- Foreground：Kris向世界深处自主一步。用途：把主体动作/受输入的对象放在第一阅读层。
- Background：cage在小角落仍可见心。用途：提供该镜空间边界与关系，避免无意义装饰。
- UI：input只照角落。用途：显现可选行动、输入归属与当前限制。
- Text：无；无。
- Character：Kris；原创程序化轮廓study；最终美术未验收。
- SOUL：留容器，不随Kris走；指示同一输入入口的空间位置，不裁定灵魂本体身份。
- In：承接DR38：Kris手离开cage，身体向外；Out：房间门白线接到vent。
- Colour：#070A14, #E7E9F2, #F04462, #75A58B；Motion：Kris一步16帧；input脉冲只让心一像素动；Effects：仅接触点窄glow、低强scanline；冲突段可路线触发glitch，不能遮心/手/选项。
- 复用：film/tui_pv_world_execute_20260926/continuity_full_v2/v2.py: FULL_ART slide staging (design reuse)；film/tui_pv_world_execute_20260926/tuikit.py: post。保留/替换：KEEP分层/读区；ADAPT pane/载体；REPLACE原DSH/模型视觉；REMOVE本片舞者。
- 新代码：dr_layers.full_world, dr_timeline.integer_slide, s_dr_separation.shot_dr39（此处是实现计划，并非已经实现）。
- 技术：PIL/RGBA；直接复用font；旧monkey patch为零；section计划路径 film/deltarune/s_dr_separation.py。HTML不必需；原创透明角色/布景预渲染可选。
- PoC：无；not yet rendered。
- Asset：Kris原创轮廓与该镜几何场景；study可程序化；生产美术与游戏画面核对待完成。
- 待问/限制：不画邪恶笑或Knight身份暗示。
- Still QA：[2754, 2760, 2769, 2783]；关键事件：[]。

### DR40 — 隔离是空间问题

- 范围：2784–2838 exclusive；116.000000–118.250000s。
- 音乐：隔离的结果；line IDs [58, 59]。详细word/frame锚点保存在JSON，不复制歌词。
- Chapter/Route：4 / common / thematic crosscut；证据 E20 E23。
- 叙述目的：从完全断开转为可窥视有限空间。
- Player：仍可移动SOUL，暂不能指挥Kris身体；Kris：身体继续自主行动，动机不替其裁定；他者：私话/世界动作不由当前输入直接操纵；Story：scene/空间边界仍规定SOUL可达范围。
- Camera/Layout：split；固定1280×720；左主体24,56,384,604，右世界404,56,1164,604；上框/底带不随镜头变换。
- Foreground：Kris远处门内影子，SOUL在vent。用途：把主体动作/受输入的对象放在第一阅读层。
- Background：gift-room/vent三段原创线布局。用途：提供该镜空间边界与关系，避免无意义装饰。
- UI：input受vent通道裁切。用途：显现可选行动、输入归属与当前限制。
- Text：无；无。
- Character：Kris；原创程序化轮廓study；最终美术未验收。
- SOUL：沿L形通道走，到门内视线边缘；指示同一输入入口的空间位置，不裁定灵魂本体身份。
- In：承接DR39：房间门白线接到vent；Out：私话层慢亮。
- Colour：#070A14, #E7E9F2, #F04462, #75A58B；Motion：身体不重绘成当前心，心贴通道；Effects：仅接触点窄glow、低强scanline；冲突段可路线触发glitch，不能遮心/手/选项。
- 复用：film/tui_pv_world_execute_20260926/continuity_full_v2/kit.py: transparent her_layer/chrome separation (design reuse)；film/tui_pv_world_execute_20260926/tuikit.py: font/scale_alpha/post。保留/替换：KEEP分层/读区；ADAPT pane/载体；REPLACE原DSH/模型视觉；REMOVE本片舞者。
- 新代码：dr_ui.control_pane, dr_ui.kris_study, dr_layers.world_body, s_dr_separation.shot_dr40（此处是实现计划，并非已经实现）。
- 技术：PIL/RGBA；直接复用font；旧monkey patch为零；section计划路径 film/deltarune/s_dr_separation.py。HTML不必需；原创透明角色/布景预渲染可选。
- PoC：无；not yet rendered。
- Asset：Kris原创轮廓与该镜几何场景；study可程序化；生产美术与游戏画面核对待完成。
- 待问/限制：章1→章4是主题cut，不是一条连续房间。
- Still QA：[2784, 2790, 2811, 2837]；关键事件：[]。

### DR41 — 不是菜单制造的声音

- 范围：2838–2928 exclusive；118.250000–122.000000s。
- 音乐：旧片段与可抹去的痕迹；line IDs [59, 60]。详细word/frame锚点保存在JSON，不复制歌词。
- Chapter/Route：4 / weird / remembered report；证据 E23 E25。
- 叙述目的：Kris离开输入时也有关系/表达。
- Player：输入影响强但维持路线条件严格；Kris：被代行命令并保留局部抵抗/反冲；他者：Noelle拒绝/执行/察觉不同声音；Story：规定命令与锁定限制其他解法。
- Camera/Layout：split；固定1280×720；左主体24,56,384,604，右世界404,56,1164,604；上框/底带不随镜头变换。
- Foreground：Kris与Noelle门内影子面对面。用途：把主体动作/受输入的对象放在第一阅读层。
- Background：门外vent里红心；门内暖色残留。用途：提供该镜空间边界与关系，避免无意义装饰。
- UI：私话没有player对话按钮直到尾段。用途：显现可选行动、输入归属与当前限制。
- Text：VOICE / KRIS（作者回忆标记）；短菜单/名称或明确作者标记，非歌词/新增角色对白。
- Character：Kris；原创程序化轮廓study；最终美术未验收。
- SOUL：留vent，choice末尾出现靠近房内位置；指示同一输入入口的空间位置，不裁定灵魂本体身份。
- In：承接DR40：私话层慢亮；Out：choice框跨过vent边界。
- Colour：#070A14, #E7E9F2, #F04462, #C7E4EC；Motion：熟悉声波从Kris发出；红input波与其不同形；Effects：仅接触点窄glow、低强scanline；冲突段可路线触发glitch，不能遮心/手/选项。
- 复用：film/tui_pv_world_execute_20260926/continuity_full_v2/kit.py: transparent her_layer/chrome separation (design reuse)；film/tui_pv_world_execute_20260926/tuikit.py: font/scale_alpha/post。保留/替换：KEEP分层/读区；ADAPT pane/载体；REPLACE原DSH/模型视觉；REMOVE本片舞者。
- 新代码：dr_ui.control_pane, dr_ui.kris_study, dr_layers.world_body, s_dr_separation.shot_dr41（此处是实现计划，并非已经实现）。
- 技术：PIL/RGBA；直接复用font；旧monkey patch为零；section计划路径 film/deltarune/s_dr_separation.py。HTML不必需；原创透明角色/布景预渲染可选。
- PoC：无；not yet rendered。
- Asset：Kris原创轮廓与该镜几何场景；study可程序化；生产美术与游戏画面核对待完成。
- 待问/限制：道歉由Noelle回忆，画法标remembered，非证实镜头目击。
- Still QA：[2838, 2844, 2883, 2927]；关键事件：[]。

### DR42 — 菜单是一扇门

- 范围：2928–3014 exclusive；122.000000–125.583333s。
- 音乐：希望把连接取回；line IDs [61, 62, 63]。详细word/frame锚点保存在JSON，不复制歌词。
- Chapter/Route：4 / weird；证据 E24。
- 叙述目的：Player选择物理位置，重新占住输入接口。
- Player：输入影响强但维持路线条件严格；Kris：被代行命令并保留局部抵抗/反冲；他者：Noelle拒绝/执行/察觉不同声音；Story：规定命令与锁定限制其他解法。
- Camera/Layout：close；右世界占主要面积；左仍留Kris胸/手轮廓；选择框最小字高24px；心不被glow盖住。
- Foreground：Kris手/胸口在门内；Noelle保持另一侧。用途：把主体动作/受输入的对象放在第一阅读层。
- Background：vent与房间边界连续。用途：提供该镜空间边界与关系，避免无意义装饰。
- UI：Proceed在房内，拒绝位置留vent。用途：显现可选行动、输入归属与当前限制。
- Text：Proceed / ...（短选项grammar）；短菜单/名称或明确作者标记，非歌词/新增角色对白。
- Character：Kris；原创程序化轮廓study；最终美术未验收。
- SOUL：从vent跳choice位置再移动到Kris胸前；指示同一输入入口的空间位置，不裁定灵魂本体身份。
- In：承接DR41：choice框跨过vent边界；Out：连接重新形成但右世界暖色退。
- Colour：#070A14, #E7E9F2, #F04462, #C7E4EC；Motion：2928–2933迁移；2934–2941进入房间；2942–2947接触；之后重入；Effects：仅接触点窄glow、低强scanline；冲突段可路线触发glitch，不能遮心/手/选项。
- 复用：film/tui_pv_world_execute_20260926/tuikit.py: font/post；film/pv_dsh_frontend_20260927/dsh_her.py: LEAD readability principle (design reuse)。保留/替换：KEEP分层/读区；ADAPT pane/载体；REPLACE原DSH/模型视觉；REMOVE本片舞者。
- 新代码：dr_ui.choice_box, dr_layers.hand_detail, dr_timeline.choice_events, s_dr_weird.shot_dr42（此处是实现计划，并非已经实现）。
- 技术：PIL/RGBA；直接复用font；旧monkey patch为零；section计划路径 film/deltarune/s_dr_weird.py。HTML不必需；原创透明角色/布景预渲染可选。
- PoC：无；not yet rendered。
- Asset：Kris原创轮廓与该镜几何场景；study可程序化；生产美术与游戏画面核对待完成。
- 待问/限制：精确游戏layout/time limit待R02，不沿用游戏tick当PVframe。
- Still QA：[2928, 2934, 2971, 3013]；关键事件：['K03']。

### DR43 — 偏离也有条件

- 范围：3014–3093 exclusive；125.583333–128.875000s。
- 音乐：挑战上游的规则；line IDs [63, 64]。详细word/frame锚点保存在JSON，不复制歌词。
- Chapter/Route：2 / 4 / weird / thematic crosscut；证据 E08 E24。
- 叙述目的：强力影响与狭窄可选结果并存。
- Player：输入影响强但维持路线条件严格；Kris：被代行命令并保留局部抵抗/反冲；他者：Noelle拒绝/执行/察觉不同声音；Story：规定命令与锁定限制其他解法。
- Camera/Layout：split；固定1280×720；左主体24,56,384,604，右世界404,56,1164,604；上框/底带不随镜头变换。
- Foreground：Kris轮廓/手，Noelle远景。用途：把主体动作/受输入的对象放在第一阅读层。
- Background：一条backtrack路线过三个门槛。用途：提供该镜空间边界与关系，避免无意义装饰。
- UI：required输入格逐个关闭其他分支。用途：显现可选行动、输入归属与当前限制。
- Text：无；无。
- Character：Kris；原创程序化轮廓study；最终美术未验收。
- SOUL：按条件路径移动，每到门槛停一帧；指示同一输入入口的空间位置，不裁定灵魂本体身份。
- In：承接DR42：连接重新形成但右世界暖色退；Out：门槛落成ring锁定边缘。
- Colour：#070A14, #E7E9F2, #F04462, #C7E4EC；Motion：路径折返、正确输入开门但外框不变；Effects：仅接触点窄glow、低强scanline；冲突段可路线触发glitch，不能遮心/手/选项。
- 复用：film/tui_pv_world_execute_20260926/continuity_full_v2/kit.py: transparent her_layer/chrome separation (design reuse)；film/tui_pv_world_execute_20260926/tuikit.py: font/scale_alpha/post。保留/替换：KEEP分层/读区；ADAPT pane/载体；REPLACE原DSH/模型视觉；REMOVE本片舞者。
- 新代码：dr_ui.control_pane, dr_ui.kris_study, dr_layers.world_body, s_dr_weird.shot_dr43（此处是实现计划，并非已经实现）。
- 技术：PIL/RGBA；直接复用font；旧monkey patch为零；section计划路径 film/deltarune/s_dr_weird.py。HTML不必需；原创透明角色/布景预渲染可选。
- PoC：无；not yet rendered。
- Asset：Kris原创轮廓与该镜几何场景；study可程序化；生产美术与游戏画面核对待完成。
- 待问/限制：不把剧情条件写作真实游戏code snippet。
- Still QA：[3014, 3020, 3053, 3092]；关键事件：[]。

### DR44 — 路线锁定的代价

- 范围：3093–3149 exclusive；128.875000–131.208333s。
- 音乐：参数不再被接受；line IDs [64, 65]。详细word/frame锚点保存在JSON，不复制歌词。
- Chapter/Route：4 / weird；证据 E25 E26。
- 叙述目的：锁定经由Kris手施加给Noelle。
- Player：输入影响强但维持路线条件严格；Kris：被代行命令并保留局部抵抗/反冲；他者：Noelle拒绝/执行/察觉不同声音；Story：规定命令与锁定限制其他解法。
- Camera/Layout：close；右世界占主要面积；左仍留Kris胸/手轮廓；选择框最小字高24px；心不被glow盖住。
- Foreground：Kris手与Noelle手腕轮廓，ring只作红裂线。用途：把主体动作/受输入的对象放在第一阅读层。
- Background：人物脸退远不作猎奇。用途：提供该镜空间边界与关系，避免无意义装饰。
- UI：option分支合并后锁线闭合。用途：显现可选行动、输入归属与当前限制。
- Text：无；无。
- Character：Kris；原创程序化轮廓study；最终美术未验收。
- SOUL：仍在命令位置，身体手运动与心不是同一物；指示同一输入入口的空间位置，不裁定灵魂本体身份。
- In：承接DR43：门槛落成ring锁定边缘；Out：红线回冲至Kris胸边。
- Colour：#070A14, #E7E9F2, #F04462, #C7E4EC；Motion：3093–3101抓腕图形；3102–3110裂线扩展；之后hold；Effects：仅接触点窄glow、低强scanline；冲突段可路线触发glitch，不能遮心/手/选项。
- 复用：film/tui_pv_world_execute_20260926/tuikit.py: font/post；film/pv_dsh_frontend_20260927/dsh_her.py: LEAD readability principle (design reuse)。保留/替换：KEEP分层/读区；ADAPT pane/载体；REPLACE原DSH/模型视觉；REMOVE本片舞者。
- 新代码：dr_ui.choice_box, dr_layers.hand_detail, dr_timeline.choice_events, s_dr_weird.shot_dr44（此处是实现计划，并非已经实现）。
- 技术：PIL/RGBA；直接复用font；旧monkey patch为零；section计划路径 film/deltarune/s_dr_weird.py。HTML不必需；原创透明角色/布景预渲染可选。
- PoC：无；not yet rendered。
- Asset：Kris原创轮廓与该镜几何场景；study可程序化；生产美术与游戏画面核对待完成。
- 待问/限制：采用当前red crack意象，原像素/玫瑰动画不混合。
- Still QA：[3093, 3099, 3121, 3148]；关键事件：['K04']。

### DR45 — 反冲到接口

- 范围：3149–3232 exclusive；131.208333–134.666667s。
- 音乐：不合法动作与冲突；line IDs [65]。详细word/frame锚点保存在JSON，不复制歌词。
- Chapter/Route：4 / weird；证据 E26 E28。
- 叙述目的：Kris反击连接却仍承受自身代价。
- Player：输入影响强但维持路线条件严格；Kris：被代行命令并保留局部抵抗/反冲；他者：Noelle拒绝/执行/察觉不同声音；Story：规定命令与锁定限制其他解法。
- Camera/Layout：split；固定1280×720；左主体24,56,384,604，右世界404,56,1164,604；上框/底带不随镜头变换。
- Foreground：Kris脚/手把SOUL放进垃圾桶意象。用途：把主体动作/受输入的对象放在第一阅读层。
- Background：程序化浴室容器和稳定地面。用途：提供该镜空间边界与关系，避免无意义装饰。
- UI：input框停留但暗，底带保留。用途：显现可选行动、输入归属与当前限制。
- Text：无；无。
- Character：Kris；原创程序化轮廓study；最终美术未验收。
- SOUL：落入容器，被震动而非消失；指示同一输入入口的空间位置，不裁定灵魂本体身份。
- In：承接DR44：红线回冲至Kris胸边；Out：容器框变倒下身体边线。
- Colour：#070A14, #E7E9F2, #F04462, #C7E4EC；Motion：一次抽出、一踢、震动回到心，随后停止；不反复自伤爽感；Effects：仅接触点窄glow、低强scanline；冲突段可路线触发glitch，不能遮心/手/选项。
- 复用：film/tui_pv_world_execute_20260926/continuity_full_v2/kit.py: transparent her_layer/chrome separation (design reuse)；film/tui_pv_world_execute_20260926/tuikit.py: font/scale_alpha/post。保留/替换：KEEP分层/读区；ADAPT pane/载体；REPLACE原DSH/模型视觉；REMOVE本片舞者。
- 新代码：dr_ui.control_pane, dr_ui.kris_study, dr_layers.world_body, s_dr_weird.shot_dr45（此处是实现计划，并非已经实现）。
- 技术：PIL/RGBA；直接复用font；旧monkey patch为零；section计划路径 film/deltarune/s_dr_weird.py。HTML不必需；原创透明角色/布景预渲染可选。
- PoC：无；not yet rendered。
- Asset：Kris原创轮廓与该镜几何场景；study可程序化；生产美术与游戏画面核对待完成。
- 待问/限制：不给反冲加自由胜利文本。
- Still QA：[3149, 3155, 3190, 3231]；关键事件：[]。

### DR46 — 命令没有随身体倒下

- 范围：3232–3323 exclusive；134.666667–138.458333s。
- 音乐：器乐第一层压力；line IDs []。详细word/frame锚点保存在JSON，不复制歌词。
- Chapter/Route：2 / weird / thematic crosscut；证据 E09 E12。
- 叙述目的：异常声音的来源不等于当前身体动作。
- Player：输入影响强但维持路线条件严格；Kris：被代行命令并保留局部抵抗/反冲；他者：Noelle拒绝/执行/察觉不同声音；Story：规定命令与锁定限制其他解法。
- Camera/Layout：split；固定1280×720；左主体24,56,384,604，右世界404,56,1164,604；上框/底带不随镜头变换。
- Foreground：Kris低姿态，Noelle远端仍面向命令。用途：把主体动作/受输入的对象放在第一阅读层。
- Background：冰白小空间保留battle线。用途：提供该镜空间边界与关系，避免无意义装饰。
- UI：命令格仍亮但Kris手不动。用途：显现可选行动、输入归属与当前限制。
- Text：无；无。
- Character：Kris；原创程序化轮廓study；最终美术未验收。
- SOUL：menu接口仍可见，不作魂出窍生理说明；指示同一输入入口的空间位置，不裁定灵魂本体身份。
- In：承接DR45：容器框变倒下身体边线；Out：输入波形成小游戏控制线。
- Colour：#070A14, #E7E9F2, #F04462, #C7E4EC；Motion：input波越过倒下Kris到Noelle，身体不给同步走动；Effects：仅接触点窄glow、低强scanline；冲突段可路线触发glitch，不能遮心/手/选项。
- 复用：film/tui_pv_world_execute_20260926/continuity_full_v2/kit.py: transparent her_layer/chrome separation (design reuse)；film/tui_pv_world_execute_20260926/tuikit.py: font/scale_alpha/post。保留/替换：KEEP分层/读区；ADAPT pane/载体；REPLACE原DSH/模型视觉；REMOVE本片舞者。
- 新代码：dr_ui.control_pane, dr_ui.kris_study, dr_layers.world_body, s_dr_weird.shot_dr46（此处是实现计划，并非已经实现）。
- 技术：PIL/RGBA；直接复用font；旧monkey patch为零；section计划路径 film/deltarune/s_dr_weird.py。HTML不必需；原创透明角色/布景预渲染可选。
- PoC：无；not yet rendered。
- Asset：Kris原创轮廓与该镜几何场景；study可程序化；生产美术与游戏画面核对待完成。
- 待问/限制：DOWN不是死亡，不能画grave碑。
- Still QA：[3232, 3238, 3277, 3322]；关键事件：[]。

### DR47 — 逃离需先拿到钥匙

- 范围：3323–3412 exclusive；138.458333–142.166667s。
- 音乐：器乐第二层压力；line IDs []。详细word/frame锚点保存在JSON，不复制歌词。
- Chapter/Route：3 / sword；证据 E15 E16。
- 叙述目的：越界被关卡设计引导，不是作者随意glitch。
- Player：在Kris与小游戏之间切换控制对象；Kris：可抵抗输入、保护他人、退出某控制链；他者：Susie可介入；舞台规则也约束角色；Story：越界须经过游戏已有障碍与触发器。
- Camera/Layout：nested；右侧世界内再置TV内框；左侧Kris维持同尺寸；跨界对象不缩放chrome。
- Foreground：Kris手握controller，HERO_SWORD在内层。用途：把主体动作/受输入的对象放在第一阅读层。
- Background：简化board障碍/门，不放原地图。用途：提供该镜空间边界与关系，避免无意义装饰。
- UI：输入下箭头与角色向上阻力。用途：显现可选行动、输入归属与当前限制。
- Text：无；无。
- Character：Kris；原创程序化轮廓study；最终美术未验收。
- SOUL：内游戏control中心，Kris肩仍有动作；指示同一输入入口的空间位置，不裁定灵魂本体身份。
- In：承接DR46：输入波形成小游戏控制线；Out：门上边界延展成第二框。
- Colour：#070A14, #E7E9F2, #F04462, #75A58B；Motion：上下两方向冲突重复两次，角色不穿墙；Effects：仅接触点窄glow、低强scanline；冲突段可路线触发glitch，不能遮心/手/选项。
- 复用：film/tui_pv_world_execute_20260926/continuity_full_v2/cuts.py: Frame/content/over concept；film/tui_pv_world_execute_20260926/continuity_full_v2/kit.py: carrier positioning (design reuse)。保留/替换：KEEP分层/读区；ADAPT pane/载体；REPLACE原DSH/模型视觉；REMOVE本片舞者。
- 新代码：dr_layers.inner_game, dr_layers.hero_carrier, dr_timeline.control_target, s_dr_nested.shot_dr47（此处是实现计划，并非已经实现）。
- 技术：PIL/RGBA；直接复用font；旧monkey patch为零；section计划路径 film/deltarune/s_dr_nested.py。HTML不必需；原创透明角色/布景预渲染可选。
- PoC：无；not yet rendered。
- Asset：Kris原创轮廓与该镜几何场景；study可程序化；生产美术与游戏画面核对待完成。
- 待问/限制：不凭shelter门下结论说Kris是Knight。
- Still QA：[3323, 3329, 3367, 3411]；关键事件：[]。

### DR48 — 框外还有框

- 范围：3412–3549 exclusive；142.166667–147.875000s。
- 音乐：器乐蓄压至执行前；line IDs []。详细word/frame锚点保存在JSON，不复制歌词。
- Chapter/Route：3 / sword / author metaphor；证据 E15 E16 E18。
- 叙述目的：Player的越界愿望仍落入可实现区域。
- Player：在Kris与小游戏之间切换控制对象；Kris：可抵抗输入、保护他人、退出某控制链；他者：Susie可介入；舞台规则也约束角色；Story：越界须经过游戏已有障碍与触发器。
- Camera/Layout：full；世界占满24,56,1164,604；Kris必须在世界中有锚点；控制框可退到边缘，底带固定。
- Foreground：Kris靠左内边，内游戏小人靠第二边。用途：把主体动作/受输入的对象放在第一阅读层。
- Background：被剪开的第一框外有另一个相同框。用途：提供该镜空间边界与关系，避免无意义装饰。
- UI：choice/门槛符号消失但边界留。用途：显现可选行动、输入归属与当前限制。
- Text：无；无。
- Character：Kris；原创程序化轮廓study；最终美术未验收。
- SOUL：随小游戏对象移动，身体锚点不变；指示同一输入入口的空间位置，不裁定灵魂本体身份。
- In：承接DR47：门上边界延展成第二框；Out：第二框回缩成execution命令格。
- Colour：#070A14, #E7E9F2, #F04462, #75A58B；Motion：3412–3423出第一框；3424–3435新外框显；之后hold；Effects：仅接触点窄glow、低强scanline；冲突段可路线触发glitch，不能遮心/手/选项。
- 复用：film/tui_pv_world_execute_20260926/continuity_full_v2/v2.py: FULL_ART slide staging (design reuse)；film/tui_pv_world_execute_20260926/tuikit.py: post。保留/替换：KEEP分层/读区；ADAPT pane/载体；REPLACE原DSH/模型视觉；REMOVE本片舞者。
- 新代码：dr_layers.full_world, dr_timeline.integer_slide, s_dr_nested.shot_dr48（此处是实现计划，并非已经实现）。
- 技术：PIL/RGBA；直接复用font；旧monkey patch为零；section计划路径 film/deltarune/s_dr_nested.py。HTML不必需；原创透明角色/布景预渲染可选。
- PoC：无；not yet rendered。
- Asset：Kris原创轮廓与该镜几何场景；study可程序化；生产美术与游戏画面核对待完成。
- 待问/限制：此镜越界空间是PV隐喻，不声称游戏无限套娃。
- Still QA：[3412, 3418, 3480, 3548]；关键事件：['K05']。

### DR49 — 命令一至六

- 范围：3549–3682 exclusive；147.875000–153.416667s。
- 音乐：重复执行前半；line IDs [67, 68, 69, 70, 71, 72]。详细word/frame锚点保存在JSON，不复制歌词。
- Chapter/Route：2 / weird / condensed replay；证据 E08 E10。
- 叙述目的：让每次命令可读为再选择而非杀敌爽点。
- Player：输入影响强但维持路线条件严格；Kris：被代行命令并保留局部抵抗/反冲；他者：Noelle拒绝/执行/察觉不同声音；Story：规定命令与锁定限制其他解法。
- Camera/Layout：split；固定1280×720；左主体24,56,384,604，右世界404,56,1164,604；上框/底带不随镜头变换。
- Foreground：Kris的手留前景，Noelle施法方向远端。用途：把主体动作/受输入的对象放在第一阅读层。
- Background：冰空位逐个留下，非具体六只敌人名单。用途：提供该镜空间边界与关系，避免无意义装饰。
- UI：单命令格pulse-index六次。用途：显现可选行动、输入归属与当前限制。
- Text：无；无。
- Character：Kris；原创程序化轮廓study；最终美术未验收。
- SOUL：每起音轻接触menu，仍同一心；指示同一输入入口的空间位置，不裁定灵魂本体身份。
- In：承接DR48：第二框回缩成execution命令格；Out：同格继续，不切换六张游戏画面。
- Colour：#070A14, #E7E9F2, #F04462, #C7E4EC；Motion：line67–72起音各一次框收窄，12帧以内hold；Effects：仅接触点窄glow、低强scanline；冲突段可路线触发glitch，不能遮心/手/选项。
- 复用：film/tui_pv_world_execute_20260926/continuity_full_v2/kit.py: transparent her_layer/chrome separation (design reuse)；film/tui_pv_world_execute_20260926/tuikit.py: font/scale_alpha/post。保留/替换：KEEP分层/读区；ADAPT pane/载体；REPLACE原DSH/模型视觉；REMOVE本片舞者。
- 新代码：dr_ui.control_pane, dr_ui.kris_study, dr_layers.world_body, s_dr_execution.shot_dr49（此处是实现计划，并非已经实现）。
- 技术：PIL/RGBA；直接复用font；旧monkey patch为零；section计划路径 film/deltarune/s_dr_execution.py。HTML不必需；原创透明角色/布景预渲染可选。
- PoC：无；not yet rendered。
- Asset：Kris原创轮廓与该镜几何场景；study可程序化；生产美术与游戏画面核对待完成。
- 待问/限制：六pulse是歌曲计数，不是canon杀敌数。
- Still QA：[3549, 3555, 3615, 3681]；关键事件：[]。

### DR50 — 命令七至十二

- 范围：3682–3821 exclusive；153.416667–159.208333s。
- 音乐：重复执行后半；line IDs [72, 73, 74, 75, 76, 77, 78, 79]。详细word/frame锚点保存在JSON，不复制歌词。
- Chapter/Route：2 / weird / condensed replay；证据 E10 E11。
- 叙述目的：重复越过拒绝，身体与命令归属渐分。
- Player：输入影响强但维持路线条件严格；Kris：被代行命令并保留局部抵抗/反冲；他者：Noelle拒绝/执行/察觉不同声音；Story：规定命令与锁定限制其他解法。
- Camera/Layout：close；右世界占主要面积；左仍留Kris胸/手轮廓；选择框最小字高24px；心不被glow盖住。
- Foreground：Kris手更僵，Noelle手势停在执行方向。用途：把主体动作/受输入的对象放在第一阅读层。
- Background：Berdly空位/冰几何一次，不能每拍死亡。用途：提供该镜空间边界与关系，避免无意义装饰。
- UI：拒绝的可见空间减少，菜单仍相同。用途：显现可选行动、输入归属与当前限制。
- Text：无；无。
- Character：Kris；原创程序化轮廓study；最终美术未验收。
- SOUL：每起音压一次选择位置，位置并不等于意志；指示同一输入入口的空间位置，不裁定灵魂本体身份。
- In：承接DR49：同格继续，不切换六张游戏画面；Out：输入归属从身体旁迁到UI边。
- Colour：#070A14, #E7E9F2, #F04462, #C7E4EC；Motion：line73–78各pulse；frame3795末次后hold至3821；Effects：仅接触点窄glow、低强scanline；冲突段可路线触发glitch，不能遮心/手/选项。
- 复用：film/tui_pv_world_execute_20260926/tuikit.py: font/post；film/pv_dsh_frontend_20260927/dsh_her.py: LEAD readability principle (design reuse)。保留/替换：KEEP分层/读区；ADAPT pane/载体；REPLACE原DSH/模型视觉；REMOVE本片舞者。
- 新代码：dr_ui.choice_box, dr_layers.hand_detail, dr_timeline.choice_events, s_dr_execution.shot_dr50（此处是实现计划，并非已经实现）。
- 技术：PIL/RGBA；直接复用font；旧monkey patch为零；section计划路径 film/deltarune/s_dr_execution.py。HTML不必需；原创透明角色/布景预渲染可选。
- PoC：无；not yet rendered。
- Asset：Kris原创轮廓与该镜几何场景；study可程序化；生产美术与游戏画面核对待完成。
- 待问/限制：末第12起音3795保留在本镜，不与计数混算。
- Still QA：[3682, 3688, 3751, 3820]；关键事件：[]。

### DR51 — 谁发出最后呼唤

- 范围：3821–3902 exclusive；159.208333–162.583333s。
- 音乐：多语言计数与呼唤归属；line IDs [79, 80, 81, 82]。详细word/frame锚点保存在JSON，不复制歌词。
- Chapter/Route：2 / 3 / weird / sword thematic crosscut；证据 E11 E18。
- 叙述目的：叙述主语和control对象可以改变。
- Player：在Kris与小游戏之间切换控制对象；Kris：可抵抗输入、保护他人、退出某控制链；他者：Susie可介入；舞台规则也约束角色；Story：越界须经过游戏已有障碍与触发器。
- Camera/Layout：nested；右侧世界内再置TV内框；左侧Kris维持同尺寸；跨界对象不缩放chrome。
- Foreground：左Kris不动，右小游戏HERO形状待跨界。用途：把主体动作/受输入的对象放在第一阅读层。
- Background：计数格不是chapter列表。用途：提供该镜空间边界与关系，避免无意义装饰。
- UI：主体状态格与input格分离。用途：显现可选行动、输入归属与当前限制。
- Text：KRIS / YOU（作者主语标记）；短菜单/名称或明确作者标记，非歌词/新增角色对白。
- Character：Kris；原创程序化轮廓study；最终美术未验收。
- SOUL：从Kris接口迁向小游戏对象的control轨迹；指示同一输入入口的空间位置，不裁定灵魂本体身份。
- In：承接DR50：输入归属从身体旁迁到UI边；Out：HERO脚步到TV白边。
- Colour：#070A14, #E7E9F2, #F04462, #75A58B；Motion：79–81三组轻计数；82收束；Effects：仅接触点窄glow、低强scanline；冲突段可路线触发glitch，不能遮心/手/选项。
- 复用：film/tui_pv_world_execute_20260926/continuity_full_v2/cuts.py: Frame/content/over concept；film/tui_pv_world_execute_20260926/continuity_full_v2/kit.py: carrier positioning (design reuse)。保留/替换：KEEP分层/读区；ADAPT pane/载体；REPLACE原DSH/模型视觉；REMOVE本片舞者。
- 新代码：dr_layers.inner_game, dr_layers.hero_carrier, dr_timeline.control_target, s_dr_execution.shot_dr51（此处是实现计划，并非已经实现）。
- 技术：PIL/RGBA；直接复用font；旧monkey patch为零；section计划路径 film/deltarune/s_dr_execution.py。HTML不必需；原创透明角色/布景预渲染可选。
- PoC：无；not yet rendered。
- Asset：Kris原创轮廓与该镜几何场景；study可程序化；生产美术与游戏画面核对待完成。
- 待问/限制：不配现实人发声、不宣告YOU=全知玩家。
- Still QA：[3821, 3827, 3861, 3901]；关键事件：[]。

### DR52 — 走出屏幕

- 范围：3902–3988 exclusive；162.583333–166.166667s。
- 音乐：把执行交给他者；line IDs [83, 84]。详细word/frame锚点保存在JSON，不复制歌词。
- Chapter/Route：3 / sword；证据 E18。
- 叙述目的：输入对象不再与Kris绑定。
- Player：在Kris与小游戏之间切换控制对象；Kris：可抵抗输入、保护他人、退出某控制链；他者：Susie可介入；舞台规则也约束角色；Story：越界须经过游戏已有障碍与触发器。
- Camera/Layout：nested；右侧世界内再置TV内框；左侧Kris维持同尺寸；跨界对象不缩放chrome。
- Foreground：HERO_SWORD跨TV边；Kris退后保持主体大比例。用途：把主体动作/受输入的对象放在第一阅读层。
- Background：TV内地面与外地面断口同高。用途：提供该镜空间边界与关系，避免无意义装饰。
- UI：left input连接新对象，Kris接口空。用途：显现可选行动、输入归属与当前限制。
- Text：无；无。
- Character：Kris；原创程序化轮廓study；最终美术未验收。
- SOUL：control载体跟HERO，不能另生第二心；指示同一输入入口的空间位置，不裁定灵魂本体身份。
- In：承接DR51：HERO脚步到TV白边；Out：HERO前进方向转向Susie/Kris。
- Colour：#070A14, #E7E9F2, #F04462, #75A58B；Motion：3902–3907至边；3908–3913跨边；3914–3925Kris后退；之后hold；Effects：仅接触点窄glow、低强scanline；冲突段可路线触发glitch，不能遮心/手/选项。
- 复用：film/tui_pv_world_execute_20260926/continuity_full_v2/cuts.py: Frame/content/over concept；film/tui_pv_world_execute_20260926/continuity_full_v2/kit.py: carrier positioning (design reuse)。保留/替换：KEEP分层/读区；ADAPT pane/载体；REPLACE原DSH/模型视觉；REMOVE本片舞者。
- 新代码：dr_layers.inner_game, dr_layers.hero_carrier, dr_timeline.control_target, s_dr_execution.shot_dr52（此处是实现计划，并非已经实现）。
- 技术：PIL/RGBA；直接复用font；旧monkey patch为零；section计划路径 film/deltarune/s_dr_execution.py。HTML不必需；原创透明角色/布景预渲染可选。
- PoC：无；not yet rendered。
- Asset：Kris原创轮廓与该镜几何场景；study可程序化；生产美术与游戏画面核对待完成。
- 待问/限制：R01连续录像未看，先画关系geometry。
- Still QA：[3902, 3908, 3945, 3987]；关键事件：['K06']。

### DR53 — Kris会保护别人

- 范围：3988–4072 exclusive；166.166667–169.666667s。
- 音乐：执行作用反转；line IDs [85, 86]。详细word/frame锚点保存在JSON，不复制歌词。
- Chapter/Route：3 / sword；证据 E19。
- 叙述目的：Kris不只抵抗，也能给他者留空间。
- Player：在Kris与小游戏之间切换控制对象；Kris：可抵抗输入、保护他人、退出某控制链；他者：Susie可介入；舞台规则也约束角色；Story：越界须经过游戏已有障碍与触发器。
- Camera/Layout：nested；右侧世界内再置TV内框；左侧Kris维持同尺寸；跨界对象不缩放chrome。
- Foreground：Kris把Susie拉出HERO攻击线。用途：把主体动作/受输入的对象放在第一阅读层。
- Background：外TV/内游戏地面同框。用途：提供该镜空间边界与关系，避免无意义装饰。
- UI：controller线最终被拔，input仍存在于框外。用途：显现可选行动、输入归属与当前限制。
- Text：无；无。
- Character：Kris；原创程序化轮廓study；最终美术未验收。
- SOUL：失去当前对象，不退化成死心；指示同一输入入口的空间位置，不裁定灵魂本体身份。
- In：承接DR52：HERO前进方向转向Susie/Kris；Out：断线落为四空选项。
- Colour：#070A14, #E7E9F2, #F04462, #75A58B；Motion：3988–3995攻击线接近；3996–4003拉离；4004–4011断线；之后hold；Effects：仅接触点窄glow、低强scanline；冲突段可路线触发glitch，不能遮心/手/选项。
- 复用：film/tui_pv_world_execute_20260926/continuity_full_v2/cuts.py: Frame/content/over concept；film/tui_pv_world_execute_20260926/continuity_full_v2/kit.py: carrier positioning (design reuse)。保留/替换：KEEP分层/读区；ADAPT pane/载体；REPLACE原DSH/模型视觉；REMOVE本片舞者。
- 新代码：dr_layers.inner_game, dr_layers.hero_carrier, dr_timeline.control_target, s_dr_execution.shot_dr53（此处是实现计划，并非已经实现）。
- 技术：PIL/RGBA；直接复用font；旧monkey patch为零；section计划路径 film/deltarune/s_dr_execution.py。HTML不必需；原创透明角色/布景预渲染可选。
- PoC：无；not yet rendered。
- Asset：Kris原创轮廓与该镜几何场景；study可程序化；生产美术与游戏画面核对待完成。
- 待问/限制：不声称Kris用这动作使全游戏自由。
- Still QA：[3988, 3994, 4030, 4071]；关键事件：['K07']。

### DR54 — 归来的空白

- 范围：4072–4164 exclusive；169.666667–173.500000s。
- 音乐：取回接口与再受困；line IDs [86, 87, 88, 89]。详细word/frame锚点保存在JSON，不复制歌词。
- Chapter/Route：4 / weird / thematic crosscut；证据 E27 E28。
- 叙述目的：恢复输入不保证能表达自己的答复。
- Player：输入影响强但维持路线条件严格；Kris：被代行命令并保留局部抵抗/反冲；他者：Noelle拒绝/执行/察觉不同声音；Story：规定命令与锁定限制其他解法。
- Camera/Layout：close；右世界占主要面积；左仍留Kris胸/手轮廓；选择框最小字高24px；心不被glow盖住。
- Foreground：Kris胸/手，Susie提问姿态小影子。用途：把主体动作/受输入的对象放在第一阅读层。
- Background：雨线暂停只作为原场景意象。用途：提供该镜空间边界与关系，避免无意义装饰。
- UI：四个空白slot；不是四个隐藏回答。用途：显现可选行动、输入归属与当前限制。
- Text：无；无。
- Character：Kris；原创程序化轮廓study；最终美术未验收。
- SOUL：selector可移动但文本为空；指示同一输入入口的空间位置，不裁定灵魂本体身份。
- In：承接DR53：断线落为四空选项；Out：四格收成起床方向格。
- Colour：#070A14, #E7E9F2, #F04462, #C7E4EC；Motion：4072–4083框显；之后slot高亮变化而Kris不说话；Effects：仅接触点窄glow、低强scanline；冲突段可路线触发glitch，不能遮心/手/选项。
- 复用：film/tui_pv_world_execute_20260926/tuikit.py: font/post；film/pv_dsh_frontend_20260927/dsh_her.py: LEAD readability principle (design reuse)。保留/替换：KEEP分层/读区；ADAPT pane/载体；REPLACE原DSH/模型视觉；REMOVE本片舞者。
- 新代码：dr_ui.choice_box, dr_layers.hand_detail, dr_timeline.choice_events, s_dr_execution.shot_dr54（此处是实现计划，并非已经实现）。
- 技术：PIL/RGBA；直接复用font；旧monkey patch为零；section计划路径 film/deltarune/s_dr_execution.py。HTML不必需；原创透明角色/布景预渲染可选。
- PoC：无；not yet rendered。
- Asset：Kris原创轮廓与该镜几何场景；study可程序化；生产美术与游戏画面核对待完成。
- 待问/限制：不把blank选项填成作者希望的Kris独白。
- Still QA：[4072, 4078, 4118, 4163]；关键事件：[]。

### DR55 — 起床的阻力

- 范围：4164–4259 exclusive；173.500000–177.458333s。
- 音乐：受困反复；line IDs [89, 90, 91]。详细word/frame锚点保存在JSON，不复制歌词。
- Chapter/Route：5 / weird；证据 E31。
- 叙述目的：输入多却只换来小幅身体进度。
- Player：可移selector但当前两项结果趋同；仍可停止输入；Kris：动作迟缓/手迟疑，动机未知；他者：Noelle主动要求旧命令并否定拒绝；Story：湖段先收窄选择，再以时限要求持续确认。
- Camera/Layout：split；固定1280×720；左主体24,56,384,604，右世界404,56,1164,604；上框/底带不随镜头变换。
- Foreground：Kris床上起身轮廓，手勉强落地。用途：把主体动作/受输入的对象放在第一阅读层。
- Background：简化卧室床/地面，后窗暮色。用途：提供该镜空间边界与关系，避免无意义装饰。
- UI：方向input重复，身体进度小。用途：显现可选行动、输入归属与当前限制。
- Text：无；无。
- Character：Kris；原创程序化轮廓study；最终美术未验收。
- SOUL：在胸前微弱，方向input红边一次次亮；指示同一输入入口的空间位置，不裁定灵魂本体身份。
- In：承接DR54：四格收成起床方向格；Out：暮光延展为湖面水平线。
- Colour：#070A14, #E7E9F2, #F04462, #C7E4EC；Motion：每两次pulse身体上抬1px；无机械数值百分比；Effects：仅接触点窄glow、低强scanline；冲突段可路线触发glitch，不能遮心/手/选项。
- 复用：film/tui_pv_world_execute_20260926/continuity_full_v2/kit.py: transparent her_layer/chrome separation (design reuse)；film/tui_pv_world_execute_20260926/tuikit.py: font/scale_alpha/post。保留/替换：KEEP分层/读区；ADAPT pane/载体；REPLACE原DSH/模型视觉；REMOVE本片舞者。
- 新代码：dr_ui.control_pane, dr_ui.kris_study, dr_layers.world_body, s_dr_reverse.shot_dr55（此处是实现计划，并非已经实现）。
- 技术：PIL/RGBA；直接复用font；旧monkey patch为零；section计划路径 film/deltarune/s_dr_reverse.py。HTML不必需；原创透明角色/布景预渲染可选。
- PoC：无；not yet rendered。
- Asset：Kris原创轮廓与该镜几何场景；study可程序化；生产美术与游戏画面核对待完成。
- 待问/限制：动作动机未知，不给抗议独白。
- Still QA：[4164, 4170, 4211, 4258]；关键事件：[]。

### DR56 — 她开始索求命令

- 范围：4259–4344 exclusive；177.458333–181.000000s。
- 音乐：学习关系的方式；line IDs [91, 92]。详细word/frame锚点保存在JSON，不复制歌词。
- Chapter/Route：5 / weird；证据 E32。
- 叙述目的：Noelle的主动并不证明已自由。
- Player：可移selector但当前两项结果趋同；仍可停止输入；Kris：动作迟缓/手迟疑，动机未知；他者：Noelle主动要求旧命令并否定拒绝；Story：湖段先收窄选择，再以时限要求持续确认。
- Camera/Layout：split；固定1280×720；左主体24,56,384,604，右世界404,56,1164,604；上框/底带不随镜头变换。
- Foreground：Kris近景手迟疑，Noelle远端手向左伸。用途：把主体动作/受输入的对象放在第一阅读层。
- Background：湖面+岸边无终末戏剧云。用途：提供该镜空间边界与关系，避免无意义装饰。
- UI：choice框由Noelle方向滑向心。用途：显现可选行动、输入归属与当前限制。
- Text：无；无。
- Character：Kris；原创程序化轮廓study；最终美术未验收。
- SOUL：被索求的接口留于框内；身体不主动扑向她；指示同一输入入口的空间位置，不裁定灵魂本体身份。
- In：承接DR55：暮光延展为湖面水平线；Out：choice框停为两项。
- Colour：#070A14, #E7E9F2, #F04462, #C7E4EC；Motion：Noelle手到Kris腕前，线由她向menu发出；Effects：仅接触点窄glow、低强scanline；冲突段可路线触发glitch，不能遮心/手/选项。
- 复用：film/tui_pv_world_execute_20260926/continuity_full_v2/kit.py: transparent her_layer/chrome separation (design reuse)；film/tui_pv_world_execute_20260926/tuikit.py: font/scale_alpha/post。保留/替换：KEEP分层/读区；ADAPT pane/载体；REPLACE原DSH/模型视觉；REMOVE本片舞者。
- 新代码：dr_ui.control_pane, dr_ui.kris_study, dr_layers.world_body, s_dr_reverse.shot_dr56（此处是实现计划，并非已经实现）。
- 技术：PIL/RGBA；直接复用font；旧monkey patch为零；section计划路径 film/deltarune/s_dr_reverse.py。HTML不必需；原创透明角色/布景预渲染可选。
- PoC：无；not yet rendered。
- Asset：Kris原创轮廓与该镜几何场景；study可程序化；生产美术与游戏画面核对待完成。
- 待问/限制：不把受创伤的主动浪漫化成爱情救赎。
- Still QA：[4259, 4265, 4301, 4343]；关键事件：[]。

### DR57 — 拒绝仍然向前

- 范围：4344–4430 exclusive；181.000000–184.583333s。
- 音乐：被质问并作答；line IDs [93, 94]。详细word/frame锚点保存在JSON，不复制歌词。
- Chapter/Route：5 / weird；证据 E33。
- 叙述目的：Player的当下拒绝与既往施压发生冲突。
- Player：可移selector但当前两项结果趋同；仍可停止输入；Kris：动作迟缓/手迟疑，动机未知；他者：Noelle主动要求旧命令并否定拒绝；Story：湖段先收窄选择，再以时限要求持续确认。
- Camera/Layout：close；右世界占主要面积；左仍留Kris胸/手轮廓；选择框最小字高24px；心不被glow盖住。
- Foreground：Kris手颤/轮廓仍为主要面积；Noelle手引向湖。用途：把主体动作/受输入的对象放在第一阅读层。
- Background：湖面抬高一小层；岸线仍在。用途：提供该镜空间边界与关系，避免无意义装饰。
- UI：Stop/Proceed同时可读，心先落Stop。用途：显现可选行动、输入归属与当前限制。
- Text：Stop / Proceed；短菜单/名称或明确作者标记，非歌词/新增角色对白。
- Character：Kris；原创程序化轮廓study；最终美术未验收。
- SOUL：在Stop项，身体仍前进微步；留下一点拒绝痕迹；指示同一输入入口的空间位置，不裁定灵魂本体身份。
- In：承接DR56：choice框停为两项；Out：文字槽保留，Stop字形开始失去区别。
- Colour：#070A14, #E7E9F2, #F04462, #C7E4EC；Motion：4344–4355心移动；4356–4367角色前移；4368后hold；Effects：仅接触点窄glow、低强scanline；冲突段可路线触发glitch，不能遮心/手/选项。
- 复用：film/tui_pv_world_execute_20260926/tuikit.py: font/post；film/pv_dsh_frontend_20260927/dsh_her.py: LEAD readability principle (design reuse)。保留/替换：KEEP分层/读区；ADAPT pane/载体；REPLACE原DSH/模型视觉；REMOVE本片舞者。
- 新代码：dr_ui.choice_box, dr_layers.hand_detail, dr_timeline.choice_events, s_dr_reverse.shot_dr57（此处是实现计划，并非已经实现）。
- 技术：PIL/RGBA；直接复用font；旧monkey patch为零；section计划路径 film/deltarune/s_dr_reverse.py。HTML不必需；原创透明角色/布景预渲染可选。
- PoC：film/deltarune_poc/renderer.py；selected mechanism study; not full shot fidelity。
- Asset：Kris原创轮廓与该镜几何场景；study可程序化；生产美术与游戏画面核对待完成。
- 待问/限制：Stop计数留差异；不标完全无效。
- Still QA：[4344, 4350, 4387, 4429]；关键事件：['K08']。

### DR58 — 两个位置同一结果

- 范围：4430–4519 exclusive；184.583333–188.291667s。
- 音乐：把关系化为表达式；line IDs [95]。详细word/frame锚点保存在JSON，不复制歌词。
- Chapter/Route：5 / weird；证据 E33 E34。
- 叙述目的：selector还能移动，结果空间却收窄。
- Player：可移selector但当前两项结果趋同；仍可停止输入；Kris：动作迟缓/手迟疑，动机未知；他者：Noelle主动要求旧命令并否定拒绝；Story：湖段先收窄选择，再以时限要求持续确认。
- Camera/Layout：close；右世界占主要面积；左仍留Kris胸/手轮廓；选择框最小字高24px；心不被glow盖住。
- Foreground：Kris近景握手；Noelle另一侧维持牵引。用途：把主体动作/受输入的对象放在第一阅读层。
- Background：湖面与两个菜单槽同宽；外框若隐若现。用途：提供该镜空间边界与关系，避免无意义装饰。
- UI：第7组概念压缩：Stop→Proceed；两槽同文。用途：显现可选行动、输入归属与当前限制。
- Text：Proceed / Proceed；短菜单/名称或明确作者标记，非歌词/新增角色对白。
- Character：Kris；原创程序化轮廓study；最终美术未验收。
- SOUL：由左到右位置可变，frame4495仍看清红心；指示同一输入入口的空间位置，不裁定灵魂本体身份。
- In：承接DR57：文字槽保留，Stop字形开始失去区别；Out：外input停顿显现，故事框继续存在。
- Colour：#070A14, #E7E9F2, #F04462, #C7E4EC；Motion：4430–4435保留Stop；4436–4441文字变形；4442–4447落为Proceed；4448–4518心移位不改变身体方向；Effects：仅接触点窄glow、低强scanline；冲突段可路线触发glitch，不能遮心/手/选项。
- 复用：film/tui_pv_world_execute_20260926/tuikit.py: font/post；film/pv_dsh_frontend_20260927/dsh_her.py: LEAD readability principle (design reuse)。保留/替换：KEEP分层/读区；ADAPT pane/载体；REPLACE原DSH/模型视觉；REMOVE本片舞者。
- 新代码：dr_ui.choice_box, dr_layers.hand_detail, dr_timeline.choice_events, s_dr_reverse.shot_dr58（此处是实现计划，并非已经实现）。
- 技术：PIL/RGBA；直接复用font；旧monkey patch为零；section计划路径 film/deltarune/s_dr_reverse.py。HTML不必需；原创透明角色/布景预渲染可选。
- PoC：film/deltarune_poc/renderer.py；selected mechanism study; not full shot fidelity。
- Asset：Kris原创轮廓与该镜几何场景；study可程序化；生产美术与游戏画面核对待完成。
- 待问/限制：PV压缩prompt次数，非逐一重演73组输入。
- Still QA：[4430, 4436, 4474, 4518]；关键事件：['K08']。

### DR59 — 停止也是输入的边界

- 范围：4519–4574 exclusive；188.291667–190.583333s。
- 音乐：看似自由的对照；line IDs [96, 97]。详细word/frame锚点保存在JSON，不复制歌词。
- Chapter/Route：5 / interrupted weird / counterfactual comparison；证据 E34 E36。
- 叙述目的：承认不持续按可以改变当前进程。
- Player：停止输入可改变这段进程，不抹除后果；Kris：身体/关系仍留痕，非全部恢复；他者：Susie关切；Noelle既往变化仍在；Story：续章及成功提前结束都是已编写出口。
- Camera/Layout：split；固定1280×720；左主体24,56,384,604，右世界404,56,1164,604；上框/底带不随镜头变换。
- Foreground：左Kris手留痕；右Susie关切的小轮廓。用途：把主体动作/受输入的对象放在第一阅读层。
- Background：成功与停止两条路径只以线区分。用途：提供该镜空间边界与关系，避免无意义装饰。
- UI：确认pulse暂停，外框留两个出口。用途：显现可选行动、输入归属与当前限制。
- Text：无；无。
- Character：Kris；原创程序化轮廓study；最终美术未验收。
- SOUL：停止selector操作，但心不被删除；指示同一输入入口的空间位置，不裁定灵魂本体身份。
- In：承接DR58：外input停顿显现，故事框继续存在；Out：两路线灰线回到一颗心。
- Colour：#070A14, #E7E9F2, #F04462, #75A58B；Motion：4519–4530pulse退去；4531–4542续章路径显；之后hold；Effects：仅接触点窄glow、低强scanline；冲突段可路线触发glitch，不能遮心/手/选项。
- 复用：film/tui_pv_world_execute_20260926/continuity_full_v2/kit.py: transparent her_layer/chrome separation (design reuse)；film/tui_pv_world_execute_20260926/tuikit.py: font/scale_alpha/post。保留/替换：KEEP分层/读区；ADAPT pane/载体；REPLACE原DSH/模型视觉；REMOVE本片舞者。
- 新代码：dr_ui.control_pane, dr_ui.kris_study, dr_layers.world_body, s_dr_reverse.shot_dr59（此处是实现计划，并非已经实现）。
- 技术：PIL/RGBA；直接复用font；旧monkey patch为零；section计划路径 film/deltarune/s_dr_reverse.py。HTML不必需；原创透明角色/布景预渲染可选。
- PoC：film/deltarune_poc/renderer.py；selected mechanism study; not full shot fidelity。
- Asset：Kris原创轮廓与该镜几何场景；study可程序化；生产美术与游戏画面核对待完成。
- 待问/限制：图形比较不是canon同时发生的多宇宙。
- Still QA：[4519, 4525, 4546, 4573]；关键事件：['K09']。

### DR60 — 继续的代价

- 范围：4574–4654 exclusive；190.583333–193.916667s。
- 音乐：受困与持续关系的尾唱；line IDs [97, 98]。详细word/frame锚点保存在JSON，不复制歌词。
- Chapter/Route：5 / weird / compare to interrupted；证据 E34 E36。
- 叙述目的：继续要求重复确认；停止支线的后果不能抹去。
- Player：可移selector但当前两项结果趋同；仍可停止输入；Kris：动作迟缓/手迟疑，动机未知；他者：Noelle主动要求旧命令并否定拒绝；Story：湖段先收窄选择，再以时限要求持续确认。
- Camera/Layout：close；右世界占主要面积；左仍留Kris胸/手轮廓；选择框最小字高24px；心不被glow盖住。
- Foreground：Kris握手仍清楚；Noelle远端将命令推回。用途：把主体动作/受输入的对象放在第一阅读层。
- Background：逐渐趋白湖面，停止支线只留关切影子。用途：提供该镜空间边界与关系，避免无意义装饰。
- UI：选择同文，时限只有收缩边不写游戏tick。用途：显现可选行动、输入归属与当前限制。
- Text：Proceed；短菜单/名称或明确作者标记，非歌词/新增角色对白。
- Character：Kris；原创程序化轮廓study；最终美术未验收。
- SOUL：红心接近白但保持红轮廓；框要求确认；指示同一输入入口的空间位置，不裁定灵魂本体身份。
- In：承接DR59：两路线灰线回到一颗心；Out：湖面折成一个框内画面。
- Colour：#070A14, #E7E9F2, #F04462, #C7E4EC；Motion：4574–4600间一次收框后复位；后一次更窄；不把静默关切消失；Effects：仅接触点窄glow、低强scanline；冲突段可路线触发glitch，不能遮心/手/选项。
- 复用：film/tui_pv_world_execute_20260926/tuikit.py: font/post；film/pv_dsh_frontend_20260927/dsh_her.py: LEAD readability principle (design reuse)。保留/替换：KEEP分层/读区；ADAPT pane/载体；REPLACE原DSH/模型视觉；REMOVE本片舞者。
- 新代码：dr_ui.choice_box, dr_layers.hand_detail, dr_timeline.choice_events, s_dr_reverse.shot_dr60（此处是实现计划，并非已经实现）。
- 技术：PIL/RGBA；直接复用font；旧monkey patch为零；section计划路径 film/deltarune/s_dr_reverse.py。HTML不必需；原创透明角色/布景预渲染可选。
- PoC：film/deltarune_poc/renderer.py；selected mechanism study; not full shot fidelity。
- Asset：Kris原创轮廓与该镜几何场景；study可程序化；生产美术与游戏画面核对待完成。
- 待问/限制：E34时限不是每组严格单调，不复刻错误线性倒计时。
- Still QA：[4574, 4580, 4614, 4653]；关键事件：['K09']。

### DR61 — 把湖留在画面里

- 范围：4654–4760 exclusive；193.916667–198.333333s。
- 音乐：器乐收束开始；line IDs []。详细word/frame锚点保存在JSON，不复制歌词。
- Chapter/Route：5 / weird / author metaphor；证据 E35。
- 叙述目的：故事接收越界而非被它击破。
- Player：可继续等待或离开，不能提供未发布的下一章；Kris：主体被留在边界内，未来未知；他者：他者不接管最后主体地位；Story：Chapter/route接口接住越界；Story是作者隐喻。
- Camera/Layout：full；世界占满24,56,1164,604；Kris必须在世界中有锚点；控制框可退到边缘，底带固定。
- Foreground：Kris手与身体轮廓保留；Noelle退到已发生场景。用途：把主体动作/受输入的对象放在第一阅读层。
- Background：湖面成为白框内图像。用途：提供该镜空间边界与关系，避免无意义装饰。
- UI：外chapter框出现但不显示未来场景。用途：显现可选行动、输入归属与当前限制。
- Text：无；无。
- Character：Kris；原创程序化轮廓study；最终美术未验收。
- SOUL：从choice到框边稳定停留；指示同一输入入口的空间位置，不裁定灵魂本体身份。
- In：承接DR60：湖面折成一个框内画面；Out：湖框外再长一圈章框。
- Colour：#070A14, #E7E9F2, #F04462, #75A58B；Motion：缩小世界frame不缩Kris识别尺寸；手锚点保持；Effects：仅接触点窄glow、低强scanline；冲突段可路线触发glitch，不能遮心/手/选项。
- 复用：film/tui_pv_world_execute_20260926/continuity_full_v2/v2.py: FULL_ART slide staging (design reuse)；film/tui_pv_world_execute_20260926/tuikit.py: post。保留/替换：KEEP分层/读区；ADAPT pane/载体；REPLACE原DSH/模型视觉；REMOVE本片舞者。
- 新代码：dr_layers.full_world, dr_timeline.integer_slide, s_dr_boundary.shot_dr61（此处是实现计划，并非已经实现）。
- 技术：PIL/RGBA；直接复用font；旧monkey patch为零；section计划路径 film/deltarune/s_dr_boundary.py。HTML不必需；原创透明角色/布景预渲染可选。
- PoC：无；not yet rendered。
- Asset：Kris原创轮廓与该镜几何场景；study可程序化；生产美术与游戏画面核对待完成。
- 待问/限制：不画湖底新世界/死亡真相。
- Still QA：[4654, 4660, 4707, 4759]；关键事件：[]。

### DR62 — 上游也有接口

- 范围：4760–4863 exclusive；198.333333–202.625000s。
- 音乐：尾奏递归；line IDs []。详细word/frame锚点保存在JSON，不复制歌词。
- Chapter/Route：1 / 3 / 5 / cross-route / author metaphor；证据 E01 E15 E35。
- 叙述目的：Player控制台也成为路线里的对象。
- Player：可继续等待或离开，不能提供未发布的下一章；Kris：主体被留在边界内，未来未知；他者：他者不接管最后主体地位；Story：Chapter/route接口接住越界；Story是作者隐喻。
- Camera/Layout：nested；右侧世界内再置TV内框；左侧Kris维持同尺寸；跨界对象不缩放chrome。
- Foreground：Kris左pane维持；右input框被外框包围。用途：把主体动作/受输入的对象放在第一阅读层。
- Background：仅三层矩形，不无限缩放难读。用途：提供该镜空间边界与关系，避免无意义装饰。
- UI：menu→route→chapter层位次依次亮。用途：显现可选行动、输入归属与当前限制。
- Text：无；无。
- Character：Kris；原创程序化轮廓study；最终美术未验收。
- SOUL：最外边心仍能移，不再声称它是最高层；指示同一输入入口的空间位置，不裁定灵魂本体身份。
- In：承接DR61：湖框外再长一圈章框；Out：三框间连线退去，留下手。
- Colour：#070A14, #E7E9F2, #F04462, #75A58B；Motion：frame4760先亮内框；4800亮route；4840亮chapter；Effects：仅接触点窄glow、低强scanline；冲突段可路线触发glitch，不能遮心/手/选项。
- 复用：film/tui_pv_world_execute_20260926/continuity_full_v2/cuts.py: Frame/content/over concept；film/tui_pv_world_execute_20260926/continuity_full_v2/kit.py: carrier positioning (design reuse)。保留/替换：KEEP分层/读区；ADAPT pane/载体；REPLACE原DSH/模型视觉；REMOVE本片舞者。
- 新代码：dr_layers.inner_game, dr_layers.hero_carrier, dr_timeline.control_target, s_dr_boundary.shot_dr62（此处是实现计划，并非已经实现）。
- 技术：PIL/RGBA；直接复用font；旧monkey patch为零；section计划路径 film/deltarune/s_dr_boundary.py。HTML不必需；原创透明角色/布景预渲染可选。
- PoC：无；not yet rendered。
- Asset：Kris原创轮廓与该镜几何场景；study可程序化；生产美术与游戏画面核对待完成。
- 待问/限制：Story是隐喻第四力，不给它角色脸。
- Still QA：[4760, 4766, 4811, 4862]；关键事件：[]。

### DR63 — 不急于给答案

- 范围：4863–4929 exclusive；202.625000–205.375000s。
- 音乐：无唱词尾奏停驻；line IDs [100]。详细word/frame锚点保存在JSON，不复制歌词。
- Chapter/Route：5 / cross-route / author metaphor；证据 E35 E36。
- 叙述目的：让角色承受与观众思考有停留。
- Player：可继续等待或离开，不能提供未发布的下一章；Kris：主体被留在边界内，未来未知；他者：他者不接管最后主体地位；Story：Chapter/route接口接住越界；Story是作者隐喻。
- Camera/Layout：full；世界占满24,56,1164,604；Kris必须在世界中有锚点；控制框可退到边缘，底带固定。
- Foreground：Kris手和遮眼轮廓，无他者主视角。用途：把主体动作/受输入的对象放在第一阅读层。
- Background：三框退到灰白，中心大片负空间。用途：提供该镜空间边界与关系，避免无意义装饰。
- UI：输入可停止的边沿开口仍留。用途：显现可选行动、输入归属与当前限制。
- Text：无；无。
- Character：Kris；原创程序化轮廓study；最终美术未验收。
- SOUL：静止但非暗灭；闪烁降至无；指示同一输入入口的空间位置，不裁定灵魂本体身份。
- In：承接DR62：三框间连线退去，留下手；Out：最后单次执行pulse落在外框。
- Colour：#070A14, #E7E9F2, #F04462, #75A58B；Motion：只湖线每beat1px，Kris不消融为代码；Effects：仅接触点窄glow、低强scanline；冲突段可路线触发glitch，不能遮心/手/选项。
- 复用：film/tui_pv_world_execute_20260926/continuity_full_v2/v2.py: FULL_ART slide staging (design reuse)；film/tui_pv_world_execute_20260926/tuikit.py: post。保留/替换：KEEP分层/读区；ADAPT pane/载体；REPLACE原DSH/模型视觉；REMOVE本片舞者。
- 新代码：dr_layers.full_world, dr_timeline.integer_slide, s_dr_boundary.shot_dr63（此处是实现计划，并非已经实现）。
- 技术：PIL/RGBA；直接复用font；旧monkey patch为零；section计划路径 film/deltarune/s_dr_boundary.py。HTML不必需；原创透明角色/布景预渲染可选。
- PoC：无；not yet rendered。
- Asset：Kris原创轮廓与该镜几何场景；study可程序化；生产美术与游戏画面核对待完成。
- 待问/限制：这是作者结尾悬置，不编写角色内心结论。
- Still QA：[4863, 4869, 4896, 4928]；关键事件：[]。

### DR64 — 提交至章节边界

- 范围：4929–4970 exclusive；205.375000–207.083333s。
- 音乐：最后执行和硬切；line IDs [100]。详细word/frame锚点保存在JSON，不复制歌词。
- Chapter/Route：5 / weird / author cut；证据 E35。
- 叙述目的：把操作归于当前章节，而非杀掉Player。
- Player：可继续等待或离开，不能提供未发布的下一章；Kris：主体被留在边界内，未来未知；他者：他者不接管最后主体地位；Story：Chapter/route接口接住越界；Story是作者隐喻。
- Camera/Layout：full；世界占满24,56,1164,604；Kris必须在世界中有锚点；控制框可退到边缘，底带固定。
- Foreground：Kris最后轮廓与手留下到4969。用途：把主体动作/受输入的对象放在第一阅读层。
- Background：世界白框在末8帧压成线。用途：提供该镜空间边界与关系，避免无意义装饰。
- UI：章边沿亮一次，不新增红命令。用途：显现可选行动、输入归属与当前限制。
- Text：无；无。
- Character：Kris；原创程序化轮廓study；最终美术未验收。
- SOUL：4948短接触外框，4969仍留一红点；指示同一输入入口的空间位置，不裁定灵魂本体身份。
- In：承接DR63：最后单次执行pulse落在外框；Out：帧4970硬切。
- Colour：#070A14, #E7E9F2, #F04462, #75A58B；Motion：4929pulse；4962–4969压线；4970切黑（global event）；Effects：仅接触点窄glow、低强scanline；冲突段可路线触发glitch，不能遮心/手/选项。
- 复用：film/tui_pv_world_execute_20260926/continuity_full_v2/v2.py: FULL_ART slide staging (design reuse)；film/tui_pv_world_execute_20260926/tuikit.py: post。保留/替换：KEEP分层/读区；ADAPT pane/载体；REPLACE原DSH/模型视觉；REMOVE本片舞者。
- 新代码：dr_layers.full_world, dr_timeline.integer_slide, s_dr_boundary.shot_dr64（此处是实现计划，并非已经实现）。
- 技术：PIL/RGBA；直接复用font；旧monkey patch为零；section计划路径 film/deltarune/s_dr_boundary.py。HTML不必需；原创透明角色/布景预渲染可选。
- PoC：film/deltarune_poc/renderer.py；selected mechanism study; not full shot fidelity。
- Asset：Kris原创轮廓与该镜几何场景；study可程序化；生产美术与游戏画面核对待完成。
- 待问/限制：音乐未在本机试听，4970继承上游精确选择。
- Still QA：[4929, 4935, 4949, 4969]；关键事件：['K10']。

### DR65 — 要求来自下一层

- 范围：4970–5004 exclusive；207.083333–208.500000s。
- 音乐：黑场尾音停留；line IDs []。详细word/frame锚点保存在JSON，不复制歌词。
- Chapter/Route：5 / weird / chapter boundary；证据 E35。
- 叙述目的：边界仍以chapter/interface语言要求继续。
- Player：可继续等待或离开，不能提供未发布的下一章；Kris：主体被留在边界内，未来未知；他者：他者不接管最后主体地位；Story：Chapter/route接口接住越界；Story是作者隐喻。
- Camera/Layout：black；全黑；仅保留一个中央边界/问题及低亮Kris手；无ticker、无词带假唱词。
- Foreground：无新人物，美术只留Kris手极低亮。用途：把主体动作/受输入的对象放在第一阅读层。
- Background：纯黑。用途：提供该镜空间边界与关系，避免无意义装饰。
- UI：小CRT边框，未发布章位置留空。用途：显现可选行动、输入归属与当前限制。
- Text：CHAPTER 7 / SIDE B（短提示意象）；短菜单/名称或明确作者标记，非歌词/新增角色对白。
- Character：Kris；原创程序化轮廓study；最终美术未验收。
- SOUL：框外一小红点，不穿未来门；指示同一输入入口的空间位置，不裁定灵魂本体身份。
- In：承接DR64：帧4970硬切；Out：章框变回一条连接。
- Colour：#070A14, #E7E9F2, #F04462, #75A58B；Motion：4970全黑；4982–4993短字显；4994以后hold；Effects：仅接触点窄glow、低强scanline；冲突段可路线触发glitch，不能遮心/手/选项。
- 复用：film/tui_pv_world_execute_20260926/continuity_full_v2/v2.py: HARD_CUT integer4970 (timing reuse)。保留/替换：KEEP分层/读区；ADAPT pane/载体；REPLACE原DSH/模型视觉；REMOVE本片舞者。
- 新代码：dr_layers.chapter_boundary, dr_layers.final_question, s_dr_final.shot_dr65（此处是实现计划，并非已经实现）。
- 技术：PIL/RGBA；直接复用font；旧monkey patch为零；section计划路径 film/deltarune/s_dr_final.py。HTML不必需；原创透明角色/布景预渲染可选。
- PoC：film/deltarune_poc/renderer.py；selected mechanism study; not full shot fidelity。
- Asset：Kris原创轮廓与该镜几何场景；study可程序化；生产美术与游戏画面核对待完成。
- 待问/限制：完整终屏文字只转录依据，具体画面待R03。
- Still QA：[4970, 4976, 4987, 5003]；关键事件：['K10']。

### DR66 — 调用方向未定

- 范围：5004–5051 exclusive；208.500000–210.458333s。
- 音乐：音乐停止后的关系残留；line IDs []。详细word/frame锚点保存在JSON，不复制歌词。
- Chapter/Route：1–5 / author synthesis；证据 E04 E18 E33 E35 E36。
- 叙述目的：不把caller/subject身份固定成胜负。
- Player：可继续等待或离开，不能提供未发布的下一章；Kris：主体被留在边界内，未来未知；他者：他者不接管最后主体地位；Story：Chapter/route接口接住越界；Story是作者隐喻。
- Camera/Layout：black；全黑；仅保留一个中央边界/问题及低亮Kris手；无ticker、无词带假唱词。
- Foreground：Kris手轮廓与红心，两者间隔至少32px。用途：把主体动作/受输入的对象放在第一阅读层。
- Background：原初白框，但一角未闭。用途：提供该镜空间边界与关系，避免无意义装饰。
- UI：一条从两端均可起亮的connection。用途：显现可选行动、输入归属与当前限制。
- Text：无；无。
- Character：Kris；原创程序化轮廓study；最终美术未验收。
- SOUL：停于一端，线从另一端亮一次；指示同一输入入口的空间位置，不裁定灵魂本体身份。
- In：承接DR65：章框变回一条连接；Out：线退成最后问题的baseline。
- Colour：#070A14, #E7E9F2, #F04462, #75A58B；Motion：5004–5015Kris手显；5016–5027两向各亮一半；5028以后hold；Effects：仅接触点窄glow、低强scanline；冲突段可路线触发glitch，不能遮心/手/选项。
- 复用：film/tui_pv_world_execute_20260926/continuity_full_v2/v2.py: HARD_CUT integer4970 (timing reuse)。保留/替换：KEEP分层/读区；ADAPT pane/载体；REPLACE原DSH/模型视觉；REMOVE本片舞者。
- 新代码：dr_layers.chapter_boundary, dr_layers.final_question, s_dr_final.shot_dr66（此处是实现计划，并非已经实现）。
- 技术：PIL/RGBA；直接复用font；旧monkey patch为零；section计划路径 film/deltarune/s_dr_final.py。HTML不必需；原创透明角色/布景预渲染可选。
- PoC：film/deltarune_poc/renderer.py；selected mechanism study; not full shot fidelity。
- Asset：Kris原创轮廓与该镜几何场景；study可程序化；生产美术与游戏画面核对待完成。
- 待问/限制：不写execute(player)为真实游戏函数。
- Still QA：[5004, 5010, 5027, 5050]；关键事件：['K11']。

### DR67 — 谁在执行谁

- 范围：5051–5086 exclusive；210.458333–211.916667s。
- 音乐：尾段保持至片尾；line IDs []。详细word/frame锚点保存在JSON，不复制歌词。
- Chapter/Route：1–5 / author synthesis；证据 E01 E04 E18 E33 E35 E36。
- 叙述目的：让问题落在保留的角色/输入上。
- Player：可继续等待或离开，不能提供未发布的下一章；Kris：主体被留在边界内，未来未知；他者：他者不接管最后主体地位；Story：Chapter/route接口接住越界；Story是作者隐喻。
- Camera/Layout：black；全黑；仅保留一个中央边界/问题及低亮Kris手；无ticker、无词带假唱词。
- Foreground：Kris手与红心均留，问题不遮主体。用途：把主体动作/受输入的对象放在第一阅读层。
- Background：纯黑、最外框开口仍在。用途：提供该镜空间边界与关系，避免无意义装饰。
- UI：无ticker/虚构回复。用途：显现可选行动、输入归属与当前限制。
- Text：Who executes whom?（作者文字）；短菜单/名称或明确作者标记，非歌词/新增角色对白。
- Character：Kris；原创程序化轮廓study；最终美术未验收。
- SOUL：稳定红心，未发送/未作下一章决定；指示同一输入入口的空间位置，不裁定灵魂本体身份。
- In：承接DR66：线退成最后问题的baseline；Out：片结束于5086 exclusive。
- Colour：#070A14, #E7E9F2, #F04462, #75A58B；Motion：5051–5056问题显；5057–5085hold，不闪烁不返黑；Effects：仅接触点窄glow、低强scanline；冲突段可路线触发glitch，不能遮心/手/选项。
- 复用：film/tui_pv_world_execute_20260926/continuity_full_v2/v2.py: HARD_CUT integer4970 (timing reuse)。保留/替换：KEEP分层/读区；ADAPT pane/载体；REPLACE原DSH/模型视觉；REMOVE本片舞者。
- 新代码：dr_layers.chapter_boundary, dr_layers.final_question, s_dr_final.shot_dr67（此处是实现计划，并非已经实现）。
- 技术：PIL/RGBA；直接复用font；旧monkey patch为零；section计划路径 film/deltarune/s_dr_final.py。HTML不必需；原创透明角色/布景预渲染可选。
- PoC：film/deltarune_poc/renderer.py；selected mechanism study; not full shot fidelity。
- Asset：Kris原创轮廓与该镜几何场景；study可程序化；生产美术与游戏画面核对待完成。
- 待问/限制：最后字不是Mili歌词也不是游戏对白。
- Still QA：[5051, 5057, 5068, 5085]；关键事件：['K11']。

## Frame-aware关键事件

这些是PV的导演帧；不冒充游戏实际tick。每个区间包含连续变化规则与hold，跨镜头保留同一个载体/心。

### K01 — identity_reassignment / DR06

| frame [a,b) | 连续行为 |
|---|---|
| 243–249 | vessel alpha=1-smooth((n-243)/6);心位置固定 |
| 249–255 | Kris alpha=smooth((n-249)/6);不创建第二颗SOUL |
| 255–269 | hold新主体，输入仍停空slot |

### K02 — SOUL_separation / DR34, DR35, DR36

| frame [a,b) | 连续行为 |
|---|---|
| 2644–2650 | 手移到胸口；SOUL仍inside |
| 2650–2656 | 同一心从胸→手沿线性x路径移12px |
| 2656–2662 | 手抬心越胸外边，connection alpha降到0 |
| 2662–2693 | 身体保持，心可移；无死亡/自由label |
| 2693–2718 | input只移动心；Kris世界位置不由该pulse决定 |

### K03 — control_reentry / DR42

| frame [a,b) | 连续行为 |
|---|---|
| 2928–2934 | 心由vent位置直接落choice物理槽，边界不断线 |
| 2934–2942 | SOUL沿房内路径移到胸前 |
| 2942–2948 | 胸口接触：原心缩到内部锚点，线亮，不生成新心 |
| 2948–2954 | hold已重入状态；Noelle手退，暖光减弱 |

### K04 — weird_lock_in / DR44

| frame [a,b) | 连续行为 |
|---|---|
| 3093–3102 | Kris手与Noelle腕图形接近但保留空隙 |
| 3102–3111 | red crack由接触点扩展；option分支收束 |
| 3111–3120 | lock线闭合，身体/选择层仍分离 |

### K05 — world_boundary_break / DR48

| frame [a,b) | 连续行为 |
|---|---|
| 3412–3424 | HERO越内框，载体在独立RGBA层不裁掉脚 |
| 3424–3436 | 外白框从角显现，主体Kris保持亮度 |
| 3436–3442 | hold外框与越界对象，拒绝glitch遮挡 |

### K06 — character_control_handoff / DR52

| frame [a,b) | 连续行为 |
|---|---|
| 3902–3908 | HERO脚在TV内；SOUL input连接仍到HERO |
| 3908–3914 | HERO carrier越白边，tv mask只裁背景 |
| 3914–3926 | Kris退6px并松controller；control保持HERO，绝不伪装Kris自主攻击 |

### K07 — refusal_and_other_intervention / DR53

| frame [a,b) | 连续行为 |
|---|---|
| 3988–3996 | HERO攻击线预示；Kris手先移 |
| 3996–4004 | Kris拉Susie横移24px，attack线落在原空位 |
| 4004–4012 | Susie断controller线；HERO透明度归零，心不灭 |

### K08 — player_story_reversal / DR57, DR58

| frame [a,b) | 连续行为 |
|---|---|
| 4418–4430 | Stop仍可读，心选中；世界仍向湖方向前进；留拒绝小痕迹 |
| 4430–4436 | hold二种文字，框不变 |
| 4436–4442 | 左文字缩短/清除6帧；心与Kris不换位置 |
| 4442–4448 | 左字出现Proceed；两项同文，无假Stop出口 |
| 4448–4460 | 心从左至右smooth移位；Kris身体移动量与两位置无关 |
| 4460–4519 | hold同结果；frame4495作为情绪peak，手仍迟疑 |

### K09 — cease_input_alternative / DR59, DR60

| frame [a,b) | 连续行为 |
|---|---|
| 4519–4531 | 原pulse停止，不把SOUL物理删除 |
| 4531–4543 | 灰线显示续章出口，Susie关切影子留下 |
| 4543–4574 | 两出口留白；不称事件没发生 |
| 4574–4601 | 返回继续侧一次收框/confirm，另一出口仍有后果影子 |
| 4601–4610 | 后一确认更短；仅为PV压缩，并非全部game timeout单调 |

### K10 — final_hard_cut / DR64, DR65

| frame [a,b) | 连续行为 |
|---|---|
| 4929–4935 | 最后歌起音亮外框；不是增加一次杀敌 |
| 4935–4962 | Kris手/心hold，看清边界 |
| 4962–4970 | 画布world高度按clamp((4969-n)/7)收缩，4969保留1px横线 |
| 4970–4982 | 全部黑12帧，无DSH chime |
| 4982–4994 | 章要求短文本淡入 |
| 4994–5004 | hold未来空位，不开下一章 |

### K11 — final_question / DR66, DR67

| frame [a,b) | 连续行为 |
|---|---|
| 5004–5016 | Kris手低亮显现，心从点回几何形 |
| 5016–5028 | connection两端各亮一半；不出现方向终判 |
| 5028–5051 | hold两者，保留最外框开口 |
| 5051–5057 | 作者问题淡入 |
| 5057–5086 | hold29帧；结束不判角色生死/未来路线 |

## 全片审查

情绪：连接/合作→身份/规则→亲密落空→能力/自主→分离→越界/反冲→重复执行→他者反向索求→边界/开放问题。器乐段09–12、46–48、61–63各有独立动作目标，不用‘蒙太奇’填空。

信息密度：身份/私话/锁定/选项反转处每镜最多两组短字；短‘离开’镜头只做一项拆层，35–39必须用连续心/手而非换角色图。12次执行用共同场景与留痕，不做12张杀敌flash。

重复motif：02框→38 cage→48外框→62 chapter框；12 SAVE→28身份卡；18内屏→52出屏；57拒绝→58同文→59停输入。Normal友情/能力多次回访，不靠Weird高潮支撑整首。

Chapter采用主题重访：1建立、2镜子/施压、3套层/越界、4私话/反冲、5反向索求/章节。Kris从开头揭露后每镜有身体/手/锚点，其他角色不能接管结尾；开头vessel段是主体选择被收回的必要例外。

Normal/Weird并非各50%硬配比。全部route标签、区间与统计可由validate脚本查看；交叉镜头明确标记，不合并成游戏连续事件。末段保留停止输入反证，避免Player单一邪恶或必然无自由。

开放验收：R01–03游戏画面；指定自备音频的对齐/听音；原创角色美术；短range节奏。完整覆盖与数据通过不等于PV已叙事/视觉验收，不能据此标goal complete。
