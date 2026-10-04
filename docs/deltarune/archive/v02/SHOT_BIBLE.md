# 211.9秒 Shot Bible v0.2

39镜导演重写；5086帧/24fps。source of truth：tools/design_deltarune_plan.py；JSON保留395个原word锚点，不提交歌词。v01已归档，DR编号只出现在legacy字段，不是当前shot或旧ALL index。

AUDIO REVIEW PENDING。CANON事实与原创blocking/主题cut分开，R01–03和production art未验收。镜头数量减少不是简化为静态图：每镜有运动与转场意图。

## 预算与连续时间线

预算：{'SUPPORT': 15, 'HERO': 12, 'BREATH': 8, 'TRANSITION': 4}。HERO成本集中在动作/空间；BREATH主动减少UI。

| shot / budget | frames [a,b) | seconds | title | legacy | evidence |
|---|---|---|---|---|---|
| PV01 / SUPPORT | 0–130 | 0.000–5.417 | 输入先到来 | DR01/DR02/DR03/DR04 | E01 |
| PV02 / HERO | 130–306 | 5.417–12.750 | 世界已有其人 | DR06/DR07 | E01 |
| PV03 / SUPPORT | 306–476 | 12.750–19.833 | 行动可以帮助 | DR08/DR09 | E03 |
| PV04 / SUPPORT | 476–567 | 19.833–23.625 | 她有自己的方向 | DR10 | E03 |
| PV05 / HERO | 567–715 | 23.625–29.792 | 愿意同行 | DR11 | E03 |
| PV06 / SUPPORT | 715–890 | 29.792–37.083 | 身体不是参数表 | DR13/DR14 | E01/E21 |
| PV07 / SUPPORT | 890–1066 | 37.083–44.417 | 已有的能力 | DR15 | E21 |
| PV08 / SUPPORT | 1066–1235 | 44.417–51.458 | 屏幕里面还有行动 | DR17/DR18 | E13/E15 |
| PV09 / BREATH | 1235–1417 | 51.458–59.042 | 共同世界的停留 | DR20 | E03 |
| PV10 / SUPPORT | 1417–1591 | 59.042–66.292 | 最后一根支撑 | DR21/DR22 | E06/E07 |
| PV11 / HERO | 1591–1774 | 66.292–73.917 | 落空后留下手 | DR24 | E06/E07 |
| PV12 / SUPPORT | 1774–1951 | 73.917–81.292 | 会给予的身体 | DR25 | E21 |
| PV13 / BREATH | 1951–2043 | 81.292–85.125 | 回应属于关系 | DR27 | E03 |
| PV14 / SUPPORT | 2043–2205 | 85.125–91.875 | 名字写入而身体留下 | DR12/DR28 | E02 |
| PV15 / TRANSITION | 2205–2382 | 91.875–99.250 | 同一个人穿过光 | DR29/DR30 | E01 |
| PV16 / SUPPORT | 2382–2571 | 99.250–107.125 | 合拍也有重量 | DR32/DR33 | E03/E21 |
| PV17 / HERO | 2571–2693 | 107.125–112.208 | 第一次身体与心分开 | DR34/DR35 | E04 |
| PV18 / BREATH | 2693–2838 | 112.208–118.250 | 输入仍在，身体走开 | DR36/DR37/DR38/DR39/DR40 | E04/E20 |
| PV19 / BREATH | 2838–2928 | 118.250–122.000 | 门内不是命令窗口 | DR41 | E20/E23 |
| PV20 / HERO | 2928–3014 | 122.000–125.583 | 菜单闯进私人空间 | DR42 | E24 |
| PV21 / SUPPORT | 3014–3093 | 125.583–128.875 | 有力量仍需走规定的路 | DR43 | E08/E24 |
| PV22 / HERO | 3093–3232 | 128.875–134.667 | 接触的代价回到身体 | DR44/DR45 | E26 |
| PV23 / SUPPORT | 3232–3323 | 134.667–138.458 | 身体倒下，命令继续 | DR46 | E09/E12 |
| PV24 / SUPPORT | 3323–3549 | 138.458–147.875 | 内世界抵住方向 | DR47/DR48 | E15/E16 |
| PV25 / HERO | 3549–3821 | 147.875–159.208 | 十二次命令改变空间 | DR49/DR50 | E08/E10 |
| PV26 / TRANSITION | 3821–3902 | 159.208–162.583 | 摄影机将跟错对象 | DR51 | E11/E18 |
| PV27 / HERO | 3902–3988 | 162.583–166.167 | 控制对象走出屏幕 | DR52 | E18 |
| PV28 / HERO | 3988–4072 | 166.167–169.667 | Kris把她拉开 | DR53 | E19 |
| PV29 / BREATH | 4072–4164 | 169.667–173.500 | 回来却没有字 | DR54 | E27 |
| PV30 / SUPPORT | 4164–4259 | 173.500–177.458 | 手撑着慢慢起身 | DR55 | E31 |
| PV31 / HERO | 4259–4430 | 177.458–184.583 | 她把命令带进世界 | DR56/DR57 | E32/E33 |
| PV32 / HERO | 4430–4519 | 184.583–188.292 | 位置变了，手仍被带着 | DR58 | E33/E34 |
| PV33 / BREATH | 4519–4574 | 188.292–190.583 | 停止到来的输入 | DR59 | E34/E36 |
| PV34 / TRANSITION | 4574–4654 | 190.583–193.917 | 继续重新组织了控制 | DR60 | E32/E34/E36 |
| PV35 / HERO | 4654–4863 | 193.917–202.625 | 连观察的位置也是屏幕 | DR61/DR62 | E13/E35 |
| PV36 / BREATH | 4863–4929 | 202.625–205.375 | 最后仍是一个人 | DR63 | E04/E36 |
| PV37 / TRANSITION | 4929–4970 | 205.375–207.083 | 最后一次接点 | DR64 | E35 |
| PV38 / SUPPORT | 4970–5030 | 207.083–209.583 | 沉默以后仍被要求继续 | DR65 | E35 |
| PV39 / BREATH | 5030–5086 | 209.583–211.917 | 谁在执行谁 | DR66/DR67 | E01/E04/E18/E33/E35/E36 |

## 逐镜导演与实现
 
### PV01 — 输入先到来 / SUPPORT

- 时间：[0,130)；0.000000–5.416667s；legacy ['DR01', 'DR02', 'DR03', 'DR04']。
- Song cue：供电/形体的组装；line IDs [0, 1, 2]；所有word/frame锚点在JSON。
- Chapter/Route：1 / opening；E E01；原创导演staging/主题剪接；非游戏连续录像或新增canon。
- 必要性：只建立心与临时主体，首次观看不背部件表。
- Player：输入先能选择临时形体；Kris：尚未揭露，不等同vessel；Other：尚未出现；Story：创建流程可收回提供的主体。
- Camera / spatial novelty：中心暗场，SOUL中心640,330；一个vessel姿态，不建三栏UI。
- Foreground：一点到红心、灰vessel合拢手势；理由：只建立心与临时主体，首次观看不背部件表。
- Background：暗场中的一组开口保护角；理由：建立身体动作的可达空间/距离；不是抽象信息图。
- UI：小的接受位置，无三栏/双姓名；Text：ACCEPT；短词/名字或明确作者问题；非歌词/新增角色对白。
- Character：Kris（PV01尚未揭露），original geometric rough blocking; production art pending；SOUL：始终同一红心。
- 连续动作：0–8点亮；8–93部件慢合；93–129心停于接受位置；动作少而留hold。
- In：黑场一点显；Out：灰部件退，绿色身体占住同一视觉锚点。
- Colour：['#070A14', '#75A58B', '#C7E4EC', '#F04462']；Effects：少量接触光/水纹；拒绝靠generic glitch提升预算；纯黑区无后期残影。
- 复用：film/tui_pv_world_execute_20260926/tuikit.py:font / film/tui_pv_world_execute_20260926/continuity_full_v2/cuts.py:independent carrier/mask principle (design reuse)；KEEP整数timing/分层；REPLACE静态左右pane与哲学分支图；REMOVE常驻ticker/舞者。
- 实现：film/deltarune_poc/scenes.py:vessel / film/deltarune_poc/stage.py:posed_characters / film/deltarune_poc/renderer.py:frame；PIL，零旧monkey patch；HTML不必需；生产原创透明asset可后替换。
- 素材：rough geometry; game visual R01–03 / production art pending；仍待：vessel形状是原创概括；不写官方完整opening对白。
- QA frames：[0, 12, 65, 129]；关键事件：[]。

### PV02 — 世界已有其人 / HERO

- 时间：[130,306)；5.416667–12.750000s；legacy ['DR06', 'DR07']。
- Song cue：接受/参数/启动；line IDs [3, 4, 5, 6]；所有word/frame锚点在JSON。
- Chapter/Route：1 / opening → normal；E E01；原创导演staging/主题剪接；非游戏连续录像或新增canon。
- 必要性：选择被收回，但Kris很早成为可识别主体。
- Player：主体选择被收回，仍有行动输入；Kris：Kris已有身份/身体，不由表格创生；Other：世界已有关系；Story：被实现的开场限定主体。
- Camera / spatial novelty：Kris从640,540中景显露；镜头从vessel位置接近身体，不再左pane肖像。
- Foreground：Kris遮眼头、绿色衣带、自己的手；理由：选择被收回，但Kris很早成为可识别主体。
- Background：卧室门与一束窗光，原vessel槽成为空位；理由：建立身体动作的可达空间/距离；不是抽象信息图。
- UI：接受位置消失，不追加name表；Text：KRIS；短词/名字或明确作者问题；非歌词/新增角色对白。
- Character：Kris，original geometric rough blocking; production art pending；SOUL：由接受位置靠近胸但不宣称本体身份。
- 连续动作：130–142灰vessel退；142–156Kris显；156–243缓推身体；243–305窗光/手先动而非表格。
- In：灰部件退，绿色身体占住同一视觉锚点；Out：门光落到可走的地面。
- Colour：['#070A14', '#75A58B', '#C7E4EC', '#F04462']；Effects：少量接触光/水纹；拒绝靠generic glitch提升预算；纯黑区无后期残影。
- 复用：film/tui_pv_world_execute_20260926/tuikit.py:font / film/tui_pv_world_execute_20260926/continuity_full_v2/cuts.py:independent carrier/mask principle (design reuse)；KEEP整数timing/分层；REPLACE静态左右pane与哲学分支图；REMOVE常驻ticker/舞者。
- 实现：film/deltarune_poc/scenes.py:arrival / film/deltarune_poc/stage.py:posed_characters / film/deltarune_poc/renderer.py:frame；PIL，零旧monkey patch；HTML不必需；生产原创透明asset可后替换。
- 素材：rough geometry; game visual R01–03 / production art pending；仍待：提前剪接是导演节奏，不改游戏opening事实顺序。
- QA frames：[130, 142, 218, 305]；关键事件：['K01']。

### PV03 — 行动可以帮助 / SUPPORT

- 时间：[306,476)；12.750000–19.833333s；legacy ['DR08', 'DR09']。
- Song cue：开始行动/器乐建立；line IDs [7]；所有word/frame锚点在JSON。
- Chapter/Route：1 / normal；E E03；原创导演staging/主题剪接；非游戏连续录像或新增canon。
- 必要性：先让输入帮助同行，后面的控制才有关系重量。
- Player：输入可帮助，但不能规定所有回应；Kris：技能/气质在共同动作中存在；Other：拒绝或主动合作；Story：有限菜单不消灭日常关系。
- Camera / spatial novelty：宽景地面，Kris约460,540/Susie约860,540；输入小而动作轨迹大。
- Foreground：Kris跨过地面间隙，Susie在同一世界；理由：先让输入帮助同行，后面的控制才有关系重量。
- Background：两块暖地形与可走路径；理由：建立身体动作的可达空间/距离；不是抽象信息图。
- UI：小方向pulse只在动作之前出现；Text：无；无。
- Character：Kris，original geometric rough blocking; production art pending；SOUL：胸/行动接口亮一次即可。
- 连续动作：306–385输入→Kris一步；385–432步幅跨缺口；432–475同地面停住，Susie另走半步。
- In：门光落到可走的地面；Out：Susie突然选择自己的方向。
- Colour：['#070A14', '#75A58B', '#D5BE8A', '#F04462']；Effects：少量接触光/水纹；拒绝靠generic glitch提升预算；纯黑区无后期残影。
- 复用：film/tui_pv_world_execute_20260926/tuikit.py:font / film/tui_pv_world_execute_20260926/continuity_full_v2/cuts.py:independent carrier/mask principle (design reuse)；KEEP整数timing/分层；REPLACE静态左右pane与哲学分支图；REMOVE常驻ticker/舞者。
- 实现：film/deltarune_poc/scenes.py:help_path / film/deltarune_poc/stage.py:posed_characters / film/deltarune_poc/renderer.py:frame；PIL，零旧monkey patch；HTML不必需；生产原创透明asset可后替换。
- 素材：rough geometry; game visual R01–03 / production art pending；仍待：原创blocking概括合作，不假造新剧情/输入延迟。
- QA frames：[306, 318, 391, 475]；关键事件：[]。

### PV04 — 她有自己的方向 / SUPPORT

- 时间：[476,567)；19.833333–23.625000s；legacy ['DR10']。
- Song cue：器乐重拍；line IDs []；所有word/frame锚点在JSON。
- Chapter/Route：1 / normal；E E03；原创导演staging/主题剪接；非游戏连续录像或新增canon。
- 必要性：他者的拒绝用偏离队形读出，不贴refusal说明。
- Player：输入可帮助，但不能规定所有回应；Kris：技能/气质在共同动作中存在；Other：拒绝或主动合作；Story：有限菜单不消灭日常关系。
- Camera / spatial novelty：同一地面，Susie横向离队；camera留Kris，不追攻击对象。
- Foreground：Kris停、Susie独自前冲；理由：他者的拒绝用偏离队形读出，不贴refusal说明。
- Background：刚建立的共同地面还在；理由：建立身体动作的可达空间/距离；不是抽象信息图。
- UI：小命令格闪一次后退灰；Text：无；无。
- Character：Kris，original geometric rough blocking; production art pending；SOUL：仍留Kris位置，不追Susie。
- 连续动作：476–500Susie准备；500–535向另一方向行动；535–566Kris留原位看她，camera不追。
- In：Susie突然选择自己的方向；Out：Susie回望，主动靠回。
- Colour：['#070A14', '#75A58B', '#D5BE8A', '#F04462']；Effects：少量接触光/水纹；拒绝靠generic glitch提升预算；纯黑区无后期残影。
- 复用：film/tui_pv_world_execute_20260926/tuikit.py:font / film/tui_pv_world_execute_20260926/continuity_full_v2/cuts.py:independent carrier/mask principle (design reuse)；KEEP整数timing/分层；REPLACE静态左右pane与哲学分支图；REMOVE常驻ticker/舞者。
- 实现：film/deltarune_poc/scenes.py:refusal / film/deltarune_poc/stage.py:posed_characters / film/deltarune_poc/renderer.py:frame；PIL，零旧monkey patch；HTML不必需；生产原创透明asset可后替换。
- 素材：rough geometry; game visual R01–03 / production art pending；仍待：不宣称Susie永远不可指挥。
- QA frames：[476, 488, 521, 566]；关键事件：[]。

### PV05 — 愿意同行 / HERO

- 时间：[567,715)；23.625000–29.791667s；legacy ['DR11']。
- Song cue：器乐回收；line IDs [9]；所有word/frame锚点在JSON。
- Chapter/Route：1 / 3 / normal / author staging；E E03；原创导演staging/主题剪接；非游戏连续录像或新增canon。
- 必要性：温暖关系成为后半会失去的东西。
- Player：输入可帮助，但不能规定所有回应；Kris：技能/气质在共同动作中存在；Other：拒绝或主动合作；Story：有限菜单不消灭日常关系。
- Camera / spatial novelty：两角色中近景，手回到共同地面；少UI，让身位靠近可读。
- Foreground：Kris与Susie的手、各自完整身体；理由：温暖关系成为后半会失去的东西。
- Background：低地平线与暖反光；理由：建立身体动作的可达空间/距离；不是抽象信息图。
- UI：menu退场，动作先于框；Text：无；无。
- Character：Kris，original geometric rough blocking; production art pending；SOUL：低亮留接口，不制造第二颗心。
- 连续动作：567–615Susie回到同地面；615–655伸手回应；655–714两人停留而非又加SAVE概念。
- In：Susie回望，主动靠回；Out：共同地面渐成斜投影。
- Colour：['#070A14', '#75A58B', '#D5BE8A', '#F04462']；Effects：少量接触光/水纹；拒绝靠generic glitch提升预算；纯黑区无后期残影。
- 复用：film/tui_pv_world_execute_20260926/tuikit.py:font / film/tui_pv_world_execute_20260926/continuity_full_v2/cuts.py:independent carrier/mask principle (design reuse)；KEEP整数timing/分层；REPLACE静态左右pane与哲学分支图；REMOVE常驻ticker/舞者。
- 实现：film/deltarune_poc/scenes.py:welcome / film/deltarune_poc/stage.py:posed_characters / film/deltarune_poc/renderer.py:frame；PIL，零旧monkey patch；HTML不必需；生产原创透明asset可后替换。
- 素材：rough geometry; game visual R01–03 / production art pending；仍待：手势是作者合作比喻，不新增canon握手对白。
- QA frames：[567, 579, 641, 714]；关键事件：[]。

### PV06 — 身体不是参数表 / SUPPORT

- 时间：[715,890)；29.791667–37.083333s；legacy ['DR13', 'DR14']。
- Song cue：点/几何定义；line IDs [9, 10, 11, 12]；所有word/frame锚点在JSON。
- Chapter/Route：1 / 4 / normal / author metaphor；E E01 E21；原创导演staging/主题剪接；非游戏连续录像或新增canon。
- 必要性：保留数学趣味但让身体先于定义，删同结果菜单预告。
- Player：输入可帮助，但不能规定所有回应；Kris：技能/气质在共同动作中存在；Other：拒绝或主动合作；Story：有限菜单不消灭日常关系。
- Camera / spatial novelty：斜光中的身体，地面点/弧是投影而非常驻choice圆。
- Foreground：Kris手和身体、少量点投影；理由：保留数学趣味但让身体先于定义，删同结果菜单预告。
- Background：斜光/地面弧，不是choice环；理由：建立身体动作的可达空间/距离；不是抽象信息图。
- UI：无常驻圆菜单；Text：无；无。
- Character：Kris，original geometric rough blocking; production art pending；SOUL：保持身体锚点。
- 连续动作：715–803点从脚边聚合；803–889投影环从地面滑过，身体不被切成数据。
- In：共同地面渐成斜投影；Out：点距变成前景键格。
- Colour：['#070A14', '#75A58B', '#D5BE8A', '#F04462']；Effects：少量接触光/水纹；拒绝靠generic glitch提升预算；纯黑区无后期残影。
- 复用：film/tui_pv_world_execute_20260926/tuikit.py:font / film/tui_pv_world_execute_20260926/continuity_full_v2/cuts.py:independent carrier/mask principle (design reuse)；KEEP整数timing/分层；REPLACE静态左右pane与哲学分支图；REMOVE常驻ticker/舞者。
- 实现：film/deltarune_poc/scenes.py:body_projection / film/deltarune_poc/stage.py:posed_characters / film/deltarune_poc/renderer.py:frame；PIL，零旧monkey patch；HTML不必需；生产原创透明asset可后替换。
- 素材：rough geometry; game visual R01–03 / production art pending；仍待：点/弧是作者视觉，不对人物能力下数学定义。
- QA frames：[715, 727, 802, 889]；关键事件：[]。

### PV07 — 已有的能力 / SUPPORT

- 时间：[890,1066)；37.083333–44.416667s；legacy ['DR15']。
- Song cue：波/可接触轨道/限制；line IDs [13, 14, 15, 16, 17]；所有word/frame锚点在JSON。
- Chapter/Route：4 / normal；E E21；原创导演staging/主题剪接；非游戏连续录像或新增canon。
- 必要性：普通输入也能与Kris的能力共同作用。
- Player：输入可帮助，但不能规定所有回应；Kris：技能/气质在共同动作中存在；Other：拒绝或主动合作；Story：有限菜单不消灭日常关系。
- Camera / spatial novelty：45度键盘前景，Kris手在近处；地平线/键格关联，非数学字幕。
- Foreground：键盘与Kris手的两次动作；理由：普通输入也能与Kris的能力共同作用。
- Background：暖暗室、稀疏乐纹；理由：建立身体动作的可达空间/距离；不是抽象信息图。
- UI：方向点很小，不占半屏；Text：无；无。
- Character：Kris，original geometric rough blocking; production art pending；SOUL：胸前稳定，手在世界前景。
- 连续动作：890–980手落键；980–1030两键相继按下；1030–1065持手/听波纹，不撞新白框。
- In：点距变成前景键格；Out：键盘角match到controller手。
- Colour：['#070A14', '#75A58B', '#D5BE8A', '#F04462']；Effects：少量接触光/水纹；拒绝靠generic glitch提升预算；纯黑区无后期残影。
- 复用：film/tui_pv_world_execute_20260926/tuikit.py:font / film/tui_pv_world_execute_20260926/continuity_full_v2/cuts.py:independent carrier/mask principle (design reuse)；KEEP整数timing/分层；REPLACE静态左右pane与哲学分支图；REMOVE常驻ticker/舞者。
- 实现：film/deltarune_poc/scenes.py:organ_intro / film/deltarune_poc/stage.py:posed_characters / film/deltarune_poc/renderer.py:frame；PIL，零旧monkey patch；HTML不必需；生产原创透明asset可后替换。
- 素材：rough geometry; game visual R01–03 / production art pending；仍待：没有音频，只用现有唱词timing，奏乐不是实际乐谱复刻。
- QA frames：[890, 902, 978, 1065]；关键事件：[]。

### PV08 — 屏幕里面还有行动 / SUPPORT

- 时间：[1066,1235)；44.416667–51.458333s；legacy ['DR17', 'DR18']。
- Song cue：电流/视角受限；line IDs [17, 18, 19, 20, 21]；所有word/frame锚点在JSON。
- Chapter/Route：3 / common / sword foreshadow；E E13 E15；原创导演staging/主题剪接；非游戏连续录像或新增canon。
- 必要性：一次建立后面会被穿透的实体屏幕平面。
- Player：controller/小游戏仍受舞台条件；Kris：主体在外层，对输入有身体反应；Other：角色可介入；Story：内外屏幕是实际可见通道。
- Camera / spatial novelty：Kris背/手在左前景，实体TV在右；一次建立内外屏幕平面。
- Foreground：Kris背/握controller的手，内HERO；理由：一次建立后面会被穿透的实体屏幕平面。
- Background：带厚度的TV与地面；理由：建立身体动作的可达空间/距离；不是抽象信息图。
- UI：控制接点在屏幕内，非三层解释图；Text：无；无。
- Character：Kris，original geometric rough blocking; production art pending；SOUL：输入到内游戏对象的路径短显。
- 连续动作：1066–1145手/TV依次亮；1145–1190内角色向边走；1190–1234边阻住但外身体仍在。
- In：键盘角match到controller手；Out：TV暖光淡到party地面。
- Colour：['#070A14', '#75A58B', '#C7E4EC', '#F04462']；Effects：少量接触光/水纹；拒绝靠generic glitch提升预算；纯黑区无后期残影。
- 复用：film/tui_pv_world_execute_20260926/tuikit.py:font / film/tui_pv_world_execute_20260926/continuity_full_v2/cuts.py:independent carrier/mask principle (design reuse)；KEEP整数timing/分层；REPLACE静态左右pane与哲学分支图；REMOVE常驻ticker/舞者。
- 实现：film/deltarune_poc/scenes.py:tv_intro / film/deltarune_poc/stage.py:posed_characters / film/deltarune_poc/renderer.py:frame；PIL，零旧monkey patch；HTML不必需；生产原创透明asset可后替换。
- 素材：rough geometry; game visual R01–03 / production art pending；仍待：不复刻未经R01核对的具体原地图。
- QA frames：[1066, 1078, 1150, 1234]；关键事件：[]。

### PV09 — 共同世界的停留 / BREATH

- 时间：[1235,1417)；51.458333–59.041667s；legacy ['DR20']。
- Song cue：时空可能/深度结合；line IDs [21, 22, 23, 24]；所有word/frame锚点在JSON。
- Chapter/Route：1 / 3 / normal / thematic crosscut；E E03；原创导演staging/主题剪接；非游戏连续录像或新增canon。
- 必要性：给关系呼吸，不把合作再解释成双向线。
- Player：输入可帮助，但不能规定所有回应；Kris：技能/气质在共同动作中存在；Other：拒绝或主动合作；Story：有限菜单不消灭日常关系。
- Camera / spatial novelty：宽景三人同路，UI退出；地平线低，缓慢横向tracking。
- Foreground：Kris主体，Susie/Ralsei各留一身间距；理由：给关系呼吸，不把合作再解释成双向线。
- Background：宽地面与暖远光；理由：建立身体动作的可达空间/距离；不是抽象信息图。
- UI：无；Text：无；无。
- Character：Kris，original geometric rough blocking; production art pending；SOUL：不抢视线，只留低亮锚点。
- 连续动作：1235–1322慢tracking同路；1322–1416脚步停下、肩/呼吸继续；不逐词加动作。
- In：TV暖光淡到party地面；Out：远光落在一根悬吊线上。
- Colour：['#070A14', '#75A58B', '#D5BE8A', '#F04462']；Effects：少量接触光/水纹；拒绝靠generic glitch提升预算；纯黑区无后期残影。
- 复用：film/tui_pv_world_execute_20260926/tuikit.py:font / film/tui_pv_world_execute_20260926/continuity_full_v2/cuts.py:independent carrier/mask principle (design reuse)；KEEP整数timing/分层；REPLACE静态左右pane与哲学分支图；REMOVE常驻ticker/舞者。
- 实现：film/deltarune_poc/scenes.py:party_breath / film/deltarune_poc/stage.py:posed_characters / film/deltarune_poc/renderer.py:frame；PIL，零旧monkey patch；HTML不必需；生产原创透明asset可后替换。
- 素材：rough geometry; game visual R01–03 / production art pending；仍待：Ralsei不成为管理员/全知解释者。
- QA frames：[1235, 1247, 1326, 1416]；关键事件：[]。

### PV10 — 最后一根支撑 / SUPPORT

- 时间：[1417,1591)；59.041667–66.291667s；legacy ['DR21', 'DR22']。
- Song cue：提供可能/满足的条件；line IDs [25, 26, 27, 28, 29]；所有word/frame锚点在JSON。
- Chapter/Route：2 / normal；E E06 E07；原创导演staging/主题剪接；非游戏连续录像或新增canon。
- 必要性：观众先期待切线能帮助，结果才会有落差。
- Player：输入可帮助，但不能规定所有回应；Kris：技能/气质在共同动作中存在；Other：拒绝或主动合作；Story：有限菜单不消灭日常关系。
- Camera / spatial novelty：低位手/单线/悬吊轮廓，抬视线；最后线留hold，不三候选菜单。
- Foreground：Kris伸手与悬吊轮廓/一根线；理由：观众先期待切线能帮助，结果才会有落差。
- Background：宽暗地面和上方支撑点；理由：建立身体动作的可达空间/距离；不是抽象信息图。
- UI：只一个确认位置；Text：无；无。
- Character：Kris，original geometric rough blocking; production art pending；SOUL：在确认接点，保持一个主要心。
- 连续动作：1417–1513线仍支撑轮廓；1513–1578手接近、hold；1578–1590接点释放。
- In：远光落在一根悬吊线上；Out：切后身体坠落，camera不庆祝。
- Colour：['#070A14', '#75A58B', '#D5BE8A', '#F04462']；Effects：少量接触光/水纹；拒绝靠generic glitch提升预算；纯黑区无后期残影。
- 复用：film/tui_pv_world_execute_20260926/tuikit.py:font / film/tui_pv_world_execute_20260926/continuity_full_v2/cuts.py:independent carrier/mask principle (design reuse)；KEEP整数timing/分层；REPLACE静态左右pane与哲学分支图；REMOVE常驻ticker/舞者。
- 实现：film/deltarune_poc/scenes.py:last_wire / film/deltarune_poc/stage.py:posed_characters / film/deltarune_poc/renderer.py:frame；PIL，零旧monkey patch；HTML不必需；生产原创透明asset可后替换。
- 素材：rough geometry; game visual R01–03 / production art pending；仍待：NEO只是关系镜子，不做boss介绍/胜利banner。
- QA frames：[1417, 1429, 1504, 1590]；关键事件：[]。

### PV11 — 落空后留下手 / HERO

- 时间：[1591,1774)；66.291667–73.916667s；legacy ['DR24']。
- Song cue：执行/仍然受困；line IDs [29, 30, 31, 32]；所有word/frame锚点在JSON。
- Chapter/Route：2 / normal；E E06 E07；原创导演staging/主题剪接；非游戏连续录像或新增canon。
- 必要性：动作成功和可行动不是一回事；让落空有余韵。
- Player：输入可帮助，但不能规定所有回应；Kris：技能/气质在共同动作中存在；Other：拒绝或主动合作；Story：有限菜单不消灭日常关系。
- Camera / spatial novelty：落下的轮廓与Kris手同框；线的空位保留，机位不追到底。
- Foreground：落下轮廓、Kris悬空未收回的手；理由：动作成功和可行动不是一回事；让落空有余韵。
- Background：断线空位保持，世界不消失；理由：建立身体动作的可达空间/距离；不是抽象信息图。
- UI：确认框撤出；Text：无；无。
- Character：Kris，original geometric rough blocking; production art pending；SOUL：停于刚按过的位置，不消灭接口。
- 连续动作：1591–1637小轮廓坠落；1637–1683空线轻摆；1683–1773Kris手留住，呼吸降强度。
- In：切后身体坠落，camera不庆祝；Out：空线摆动变成暖键格影。
- Colour：['#070A14', '#75A58B', '#D5BE8A', '#F04462']；Effects：少量接触光/水纹；拒绝靠generic glitch提升预算；纯黑区无后期残影。
- 复用：film/tui_pv_world_execute_20260926/tuikit.py:font / film/tui_pv_world_execute_20260926/continuity_full_v2/cuts.py:independent carrier/mask principle (design reuse)；KEEP整数timing/分层；REPLACE静态左右pane与哲学分支图；REMOVE常驻ticker/舞者。
- 实现：film/deltarune_poc/scenes.py:wire_fall / film/deltarune_poc/stage.py:posed_characters / film/deltarune_poc/renderer.py:frame；PIL，零旧monkey patch；HTML不必需；生产原创透明asset可后替换。
- 素材：rough geometry; game visual R01–03 / production art pending；仍待：不画角色死亡/全员解放，不提前演保护Susie。
- QA frames：[1591, 1603, 1682, 1773]；关键事件：[]。

### PV12 — 会给予的身体 / SUPPORT

- 时间：[1774,1951)；73.916667–81.291667s；legacy ['DR25']。
- Song cue：给予能力/保护；line IDs [33, 34, 35, 36, 37]；所有word/frame锚点在JSON。
- Chapter/Route：4 / normal；E E21；原创导演staging/主题剪接；非游戏连续录像或新增canon。
- 必要性：能力不是菜单制造的空壳；日常抵消恐怖的单一情绪。
- Player：输入可帮助，但不能规定所有回应；Kris：技能/气质在共同动作中存在；Other：拒绝或主动合作；Story：有限菜单不消灭日常关系。
- Camera / spatial novelty：暖房间，Kris手/肩的奏乐动作；不再把波形占满半屏。
- Foreground：Kris肩、手与前景键格；理由：能力不是菜单制造的空壳；日常抵消恐怖的单一情绪。
- Background：暖室/窗纹；理由：建立身体动作的可达空间/距离；不是抽象信息图。
- UI：可用输入轻亮后退出；Text：无；无。
- Character：Kris，original geometric rough blocking; production art pending；SOUL：胸口低亮，动作在世界中发生。
- 连续动作：1774–1865两次手/肩表演；1865–1950光从键面流向窗，身体保留而非变波形。
- In：空线摆动变成暖键格影；Out：窗光延长成街道。
- Colour：['#070A14', '#75A58B', '#D5BE8A', '#F04462']；Effects：少量接触光/水纹；拒绝靠generic glitch提升预算；纯黑区无后期残影。
- 复用：film/tui_pv_world_execute_20260926/tuikit.py:font / film/tui_pv_world_execute_20260926/continuity_full_v2/cuts.py:independent carrier/mask principle (design reuse)；KEEP整数timing/分层；REPLACE静态左右pane与哲学分支图；REMOVE常驻ticker/舞者。
- 实现：film/deltarune_poc/scenes.py:organ_care / film/deltarune_poc/stage.py:posed_characters / film/deltarune_poc/renderer.py:frame；PIL，零旧monkey patch；HTML不必需；生产原创透明asset可后替换。
- 素材：rough geometry; game visual R01–03 / production art pending；仍待：删前段balloon离体，保护110秒首次明确分离。
- QA frames：[1774, 1786, 1862, 1950]；关键事件：[]。

### PV13 — 回应属于关系 / BREATH

- 时间：[1951,2043)；81.291667–85.125000s；legacy ['DR27']。
- Song cue：让他者快乐/回应；line IDs [37, 38]；所有word/frame锚点在JSON。
- Chapter/Route：1 / 5 / normal / author staging；E E03；原创导演staging/主题剪接；非游戏连续录像或新增canon。
- 必要性：Susie也可回应Kris，关切需要在压力前熟悉。
- Player：输入可帮助，但不能规定所有回应；Kris：技能/气质在共同动作中存在；Other：拒绝或主动合作；Story：有限菜单不消灭日常关系。
- Camera / spatial novelty：街道中景，Susie回头，Kris衣色在同一地面；无SOUL离体预告。
- Foreground：Kris与回头的Susie；理由：Susie也可回应Kris，关切需要在压力前熟悉。
- Background：暖街道/同一地面，少线；理由：建立身体动作的可达空间/距离；不是抽象信息图。
- UI：无；Text：无；无。
- Character：Kris，original geometric rough blocking; production art pending；SOUL：很低亮仍可辨。
- 连续动作：1951–1991同行；1991–2042Susie回头/Kris衣袖轻动；不加love confession。
- In：窗光延长成街道；Out：两人影子间出现一次SAVE卡。
- Colour：['#070A14', '#75A58B', '#D5BE8A', '#F04462']；Effects：少量接触光/水纹；拒绝靠generic glitch提升预算；纯黑区无后期残影。
- 复用：film/tui_pv_world_execute_20260926/tuikit.py:font / film/tui_pv_world_execute_20260926/continuity_full_v2/cuts.py:independent carrier/mask principle (design reuse)；KEEP整数timing/分层；REPLACE静态左右pane与哲学分支图；REMOVE常驻ticker/舞者。
- 实现：film/deltarune_poc/scenes.py:friend_breath / film/deltarune_poc/stage.py:posed_characters / film/deltarune_poc/renderer.py:frame；PIL，零旧monkey patch；HTML不必需；生产原创透明asset可后替换。
- 素材：rough geometry; game visual R01–03 / production art pending；仍待：普通友情的作者概括，不冒充Ch5 balloon事件。
- QA frames：[1951, 1963, 1997, 2042]；关键事件：[]。

### PV14 — 名字写入而身体留下 / SUPPORT

- 时间：[2043,2205)；85.125000–91.875000s；legacy ['DR12', 'DR28']。
- Song cue：存在/身份；line IDs [39, 40, 41, 42]；所有word/frame锚点在JSON。
- Chapter/Route：1 / normal / thematic recall；E E02；原创导演staging/主题剪接；非游戏连续录像或新增canon。
- 必要性：SAVE名字只出现一次；有身体才不变哲学图表。
- Player：输入可帮助，但不能规定所有回应；Kris：技能/气质在共同动作中存在；Other：拒绝或主动合作；Story：有限菜单不消灭日常关系。
- Camera / spatial novelty：SAVE卡只遮身体小部分，Kris身形持续可见；只一次名字覆盖。
- Foreground：Kris衣色和手持续，单卡小范围覆盖；理由：SAVE名字只出现一次；有身体才不变哲学图表。
- Background：街道暗下但身体不消散；理由：建立身体动作的可达空间/距离；不是抽象信息图。
- UI：SAVE一slot，一次name覆盖；Text：KRIS / CREATOR；短词/名字或明确作者问题；非歌词/新增角色对白。
- Character：Kris，original geometric rough blocking; production art pending；SOUL：在保存位置，不把名字变成脸。
- 连续动作：2043–2080slot显；2080–2125名字覆盖；2125–2204卡退一半/身体继续呼吸。
- In：两人影子间出现一次SAVE卡；Out：卡白光变窗光边。
- Colour：['#070A14', '#75A58B', '#D5BE8A', '#F04462']；Effects：少量接触光/水纹；拒绝靠generic glitch提升预算；纯黑区无后期残影。
- 复用：film/tui_pv_world_execute_20260926/tuikit.py:font / film/tui_pv_world_execute_20260926/continuity_full_v2/cuts.py:independent carrier/mask principle (design reuse)；KEEP整数timing/分层；REPLACE静态左右pane与哲学分支图；REMOVE常驻ticker/舞者。
- 实现：film/deltarune_poc/scenes.py:save_identity / film/deltarune_poc/stage.py:posed_characters / film/deltarune_poc/renderer.py:frame；PIL，零旧monkey patch；HTML不必需；生产原创透明asset可后替换。
- 素材：rough geometry; game visual R01–03 / production art pending；仍待：不虚构输入者名字或多周目全角色记忆。
- QA frames：[2043, 2055, 2124, 2204]；关键事件：[]。

### PV15 — 同一个人穿过光 / TRANSITION

- 时间：[2205,2382)；91.875000–99.250000s；legacy ['DR29', 'DR30']。
- Song cue：日夜/身份情境；line IDs [43, 44, 45, 46]；所有word/frame锚点在JSON。
- Chapter/Route：1 / 2 / normal / author metaphor；E E01；原创导演staging/主题剪接；非游戏连续录像或新增canon。
- 必要性：舞台变化不能更改Kris身份；不第二次套TV。
- Player：输入可帮助，但不能规定所有回应；Kris：技能/气质在共同动作中存在；Other：拒绝或主动合作；Story：有限菜单不消灭日常关系。
- Camera / spatial novelty：相同身体横移穿过光/暗色域，窗帘边作match，非属性切换卡。
- Foreground：同一遮眼头/衣袖，拉帘的手；理由：舞台变化不能更改Kris身份；不第二次套TV。
- Background：Light暖色→Dark靛蓝，一次色域变化；理由：建立身体动作的可达空间/距离；不是抽象信息图。
- UI：无属性卡或gender项；Text：无；无。
- Character：Kris，original geometric rough blocking; production art pending；SOUL：身体锚点不断，不提前藏心。
- 连续动作：2205–2295手拉光边；2295–2381身体横越色域，环境变而身形连续。
- In：卡白光变窗光边；Out：暗光进入共同动作的近景。
- Colour：['#070A14', '#75A58B', '#D5BE8A', '#F04462']；Effects：少量接触光/水纹；拒绝靠generic glitch提升预算；纯黑区无后期残影。
- 复用：film/tui_pv_world_execute_20260926/tuikit.py:font / film/tui_pv_world_execute_20260926/continuity_full_v2/cuts.py:independent carrier/mask principle (design reuse)；KEEP整数timing/分层；REPLACE静态左右pane与哲学分支图；REMOVE常驻ticker/舞者。
- 实现：film/deltarune_poc/scenes.py:light_dark / film/deltarune_poc/stage.py:posed_characters / film/deltarune_poc/renderer.py:frame；PIL，零旧monkey patch；HTML不必需；生产原创透明asset可后替换。
- 素材：rough geometry; game visual R01–03 / production art pending；仍待：窗口动作是导演match，不声称某段自主剧情。
- QA frames：[2205, 2217, 2293, 2381]；关键事件：[]。

### PV16 — 合拍也有重量 / SUPPORT

- 时间：[2382,2571)；99.250000–107.125000s；legacy ['DR32', 'DR33']。
- Song cue：感应/共振；line IDs [47, 48, 49, 50]；所有word/frame锚点在JSON。
- Chapter/Route：1 / 4 / normal / thematic crosscut；E E03 E21；原创导演staging/主题剪接；非游戏连续录像或新增canon。
- 必要性：分离前留一次确实成立的合作，不能所有连接都负面。
- Player：输入可帮助，但不能规定所有回应；Kris：技能/气质在共同动作中存在；Other：拒绝或主动合作；Story：有限菜单不消灭日常关系。
- Camera / spatial novelty：手与party动作相合，缓慢靠近胸/肩，为下一镜留真实关系。
- Foreground：Kris手与伙伴回应动作；理由：分离前留一次确实成立的合作，不能所有连接都负面。
- Background：小暖光、不满屏光谱；理由：建立身体动作的可达空间/距离；不是抽象信息图。
- UI：menu弱退，不比较两种wave数据；Text：无；无。
- Character：Kris，original geometric rough blocking; production art pending；SOUL：胸前完整、不过度放大。
- 连续动作：2382–2485两种动作靠近；2485–2530相合一次；2530–2570在完整身体上hold。
- In：暗光进入共同动作的近景；Out：camera留在同一胸/手，暖光开始退。
- Colour：['#070A14', '#75A58B', '#D5BE8A', '#F04462']；Effects：少量接触光/水纹；拒绝靠generic glitch提升预算；纯黑区无后期残影。
- 复用：film/tui_pv_world_execute_20260926/tuikit.py:font / film/tui_pv_world_execute_20260926/continuity_full_v2/cuts.py:independent carrier/mask principle (design reuse)；KEEP整数timing/分层；REPLACE静态左右pane与哲学分支图；REMOVE常驻ticker/舞者。
- 实现：film/deltarune_poc/scenes.py:shared_rhythm / film/deltarune_poc/stage.py:posed_characters / film/deltarune_poc/renderer.py:frame；PIL，零旧monkey patch；HTML不必需；生产原创透明asset可后替换。
- 素材：rough geometry; game visual R01–03 / production art pending；仍待：相合是作者表演，不当精确输入时延事实。
- QA frames：[2382, 2394, 2476, 2570]；关键事件：[]。

### PV17 — 第一次身体与心分开 / HERO

- 时间：[2571,2693)；107.125000–112.208333s；legacy ['DR34', 'DR35']。
- Song cue：完成→离开；line IDs [51, 52, 53, 54]；所有word/frame锚点在JSON。
- Chapter/Route：1 / ending / director staging；E E04；原创导演staging/主题剪接；非游戏连续录像或新增canon。
- 必要性：第一次明确认知断裂：心可离开，身体没有随它退场。
- Player：仍能移同一SOUL，不能由它决定身体步伐；Kris：身体继续有动作，动机不裁定；Other：私域/关系不依当前选择更新；Story：笼/vent限制可达位置。
- Camera / spatial novelty：Kris胸/手近景，约身体540,560；同一心先在胸，再移手，camera不跳。
- Foreground：Kris胸、同一只手、同一SOUL；理由：第一次明确认知断裂：心可离开，身体没有随它退场。
- Background：房间地面/门；不切换人物海报；理由：建立身体动作的可达空间/距离；不是抽象信息图。
- UI：接口在接触时断，不逐词拆CSS；Text：无；无。
- Character：Kris，original geometric rough blocking; production art pending；SOUL：胸→手→胸外，不能生成替身心。
- 连续动作：2571–2644留完整身体；2644–2650手准备；2650–2674连续拉出；2674–2692手带心到笼位置。
- In：camera留在同一胸/手，暖光开始退；Out：同一房间拉宽，身体/心同时能看见。
- Colour：['#070A14', '#75A58B', '#C7E4EC', '#F04462']；Effects：少量接触光/水纹；拒绝靠generic glitch提升预算；纯黑区无后期残影。
- 复用：film/tui_pv_world_execute_20260926/tuikit.py:font / film/tui_pv_world_execute_20260926/continuity_full_v2/cuts.py:independent carrier/mask principle (design reuse)；KEEP整数timing/分层；REPLACE静态左右pane与哲学分支图；REMOVE常驻ticker/舞者。
- 实现：film/deltarune_poc/scenes.py:separation / film/deltarune_poc/stage.py:posed_characters / film/deltarune_poc/renderer.py:frame；PIL，零旧monkey patch；HTML不必需；生产原创透明asset可后替换。
- 素材：rough geometry; game visual R01–03 / production art pending；仍待：不写Kris认识/憎恨现实Player；抽心细节仍是原创staging。
- QA frames：[2571, 2583, 2632, 2692]；关键事件：['K02']。

### PV18 — 输入仍在，身体走开 / BREATH

- 时间：[2693,2838)；112.208333–118.250000s；legacy ['DR36', 'DR37', 'DR38', 'DR39', 'DR40']。
- Song cue：反复离开→隔离；line IDs [54, 55, 56, 57, 58, 59]；所有word/frame锚点在JSON。
- Chapter/Route：1 / 4 / ending → vent thematic match；E E04 E20；原创导演staging/主题剪接；非游戏连续录像或新增canon。
- 必要性：把五次短拆层合成一个因果空间：心动、身体不跟。
- Player：仍能移同一SOUL，不能由它决定身体步伐；Kris：身体继续有动作，动机不裁定；Other：私域/关系不依当前选择更新；Story：笼/vent限制可达位置。
- Camera / spatial novelty：延续同一房间，camera拉宽见笼及远离的身体；后段笼格match成vent。
- Foreground：Kris向门独走，前景心在笼/后续vent；理由：把五次短拆层合成一个因果空间：心动、身体不跟。
- Background：同一地面拉宽，2784后格线主题match通道；理由：建立身体动作的可达空间/距离；不是抽象信息图。
- UI：外读区随身体退让，不补新字；Text：无；无。
- Character：Kris，original geometric rough blocking; production art pending；SOUL：同一心保持可见锚点，笼内移动不穿边。
- 连续动作：2693–2728心在笼移；2728–2754Kris离开；2754–2784两者同框hold；2784–2837格线match到vent。
- In：同一房间拉宽，身体/心同时能看见；Out：门内暖光露出私域。
- Colour：['#070A14', '#75A58B', '#C7E4EC', '#F04462']；Effects：少量接触光/水纹；拒绝靠generic glitch提升预算；纯黑区无后期残影。
- 复用：film/tui_pv_world_execute_20260926/tuikit.py:font / film/tui_pv_world_execute_20260926/continuity_full_v2/cuts.py:independent carrier/mask principle (design reuse)；KEEP整数timing/分层；REPLACE静态左右pane与哲学分支图；REMOVE常驻ticker/舞者。
- 实现：film/deltarune_poc/scenes.py:isolated / film/deltarune_poc/stage.py:posed_characters / film/deltarune_poc/renderer.py:frame；PIL，零旧monkey patch；HTML不必需；生产原创透明asset可后替换。
- 素材：rough geometry; game visual R01–03 / production art pending；仍待：Ch1→Ch4是主题match，不宣称房间真实连通；不能穿笼造canon。
- QA frames：[2693, 2705, 2765, 2837]；关键事件：['K02']。

### PV19 — 门内不是命令窗口 / BREATH

- 时间：[2838,2928)；118.250000–122.000000s；legacy ['DR41']。
- Song cue：清理片段/希望留住；line IDs [59, 60]；所有word/frame锚点在JSON。
- Chapter/Route：4 / weird / private space with remembered report；E E20 E23；原创导演staging/主题剪接；非游戏连续录像或新增canon。
- 必要性：隔墙的距离使外心成为观察者，给私话重量。
- Player：仍能移同一SOUL，不能由它决定身体步伐；Kris：身体继续有动作，动机不裁定；Other：私域/关系不依当前选择更新；Story：笼/vent限制可达位置。
- Camera / spatial novelty：隔墙低机位，心在前景vent，门内两个人处暖光；private/recollection有明确距离。
- Foreground：门内Kris/Noelle，外面SOUL小但清楚；理由：隔墙的距离使外心成为观察者，给私话重量。
- Background：房间暖光与vent暗角，缺一条控制连接；理由：建立身体动作的可达空间/距离；不是抽象信息图。
- UI：无VOICE/KRIS解释卡；Text：无；无。
- Character：Kris，original geometric rough blocking; production art pending；SOUL：留在前景通道，看得到身体但够不到。
- 连续动作：2838–2885门内身位靠近；2885–2927只肩/手的微动作，外心停；不新增对白。
- In：门内暖光露出私域；Out：一个choice物体在房内立起来。
- Colour：['#070A14', '#75A58B', '#C7E4EC', '#F04462']；Effects：少量接触光/水纹；拒绝靠generic glitch提升预算；纯黑区无后期残影。
- 复用：film/tui_pv_world_execute_20260926/tuikit.py:font / film/tui_pv_world_execute_20260926/continuity_full_v2/cuts.py:independent carrier/mask principle (design reuse)；KEEP整数timing/分层；REPLACE静态左右pane与哲学分支图；REMOVE常驻ticker/舞者。
- 实现：film/deltarune_poc/scenes.py:private / film/deltarune_poc/stage.py:posed_characters / film/deltarune_poc/renderer.py:frame；PIL，零旧monkey patch；HTML不必需；生产原创透明asset可后替换。
- 素材：rough geometry; game visual R01–03 / production art pending；仍待：歉意只由Noelle回忆支持，不把旧回忆画成确证录像。
- QA frames：[2838, 2850, 2883, 2927]；关键事件：[]。

### PV20 — 菜单闯进私人空间 / HERO

- 时间：[2928,3014)；122.000000–125.583333s；legacy ['DR42']。
- Song cue：希望重获连接；line IDs [61, 62, 63]；所有word/frame锚点在JSON。
- Chapter/Route：4 / weird；E E24；原创导演staging/主题剪接；非游戏连续录像或新增canon。
- 必要性：外面的心沿实体choice进入，再占回身体接口。
- Player：影响强，维持路线的条件窄；Kris：代行/反冲并保留动作及代价；Other：拒绝/执行/察觉不同声音；Story：预设条件与锁定规定推进。
- Camera / spatial novelty：延续门/vent同几何，菜单竖成房内入口；心路径跨墙至胸，非字卡切换。
- Foreground：同一SOUL越墙到胸；Kris/Noelle仍是身体；理由：外面的心沿实体choice进入，再占回身体接口。
- Background：门与vent延续前镜坐标；理由：建立身体动作的可达空间/距离；不是抽象信息图。
- UI：choice竖成门一样的世界物体；Text：Proceed；短词/名字或明确作者问题；非歌词/新增角色对白。
- Character：Kris，original geometric rough blocking; production art pending；SOUL：vent→房内菜单→Kris胸，只有一次心。
- 连续动作：2928–2940门显；2940–2972心穿通道；2972–2996到胸；2996–3013重入，暖空间受挤。
- In：一个choice物体在房内立起来；Out：房间地面转为折返路径。
- Colour：['#070A14', '#75A58B', '#C7E4EC', '#F04462']；Effects：少量接触光/水纹；拒绝靠generic glitch提升预算；纯黑区无后期残影。
- 复用：film/tui_pv_world_execute_20260926/tuikit.py:font / film/tui_pv_world_execute_20260926/continuity_full_v2/cuts.py:independent carrier/mask principle (design reuse)；KEEP整数timing/分层；REPLACE静态左右pane与哲学分支图；REMOVE常驻ticker/舞者。
- 实现：film/deltarune_poc/scenes.py:reentry / film/deltarune_poc/stage.py:posed_characters / film/deltarune_poc/renderer.py:frame；PIL，零旧monkey patch；HTML不必需；生产原创透明asset可后替换。
- 素材：rough geometry; game visual R01–03 / production art pending；仍待：原游戏layout/time limit待R02，PV frame不冒充game tick。
- QA frames：[2928, 2940, 2971, 3013]；关键事件：['K03']。

### PV21 — 有力量仍需走规定的路 / SUPPORT

- 时间：[3014,3093)；125.583333–128.875000s；legacy ['DR43']。
- Song cue：挑战/条件限制；line IDs [63, 64]；所有word/frame锚点在JSON。
- Chapter/Route：2 / 4 / weird / thematic crosscut；E E08 E24；原创导演staging/主题剪接；非游戏连续录像或新增canon。
- 必要性：偏离的强影响与狭窄路径在俯视地面同时出现。
- Player：影响强，维持路线的条件窄；Kris：代行/反冲并保留动作及代价；Other：拒绝/执行/察觉不同声音；Story：预设条件与锁定规定推进。
- Camera / spatial novelty：俯视折返地面/有限步点；Kris可走路径有限，UI不列条件表。
- Foreground：Kris走回自己留下的足位；理由：偏离的强影响与狭窄路径在俯视地面同时出现。
- Background：三处实际窄口，回退弧；理由：建立身体动作的可达空间/距离；不是抽象信息图。
- UI：不列requirements文字；Text：无；无。
- Character：Kris，original geometric rough blocking; production art pending；SOUL：沿有限路径，不能任意跳到另一世界。
- 连续动作：3014–3054折返；3054–3092逐窄口停一步，出口仍窄。
- In：房间地面转为折返路径；Out：窄口接触点match到腕。
- Colour：['#070A14', '#75A58B', '#C7E4EC', '#F04462']；Effects：少量接触光/水纹；拒绝靠generic glitch提升预算；纯黑区无后期残影。
- 复用：film/tui_pv_world_execute_20260926/tuikit.py:font / film/tui_pv_world_execute_20260926/continuity_full_v2/cuts.py:independent carrier/mask principle (design reuse)；KEEP整数timing/分层；REPLACE静态左右pane与哲学分支图；REMOVE常驻ticker/舞者。
- 实现：film/deltarune_poc/scenes.py:route_gates / film/deltarune_poc/stage.py:posed_characters / film/deltarune_poc/renderer.py:frame；PIL，零旧monkey patch；HTML不必需；生产原创透明asset可后替换。
- 素材：rough geometry; game visual R01–03 / production art pending；仍待：不写真实游戏code或虚构剧情条件。
- QA frames：[3014, 3026, 3053, 3092]；关键事件：[]。

### PV22 — 接触的代价回到身体 / HERO

- 时间：[3093,3232)；128.875000–134.666667s；legacy ['DR44', 'DR45']。
- Song cue：锁定/非法参数/反冲；line IDs [64, 65]；所有word/frame锚点在JSON。
- Chapter/Route：4 / weird；E E26；原创导演staging/主题剪接；非游戏连续录像或新增canon。
- 必要性：抓腕施加与接口反冲在同一角色上，不是胜利恐怖特效。
- Player：影响强，维持路线的条件窄；Kris：代行/反冲并保留动作及代价；Other：拒绝/执行/察觉不同声音；Story：预设条件与锁定规定推进。
- Camera / spatial novelty：腕/接触前景→房间反冲宽景一次pullback；red crack不血腥。
- Foreground：Kris/Noelle腕接触、红裂、随后Kris手/脚反冲；理由：抓腕施加与接口反冲在同一角色上，不是胜利恐怖特效。
- Background：接触close拉后见稳定浴室容器；理由：建立身体动作的可达空间/距离；不是抽象信息图。
- UI：分支只短暂收束，不常驻glitch；Text：无；无。
- Character：Kris，original geometric rough blocking; production art pending；SOUL：命令位置→被放入容器，震动仍有心。
- 连续动作：3093–3117手接近；3117–3149裂；3149–3185抽心放容器；3185–3209一次踢/回震；3209–3231静止。
- In：窄口接触点match到腕；Out：回震低姿态match到另一章低伏身体。
- Colour：['#070A14', '#75A58B', '#C7E4EC', '#F04462']；Effects：少量接触光/水纹；拒绝靠generic glitch提升预算；纯黑区无后期残影。
- 复用：film/tui_pv_world_execute_20260926/tuikit.py:font / film/tui_pv_world_execute_20260926/continuity_full_v2/cuts.py:independent carrier/mask principle (design reuse)；KEEP整数timing/分层；REPLACE静态左右pane与哲学分支图；REMOVE常驻ticker/舞者。
- 实现：film/deltarune_poc/scenes.py:lock_recoil / film/deltarune_poc/stage.py:posed_characters / film/deltarune_poc/renderer.py:frame；PIL，零旧monkey patch；HTML不必需；生产原创透明asset可后替换。
- 素材：rough geometry; game visual R01–03 / production art pending；仍待：Ch4→Ch2是主题cut；不浪漫化自伤/不判断动机。
- QA frames：[3093, 3105, 3162, 3231]；关键事件：['K04']。

### PV23 — 身体倒下，命令继续 / SUPPORT

- 时间：[3232,3323)；134.666667–138.458333s；legacy ['DR46']。
- Song cue：器乐施压；line IDs []；所有word/frame锚点在JSON。
- Chapter/Route：2 / weird；E E09 E12；原创导演staging/主题剪接；非游戏连续录像或新增canon。
- 必要性：声音/命令归属不能由倒下身体概括。
- Player：影响强，维持路线的条件窄；Kris：代行/反冲并保留动作及代价；Other：拒绝/执行/察觉不同声音；Story：预设条件与锁定规定推进。
- Camera / spatial novelty：低伏Kris在近景，Noelle远处仍面向屏外pulse；命令越过身体。
- Foreground：低身位Kris在近处，Noelle远处应对；理由：声音/命令归属不能由倒下身体概括。
- Background：冰白空间保留地面与空位；理由：建立身体动作的可达空间/距离；不是抽象信息图。
- UI：屏外pulse越过Kris而非自胸发出；Text：无；无。
- Character：Kris，original geometric rough blocking; production art pending；SOUL：接口可见，Kris不随pulse起身。
- 连续动作：3232–3270身体低伏，pulse越过；3270–3322Noelle远处动作一次，Kris维持。
- In：回震低姿态match到另一章低伏身体；Out：pulse源落到controller接点。
- Colour：['#070A14', '#75A58B', '#C7E4EC', '#F04462']；Effects：少量接触光/水纹；拒绝靠generic glitch提升预算；纯黑区无后期残影。
- 复用：film/tui_pv_world_execute_20260926/tuikit.py:font / film/tui_pv_world_execute_20260926/continuity_full_v2/cuts.py:independent carrier/mask principle (design reuse)；KEEP整数timing/分层；REPLACE静态左右pane与哲学分支图；REMOVE常驻ticker/舞者。
- 实现：film/deltarune_poc/scenes.py:down_command / film/deltarune_poc/stage.py:posed_characters / film/deltarune_poc/renderer.py:frame；PIL，零旧monkey patch；HTML不必需；生产原创透明asset可后替换。
- 素材：rough geometry; game visual R01–03 / production art pending；仍待：DOWN不等于死亡，不配现实玩家声音。
- QA frames：[3232, 3244, 3277, 3322]；关键事件：[]。

### PV24 — 内世界抵住方向 / SUPPORT

- 时间：[3323,3549)；138.458333–147.875000s；legacy ['DR47', 'DR48']。
- Song cue：器乐蓄压/越界条件；line IDs []；所有word/frame锚点在JSON。
- Chapter/Route：3 / sword；E E15 E16；原创导演staging/主题剪接；非游戏连续录像或新增canon。
- 必要性：控制链在实际小游戏边界积压，不再增加概念框。
- Player：controller/小游戏仍受舞台条件；Kris：主体在外层，对输入有身体反应；Other：角色可介入；Story：内外屏幕是实际可见通道。
- Camera / spatial novelty：同一TV地面抵住方向；camera逐渐到内屏边，删第二个套框。
- Foreground：Kris/controller、内HERO在shelter方向受阻；理由：控制链在实际小游戏边界积压，不再增加概念框。
- Background：有厚度TV内两段地面和门槛；理由：建立身体动作的可达空间/距离；不是抽象信息图。
- UI：内方向点与身体退步不同节奏；Text：无；无。
- Character：Kris，original geometric rough blocking; production art pending；SOUL：连接到内HERO，Kris不被替换。
- 连续动作：3323–3412向门/阻力重复两次；3412–3500慢推至屏面；3500–3548留edge压力。
- In：pulse源落到controller接点；Out：镜头压紧的空间接到12pulse世界。
- Colour：['#070A14', '#75A58B', '#C7E4EC', '#F04462']；Effects：少量接触光/水纹；拒绝靠generic glitch提升预算；纯黑区无后期残影。
- 复用：film/tui_pv_world_execute_20260926/tuikit.py:font / film/tui_pv_world_execute_20260926/continuity_full_v2/cuts.py:independent carrier/mask principle (design reuse)；KEEP整数timing/分层；REPLACE静态左右pane与哲学分支图；REMOVE常驻ticker/舞者。
- 实现：film/deltarune_poc/scenes.py:sword_pressure / film/deltarune_poc/stage.py:posed_characters / film/deltarune_poc/renderer.py:frame；PIL，零旧monkey patch；HTML不必需；生产原创透明asset可后替换。
- 素材：rough geometry; game visual R01–03 / production art pending；仍待：不猜shelter/holder身份；精确动作待R01。
- QA frames：[3323, 3335, 3436, 3548]；关键事件：[]。

### PV25 — 十二次命令改变空间 / HERO

- 时间：[3549,3821)；147.875000–159.208333s；legacy ['DR49', 'DR50']。
- Song cue：十二次重复执行；line IDs [67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79]；所有word/frame锚点在JSON。
- Chapter/Route：2 / weird / condensed execution；E E08 E10；原创导演staging/主题剪接；非游戏连续录像或新增canon。
- 必要性：每次输入留下世界压力与代价，不能成12个杀敌flash。
- Player：影响强，维持路线的条件窄；Kris：代行/反冲并保留动作及代价；Other：拒绝/执行/察觉不同声音；Story：预设条件与锁定规定推进。
- Camera / spatial novelty：侧向世界构图，12起音依次使冰/路径压力积累；第二半镜头进深，不靠12cut。
- Foreground：Kris手保持，Noelle施法方向和空位逐渐受挤；理由：每次输入留下世界压力与代价，不能成12个杀敌flash。
- Background：侧景地面被冰纹/窄列挤压；第二半camera进深；理由：建立身体动作的可达空间/距离；不是抽象信息图。
- UI：一命令位置短亮，每pulse后留hold；Text：无；无。
- Character：Kris，original geometric rough blocking; production art pending；SOUL：同一心触同一接口，不生成12心。
- 连续动作：line67–78每起音一次空间压力；前6侧向压，后6camera沿深度推；末3795后hold到3821。
- In：镜头压紧的空间接到12pulse世界；Out：最后压力线match到TV内控制接点。
- Colour：['#070A14', '#75A58B', '#C7E4EC', '#F04462']；Effects：少量接触光/水纹；拒绝靠generic glitch提升预算；纯黑区无后期残影。
- 复用：film/tui_pv_world_execute_20260926/tuikit.py:font / film/tui_pv_world_execute_20260926/continuity_full_v2/cuts.py:independent carrier/mask principle (design reuse)；KEEP整数timing/分层；REPLACE静态左右pane与哲学分支图；REMOVE常驻ticker/舞者。
- 实现：film/deltarune_poc/scenes.py:execution / film/deltarune_poc/stage.py:posed_characters / film/deltarune_poc/renderer.py:frame；PIL，零旧monkey patch；HTML不必需；生产原创透明asset可后替换。
- 素材：rough geometry; game visual R01–03 / production art pending；仍待：12是歌曲次数，不是canon敌人数；Berdly冰封不当死亡确证。
- QA frames：[3549, 3561, 3685, 3820]；关键事件：[]。

### PV26 — 摄影机将跟错对象 / TRANSITION

- 时间：[3821,3902)；159.208333–162.583333s；legacy ['DR51']。
- Song cue：计数/呼唤归属；line IDs [79, 80, 81, 82]；所有word/frame锚点在JSON。
- Chapter/Route：2 / 3 / weird → sword thematic cut；E E11 E18；原创导演staging/主题剪接；非游戏连续录像或新增canon。
- 必要性：叙述主语不用标签解释，input目标迁到内HERO。
- Player：controller/小游戏仍受舞台条件；Kris：主体在外层，对输入有身体反应；Other：角色可介入；Story：内外屏幕是实际可见通道。
- Camera / spatial novelty：controller手→内HERO控制接点的match；不写KRIS/YOU说明字。
- Foreground：Kris握controller仍大，HERO在另一平面；理由：叙述主语不用标签解释，input目标迁到内HERO。
- Background：TV屏面和外世界不同深度；理由：建立身体动作的可达空间/距离；不是抽象信息图。
- UI：接点从身体移至HERO，不写KRIS/YOU；Text：无；无。
- Character：Kris，original geometric rough blocking; production art pending；SOUL：只有一个主要心，输入指向HERO。
- 连续动作：3821–3880控制接点移；3880–3901HERO脚至内屏边；camera预先偏向它。
- In：最后压力线match到TV内控制接点；Out：HERO载体开始跨实体屏面。
- Colour：['#070A14', '#75A58B', '#C7E4EC', '#F04462']；Effects：少量接触光/水纹；拒绝靠generic glitch提升预算；纯黑区无后期残影。
- 复用：film/tui_pv_world_execute_20260926/tuikit.py:font / film/tui_pv_world_execute_20260926/continuity_full_v2/cuts.py:independent carrier/mask principle (design reuse)；KEEP整数timing/分层；REPLACE静态左右pane与哲学分支图；REMOVE常驻ticker/舞者。
- 实现：film/deltarune_poc/scenes.py:target_shift / film/deltarune_poc/stage.py:posed_characters / film/deltarune_poc/renderer.py:frame；PIL，零旧monkey patch；HTML不必需；生产原创透明asset可后替换。
- 素材：rough geometry; game visual R01–03 / production art pending；仍待：不擅自把第二人称配成人类玩家声音。
- QA frames：[3821, 3833, 3861, 3901]；关键事件：[]。

### PV27 — 控制对象走出屏幕 / HERO

- 时间：[3902,3988)；162.583333–166.166667s；legacy ['DR52']。
- Song cue：执行交给他者；line IDs [83, 84]；所有word/frame锚点在JSON。
- Chapter/Route：3 / sword；E E18；原创导演staging/主题剪接；非游戏连续录像或新增canon。
- 必要性：camera跟HERO使观众短暂丢失对Kris的中心感；输入归属仍清楚。
- Player：仍黏在HERO，camera错跟不是Kris意愿；Kris：可退后/拉开Susie；Other：Susie可介入断线；Story：出屏也属于已实现分支。
- Camera / spatial novelty：HERO跨实体屏幕平面；camera追它，Kris暂在侧缘但不消失。
- Foreground：HERO跨厚TV边，Kris退后但留左侧；理由：camera跟HERO使观众短暂丢失对Kris的中心感；输入归属仍清楚。
- Background：TV内地面只裁背景，跨屏carrier独立；理由：建立身体动作的可达空间/距离；不是抽象信息图。
- UI：input接点跟HERO，不跟Kris；Text：无；无。
- Character：Kris，original geometric rough blocking; production art pending；SOUL：连接目标始终HERO，跨边不另造心。
- 连续动作：3902–3938HERO跨平面；3926–3942Kris退；3938–3962camera追HERO；3962–3987停在错误中心。
- In：HERO载体开始跨实体屏面；Out：攻击方向逼近Susie，Kris准备横移。
- Colour：['#070A14', '#75A58B', '#C7E4EC', '#F04462']；Effects：少量接触光/水纹；拒绝靠generic glitch提升预算；纯黑区无后期残影。
- 复用：film/tui_pv_world_execute_20260926/tuikit.py:font / film/tui_pv_world_execute_20260926/continuity_full_v2/cuts.py:independent carrier/mask principle (design reuse)；KEEP整数timing/分层；REPLACE静态左右pane与哲学分支图；REMOVE常驻ticker/舞者。
- 实现：film/deltarune_poc/scenes.py:screen_exit / film/deltarune_poc/stage.py:posed_characters / film/deltarune_poc/renderer.py:frame；PIL，零旧monkey patch；HTML不必需；生产原创透明asset可后替换。
- 素材：rough geometry; game visual R01–03 / production art pending；仍待：crossing与camera都是原创演出，游戏连续画面待R01。
- QA frames：[3902, 3914, 3945, 3987]；关键事件：['K06']。

### PV28 — Kris把她拉开 / HERO

- 时间：[3988,4072)；166.166667–169.666667s；legacy ['DR53']。
- Song cue：执行作用反转；line IDs [85, 86]；所有word/frame锚点在JSON。
- Chapter/Route：3 / sword / condensed branch staging；E E19；原创导演staging/主题剪接；非游戏连续录像或新增canon。
- 必要性：全片最明显的非当前selector主导动作；他者可介入控制链。
- Player：仍黏在HERO，camera错跟不是Kris意愿；Kris：可退后/拉开Susie；Other：Susie可介入断线；Story：出屏也属于已实现分支。
- Camera / spatial novelty：camera被Kris横向拉开动作抢回；Susie移走后攻击落空，再拔connector。
- Foreground：Kris手拉Susie离开攻击旧位置，Susie再拔connector；理由：全片最明显的非当前selector主导动作；他者可介入控制链。
- Background：同TV/外地面，camera因拉开被抢回；理由：建立身体动作的可达空间/距离；不是抽象信息图。
- UI：输入仍对HERO，拔线后它失去载体；Text：无；无。
- Character：Kris，original geometric rough blocking; production art pending；SOUL：选择点未先移动，手先动；断线不抹心。
- 连续动作：3988–4000预攻击；4000–4012Kris先伸手；4012–4030拉离；4030–4040攻击落空；4040–4064Susie拔线；4064–4071hold。
- In：攻击方向逼近Susie，Kris准备横移；Out：空的旧攻击位成为一段沉默。
- Colour：['#070A14', '#75A58B', '#C7E4EC', '#F04462']；Effects：少量接触光/水纹；拒绝靠generic glitch提升预算；纯黑区无后期残影。
- 复用：film/tui_pv_world_execute_20260926/tuikit.py:font / film/tui_pv_world_execute_20260926/continuity_full_v2/cuts.py:independent carrier/mask principle (design reuse)；KEEP整数timing/分层；REPLACE静态左右pane与哲学分支图；REMOVE常驻ticker/舞者。
- 实现：film/deltarune_poc/scenes.py:protect / film/deltarune_poc/stage.py:posed_characters / film/deltarune_poc/renderer.py:frame；PIL，零旧monkey patch；HTML不必需；生产原创透明asset可后替换。
- 素材：rough geometry; game visual R01–03 / production art pending；仍待：合并相关分支用于导演staging，不声称同一游戏录像必然连续如此。
- QA frames：[3988, 4000, 4030, 4071]；关键事件：['K07']。

### PV29 — 回来却没有字 / BREATH

- 时间：[4072,4164)；169.666667–173.500000s；legacy ['DR54']。
- Song cue：取回接口/回应不可能；line IDs [86, 87, 88, 89]；所有word/frame锚点在JSON。
- Chapter/Route：4 / weird / thematic crosscut；E E27；原创导演staging/主题剪接；非游戏连续录像或新增canon。
- 必要性：不立刻制造第三个高潮，让Kris/Susie之间的停顿可见。
- Player：影响强，维持路线的条件窄；Kris：代行/反冲并保留动作及代价；Other：拒绝/执行/察觉不同声音；Story：预设条件与锁定规定推进。
- Camera / spatial novelty：静默两人中景，四空格短显；雨/呼吸取代持续输入ticker。
- Foreground：Kris胸/手、可辨的Susie侧影；理由：不立刻制造第三个高潮，让Kris/Susie之间的停顿可见。
- Background：雨/低光地面，关系距离；理由：建立身体动作的可达空间/距离；不是抽象信息图。
- UI：四空slot短显后不刷说明；Text：无；无。
- Character：Kris，original geometric rough blocking; production art pending；SOUL：可移而无文本，身体不替作者说话。
- 连续动作：4072–4100格显；4100–4130selector一移；4130–4163只有雨/肩呼吸。
- In：空的旧攻击位成为一段沉默；Out：低身位落向床边。
- Colour：['#070A14', '#75A58B', '#C7E4EC', '#F04462']；Effects：少量接触光/水纹；拒绝靠generic glitch提升预算；纯黑区无后期残影。
- 复用：film/tui_pv_world_execute_20260926/tuikit.py:font / film/tui_pv_world_execute_20260926/continuity_full_v2/cuts.py:independent carrier/mask principle (design reuse)；KEEP整数timing/分层；REPLACE静态左右pane与哲学分支图；REMOVE常驻ticker/舞者。
- 实现：film/deltarune_poc/scenes.py:blank_reply / film/deltarune_poc/stage.py:posed_characters / film/deltarune_poc/renderer.py:frame；PIL，零旧monkey patch；HTML不必需；生产原创透明asset可后替换。
- 素材：rough geometry; game visual R01–03 / production art pending；仍待：不能给空项填作者希望的Kris独白。
- QA frames：[4072, 4084, 4118, 4163]；关键事件：[]。

### PV30 — 手撑着慢慢起身 / SUPPORT

- 时间：[4164,4259)；173.500000–177.458333s；legacy ['DR55']。
- Song cue：受困/反复输入；line IDs [89, 90, 91]；所有word/frame锚点在JSON。
- Chapter/Route：5 / weird；E E31；原创导演staging/主题剪接；非游戏连续录像或新增canon。
- 必要性：急输入与慢身体以低机位呈现，不用进度条。
- Player：selector可移，结果趋同；仍可停止输入；Kris：身体/手有另一节奏，动机未知；Other：Noelle主动索求不等于自由；Story：确认时限要求继续执行。
- Camera / spatial novelty：手撑地的低机位，身体大、pulse小；身位迟缓不等于明确抗议动机。
- Foreground：Kris手撑地、身形低而大；理由：急输入与慢身体以低机位呈现，不用进度条。
- Background：床边与后窗冷光；理由：建立身体动作的可达空间/距离；不是抽象信息图。
- UI：小pulse急于身体，非百分比；Text：无；无。
- Character：Kris，original geometric rough blocking; production art pending；SOUL：留身体接口，弱亮但不消失。
- 连续动作：4164–4200手压地；4200–4258重复pulse而身体只抬很小距离。
- In：低身位落向床边；Out：窗冷光延伸成湖岸。
- Colour：['#070A14', '#75A58B', '#C7E4EC', '#F04462']；Effects：少量接触光/水纹；拒绝靠generic glitch提升预算；纯黑区无后期残影。
- 复用：film/tui_pv_world_execute_20260926/tuikit.py:font / film/tui_pv_world_execute_20260926/continuity_full_v2/cuts.py:independent carrier/mask principle (design reuse)；KEEP整数timing/分层；REPLACE静态左右pane与哲学分支图；REMOVE常驻ticker/舞者。
- 实现：film/deltarune_poc/scenes.py:bed_drag / film/deltarune_poc/stage.py:posed_characters / film/deltarune_poc/renderer.py:frame；PIL，零旧monkey patch；HTML不必需；生产原创透明asset可后替换。
- 素材：rough geometry; game visual R01–03 / production art pending；仍待：迟缓动机未知，不诊断其自伤/拒绝/认知现实玩家。
- QA frames：[4164, 4176, 4211, 4258]；关键事件：[]。

### PV31 — 她把命令带进世界 / HERO

- 时间：[4259,4430)；177.458333–184.583333s；legacy ['DR56', 'DR57']。
- Song cue：学习/索求/拒绝仍前进；line IDs [91, 92, 93, 94]；所有word/frame锚点在JSON。
- Chapter/Route：5 / weird；E E32 E33；原创导演staging/主题剪接；非游戏连续录像或新增canon。
- 必要性：Noelle第一次从角色层主动跨向输入源；Player拒绝与既往塑造冲突。
- Player：selector可移，结果趋同；仍可停止输入；Kris：身体/手有另一节奏，动机未知；Other：Noelle主动索求不等于自由；Story：确认时限要求继续执行。
- Camera / spatial novelty：湖全宽，Noelle从右主动伸手跨向input来源；Kris大体量/手仍为焦点。
- Foreground：Noelle伸向input的手、Kris独立慢身位/手；理由：Noelle第一次从角色层主动跨向输入源；Player拒绝与既往塑造冲突。
- Background：全宽湖/岸，角色大，UI少；理由：建立身体动作的可达空间/距离；不是抽象信息图。
- UI：choice被她的手势带到世界，而非静态左pane；Text：Stop / Proceed；短词/名字或明确作者问题；非歌词/新增角色对白。
- Character：Kris，original geometric rough blocking; production art pending；SOUL：先停Stop，身位仍在她引导方向小移。
- 连续动作：4259–4319她跨向输入；4319–4344菜单入世界；4344–4367Stop/手引导；4367–4429角色hold与水移动。
- In：窗冷光延伸成湖岸；Out：两只手夹住菜单进入近景。
- Colour：['#070A14', '#75A58B', '#C7E4EC', '#F04462']；Effects：少量接触光/水纹；拒绝靠generic glitch提升预算；纯黑区无后期残影。
- 复用：film/tui_pv_world_execute_20260926/tuikit.py:font / film/tui_pv_world_execute_20260926/continuity_full_v2/cuts.py:independent carrier/mask principle (design reuse)；KEEP整数timing/分层；REPLACE静态左右pane与哲学分支图；REMOVE常驻ticker/舞者。
- 实现：film/deltarune_poc/scenes.py:noelle_lead / film/deltarune_poc/stage.py:posed_characters / film/deltarune_poc/renderer.py:frame；PIL，零旧monkey patch；HTML不必需；生产原创透明asset可后替换。
- 素材：rough geometry; game visual R01–03 / production art pending；仍待：主动不是自由/爱情解救；保留Stop回应/计数差异的短痕迹。
- QA frames：[4259, 4271, 4344, 4429]；关键事件：['K08']。

### PV32 — 位置变了，手仍被带着 / HERO

- 时间：[4430,4519)；184.583333–188.291667s；legacy ['DR58']。
- Song cue：关系变成表达式；line IDs [95]；所有word/frame锚点在JSON。
- Chapter/Route：5 / weird / prompt condensation；E E33 E34；原创导演staging/主题剪接；非游戏连续录像或新增canon。
- 必要性：不解释式子，让selector可变而手/身体保持另一节奏。
- Player：selector可移，结果趋同；仍可停止输入；Kris：身体/手有另一节奏，动机未知；Other：Noelle主动索求不等于自由；Story：确认时限要求继续执行。
- Camera / spatial novelty：两只手、菜单和红心的近景；一条水线，不左右技术pane。
- Foreground：Kris与Noelle两只手占主要面积，红心在菜单；理由：不解释式子，让selector可变而手/身体保持另一节奏。
- Background：一条湖水线/外冷光；理由：建立身体动作的可达空间/距离；不是抽象信息图。
- UI：两格同文，menu已经在世界内；Text：Proceed / Proceed；短词/名字或明确作者问题；非歌词/新增角色对白。
- Character：Kris，original geometric rough blocking; production art pending；SOUL：左→右，4495可读；无假Stop出口。
- 连续动作：4430–4436Stophold；4436–4442退字；4442–4448同文；4448–4460心移；4460–4518手迟疑/湖留痕。
- In：两只手夹住菜单进入近景；Out：屏外pulse停止到来，UI失去节奏。
- Colour：['#070A14', '#75A58B', '#C7E4EC', '#F04462']；Effects：少量接触光/水纹；拒绝靠generic glitch提升预算；纯黑区无后期残影。
- 复用：film/tui_pv_world_execute_20260926/tuikit.py:font / film/tui_pv_world_execute_20260926/continuity_full_v2/cuts.py:independent carrier/mask principle (design reuse)；KEEP整数timing/分层；REPLACE静态左右pane与哲学分支图；REMOVE常驻ticker/舞者。
- 实现：film/deltarune_poc/scenes.py:converged_choice / film/deltarune_poc/stage.py:posed_characters / film/deltarune_poc/renderer.py:frame；PIL，零旧monkey patch；HTML不必需；生产原创透明asset可后替换。
- 素材：rough geometry; game visual R01–03 / production art pending；仍待：不重演全部prompt；身体迟疑是作者情绪设计非动机证明。
- QA frames：[4430, 4442, 4474, 4518]；关键事件：['K08']。

### PV33 — 停止到来的输入 / BREATH

- 时间：[4519,4574)；188.291667–190.583333s；legacy ['DR59']。
- Song cue：似自由/受困的反证；line IDs [96, 97]；所有word/frame锚点在JSON。
- Chapter/Route：5 / interrupted weird / comparative staging；E E34 E36；原创导演staging/主题剪接；非游戏连续录像或新增canon。
- 必要性：停止是输入没有再到来；后果不能被按钮洗净。
- Player：可停止输入，当前段可被中止；Kris：身体/既往后果留存；Other：Susie关切/Noelle变化未重置；Story：中止续章也是已编写出口。
- Camera / spatial novelty：pulse停止到来，心/冷痕不删；关切作为续章比较的反射，不画暂停按钮。
- Foreground：Kris手松、红心保留、关切关系的反射；理由：停止是输入没有再到来；后果不能被按钮洗净。
- Background：冷痕/空位未退；续章关切作为灰暖反射；理由：建立身体动作的可达空间/距离；不是抽象信息图。
- UI：确认pulse退去，不画暂停按钮；Text：无；无。
- Character：Kris，original geometric rough blocking; production art pending；SOUL：不被物理删除，停止selector操作。
- 连续动作：4519–4531pulse消失；4531–4543关切反射显；4543–4573人物/冷痕留hold。
- In：屏外pulse停止到来，UI失去节奏；Out：反射不删，继续側手势重新要求输入。
- Colour：['#070A14', '#75A58B', '#C7E4EC', '#F04462']；Effects：少量接触光/水纹；拒绝靠generic glitch提升预算；纯黑区无后期残影。
- 复用：film/tui_pv_world_execute_20260926/tuikit.py:font / film/tui_pv_world_execute_20260926/continuity_full_v2/cuts.py:independent carrier/mask principle (design reuse)；KEEP整数timing/分层；REPLACE静态左右pane与哲学分支图；REMOVE常驻ticker/舞者。
- 实现：film/deltarune_poc/scenes.py:cease_input / film/deltarune_poc/stage.py:posed_characters / film/deltarune_poc/renderer.py:frame；PIL，零旧monkey patch；HTML不必需；生产原创透明asset可后替换。
- 素材：rough geometry; game visual R01–03 / production art pending；仍待：比较不是同时canon多宇宙；不称全部reset。
- QA frames：[4519, 4531, 4546, 4573]；关键事件：['K09']。

### PV34 — 继续重新组织了控制 / TRANSITION

- 时间：[4574,4654)；190.583333–193.916667s；legacy ['DR60']。
- Song cue：持续确认的代价；line IDs [97, 98]；所有word/frame锚点在JSON。
- Chapter/Route：5 / weird + interruption comparison；E E32 E34 E36；原创导演staging/主题剪接；非游戏连续录像或新增canon。
- 必要性：继续不是Player胜利，角色世界向接口要求下一次执行。
- Player：selector可移，结果趋同；仍可停止输入；Kris：身体/手有另一节奏，动机未知；Other：Noelle主动索求不等于自由；Story：确认时限要求继续执行。
- Camera / spatial novelty：实际手势再要求确认，保留停止支线的关系余痕；不做两条按钮分支图。
- Foreground：Kris迟疑手，Noelle掌势把menu推回；理由：继续不是Player胜利，角色世界向接口要求下一次执行。
- Background：湖压力和停止侧关切余痕共在但不对称；理由：建立身体动作的可达空间/距离；不是抽象信息图。
- UI：一次confirmation收窄，再一次更紧；不画两分支按钮；Text：Proceed；短词/名字或明确作者问题；非歌词/新增角色对白。
- Character：Kris，original geometric rough blocking; production art pending；SOUL：趋白但留红外轮廓，仍能停止输入。
- 连续动作：4574–4601第一次收框；4601–4621第二次更紧；4621–4653世界水线抬，input小而身体大。
- In：反射不删，继续側手势重新要求输入；Out：水面成为屏幕表面的一层光。
- Colour：['#070A14', '#75A58B', '#C7E4EC', '#F04462']；Effects：少量接触光/水纹；拒绝靠generic glitch提升预算；纯黑区无后期残影。
- 复用：film/tui_pv_world_execute_20260926/tuikit.py:font / film/tui_pv_world_execute_20260926/continuity_full_v2/cuts.py:independent carrier/mask principle (design reuse)；KEEP整数timing/分层；REPLACE静态左右pane与哲学分支图；REMOVE常驻ticker/舞者。
- 实现：film/deltarune_poc/scenes.py:continue_input / film/deltarune_poc/stage.py:posed_characters / film/deltarune_poc/renderer.py:frame；PIL，零旧monkey patch；HTML不必需；生产原创透明asset可后替换。
- 素材：rough geometry; game visual R01–03 / production art pending；仍待：不是每个原game timeout单调减少；只PV压缩。
- QA frames：[4574, 4586, 4614, 4653]；关键事件：['K09']。

### PV35 — 连观察的位置也是屏幕 / HERO

- 时间：[4654,4863)；193.916667–202.625000s；legacy ['DR61', 'DR62']。
- Song cue：器乐递归/章节接收越界；line IDs []；所有word/frame锚点在JSON。
- Chapter/Route：3 / 5 / weird / author spatial metaphor；E E13 E35；原创导演staging/主题剪接；非游戏连续录像或新增canon。
- 必要性：唯一大边界揭示：内世界和操作点在实体CRT同一表面。
- Player：可等待/离开，不能提供未来章节；Kris：手/衣色仍使Kris成为最终主体；Other：不接管最后主体位置；Story：实体屏幕/章节断点是作者的上游边界隐喻。
- Camera / spatial novelty：湖/人物作为实体CRT表面，camera拉后露机身/stand/input plug；唯一大边界揭示。
- Foreground：Kris身体仍在湖图像，绿色衣袖保持识别；理由：唯一大边界揭示：内世界和操作点在实体CRT同一表面。
- Background：camera拉后露厚机身/stand/input plug，非三白框；理由：建立身体动作的可达空间/距离；不是抽象信息图。
- UI：小操作点也在屏幕上，不新增route/chapter标签；Text：无；无。
- Character：Kris，original geometric rough blocking; production art pending；SOUL：在表面内停留，不能称现实人被强制按键。
- 连续动作：4654–4734世界拉后/机身露；4734–4814input plug显；4814–4862保持主体尺寸可辨。
- In：水面成为屏幕表面的一层光；Out：camera回到衣袖/手的余波。
- Colour：['#070A14', '#75A58B', '#C7E4EC', '#F04462']；Effects：少量接触光/水纹；拒绝靠generic glitch提升预算；纯黑区无后期残影。
- 复用：film/tui_pv_world_execute_20260926/tuikit.py:font / film/tui_pv_world_execute_20260926/continuity_full_v2/cuts.py:independent carrier/mask principle (design reuse)；KEEP整数timing/分层；REPLACE静态左右pane与哲学分支图；REMOVE常驻ticker/舞者。
- 实现：film/deltarune_poc/scenes.py:crt_reveal / film/deltarune_poc/stage.py:posed_characters / film/deltarune_poc/renderer.py:frame；PIL，零旧monkey patch；HTML不必需；生产原创透明asset可后替换。
- 素材：rough geometry; game visual R01–03 / production art pending；仍待：CRT是作者Story隐喻，不声称Kris逃出或现实玩家可见。
- QA frames：[4654, 4666, 4758, 4862]；关键事件：['K05']。

### PV36 — 最后仍是一个人 / BREATH

- 时间：[4863,4929)；202.625000–205.375000s；legacy ['DR63']。
- Song cue：尾奏留停顿；line IDs [100]；所有word/frame锚点在JSON。
- Chapter/Route：1 / 5 / author aftermath；E E04 E36；原创导演staging/主题剪接；非游戏连续录像或新增canon。
- 必要性：最后20秒保住角色情绪，少于一个解释图表。
- Player：可等待/离开，不能提供未来章节；Kris：手/衣色仍使Kris成为最终主体；Other：不接管最后主体位置；Story：实体屏幕/章节断点是作者的上游边界隐喻。
- Camera / spatial novelty：回近景Kris衣袖/迟疑手与水面残影；最后20秒仍有身体。
- Foreground：Kris绿色衣袖与未完成的伸手；理由：最后20秒保住角色情绪，少于一个解释图表。
- Background：水/屏光反射一层，不加新框；理由：建立身体动作的可达空间/距离；不是抽象信息图。
- UI：无ticker/箭头；Text：无；无。
- Character：Kris，original geometric rough blocking; production art pending；SOUL：相距足够，没有最终谁占有谁。
- 连续动作：4863–4895衣袖慢入近景；4895–4928手停，只有反射/呼吸移动。
- In：camera回到衣袖/手的余波；Out：最后pulse落到手与心之间的接点。
- Colour：['#070A14', '#75A58B', '#C7E4EC', '#F04462']；Effects：少量接触光/水纹；拒绝靠generic glitch提升预算；纯黑区无后期残影。
- 复用：film/tui_pv_world_execute_20260926/tuikit.py:font / film/tui_pv_world_execute_20260926/continuity_full_v2/cuts.py:independent carrier/mask principle (design reuse)；KEEP整数timing/分层；REPLACE静态左右pane与哲学分支图；REMOVE常驻ticker/舞者。
- 实现：film/deltarune_poc/scenes.py:hand_aftermath / film/deltarune_poc/stage.py:posed_characters / film/deltarune_poc/renderer.py:frame；PIL，零旧monkey patch；HTML不必需；生产原创透明asset可后替换。
- 素材：rough geometry; game visual R01–03 / production art pending；仍待：不把伸手读作确定求死/同意/仇恨。
- QA frames：[4863, 4875, 4896, 4928]；关键事件：[]。

### PV37 — 最后一次接点 / TRANSITION

- 时间：[4929,4970)；205.375000–207.083333s；legacy ['DR64']。
- Song cue：最后执行/硬切；line IDs [100]；所有word/frame锚点在JSON。
- Chapter/Route：5 / weird / author compression；E E35；原创导演staging/主题剪接；非游戏连续录像或新增canon。
- 必要性：结束当前执行而非杀掉Player或角色。
- Player：可等待/离开，不能提供未来章节；Kris：手/衣色仍使Kris成为最终主体；Other：不接管最后主体位置；Story：实体屏幕/章节断点是作者的上游边界隐喻。
- Camera / spatial novelty：最后一次接触pulse，屏幕从完整像收为1px扫描线；无更大矩形。
- Foreground：Kris手/心、实体屏幕的残光；理由：结束当前执行而非杀掉Player或角色。
- Background：机身/湖只一层残像；理由：建立身体动作的可达空间/距离；不是抽象信息图。
- UI：最后pulse不引入新矩形；Text：无；无。
- Character：Kris，original geometric rough blocking; production art pending；SOUL：仍同一颗心到4969。
- 连续动作：4929–4935接点亮；4935–4962手hold；4962–4969画布收缩；4969只1px；4970切纯黑。
- In：最后pulse落到手与心之间的接点；Out：完整24帧黑，不继承DSHchime。
- Colour：['#070A14', '#75A58B', '#C7E4EC', '#F04462']；Effects：少量接触光/水纹；拒绝靠generic glitch提升预算；纯黑区无后期残影。
- 复用：film/tui_pv_world_execute_20260926/tuikit.py:font / film/tui_pv_world_execute_20260926/continuity_full_v2/cuts.py:independent carrier/mask principle (design reuse)；KEEP整数timing/分层；REPLACE静态左右pane与哲学分支图；REMOVE常驻ticker/舞者。
- 实现：film/deltarune_poc/scenes.py:final_pulse / film/deltarune_poc/stage.py:posed_characters / film/deltarune_poc/renderer.py:frame；PIL，零旧monkey patch；HTML不必需；生产原创透明asset可后替换。
- 素材：rough geometry; game visual R01–03 / production art pending；仍待：AUDIO REVIEW PENDING，4970来自原timing未听音校准。
- QA frames：[4929, 4941, 4949, 4969]；关键事件：['K10']。

### PV38 — 沉默以后仍被要求继续 / SUPPORT

- 时间：[4970,5030)；207.083333–209.583333s；legacy ['DR65']。
- Song cue：黑场/章边界；line IDs []；所有word/frame锚点在JSON。
- Chapter/Route：5 / weird early chapter ending；E E35；原创导演staging/主题剪接；非游戏连续录像或新增canon。
- 必要性：黑有时间重量，短提示只提出未来缺口，不展示答案。
- Player：可等待/离开，不能提供未来章节；Kris：手/衣色仍使Kris成为最终主体；Other：不接管最后主体位置；Story：实体屏幕/章节断点是作者的上游边界隐喻。
- Camera / spatial novelty：4970–4993纯黑24帧；4994–5029短章提示；不画下一章。
- Foreground：先无主体；随后只两行章提示；理由：黑有时间重量，短提示只提出未来缺口，不展示答案。
- Background：纯黑，禁止恢复ticker/世界glitch；理由：建立身体动作的可达空间/距离；不是抽象信息图。
- UI：不仿官方启动品牌；Text：Insert Chapter 7 / Side B；短词/名字或明确作者问题；非歌词/新增角色对白。
- Character：Kris，original geometric rough blocking; production art pending；SOUL：黑场不叠SOUL。
- 连续动作：4970–4994全黑24帧；4994–5002淡入；5002–5029短字hold36帧范围。
- In：完整24帧黑，不继承DSHchime；Out：提示退，Kris衣袖与心回低光。
- Colour：['#070A14', '#75A58B', '#C7E4EC', '#F04462']；Effects：少量接触光/水纹；拒绝靠generic glitch提升预算；纯黑区无后期残影。
- 复用：film/tui_pv_world_execute_20260926/tuikit.py:font / film/tui_pv_world_execute_20260926/continuity_full_v2/cuts.py:independent carrier/mask principle (design reuse)；KEEP整数timing/分层；REPLACE静态左右pane与哲学分支图；REMOVE常驻ticker/舞者。
- 实现：film/deltarune_poc/scenes.py:chapter_cut / film/deltarune_poc/stage.py:posed_characters / film/deltarune_poc/renderer.py:frame；PIL，零旧monkey patch；HTML不必需；生产原创透明asset可后替换。
- 素材：rough geometry; game visual R01–03 / production art pending；仍待：终屏转录待R03精确版画面核对；不画未发布章节。
- QA frames：[4970, 4982, 5000, 5029]；关键事件：['K10']。

### PV39 — 谁在执行谁 / BREATH

- 时间：[5030,5086)；209.583333–211.916667s；legacy ['DR66', 'DR67']。
- Song cue：未解决的余韵；line IDs []；所有word/frame锚点在JSON。
- Chapter/Route：1–5 / author unresolved question；E E01 E04 E18 E33 E35 E36；原创导演staging/主题剪接；非游戏连续录像或新增canon。
- 必要性：问题在迟疑手/心之后才到来，调用身份不固定成胜负。
- Player：可等待/离开，不能提供未来章节；Kris：手/衣色仍使Kris成为最终主体；Other：不接管最后主体位置；Story：实体屏幕/章节断点是作者的上游边界隐喻。
- Camera / spatial novelty：5030起绿色衣袖和同一心，接触未完成；5051起作者问题，hold至5086。
- Foreground：Kris绿色衣袖/手与同一心，接触留空隙；理由：问题在迟疑手/心之后才到来，调用身份不固定成胜负。
- Background：黑/低光，不重新套上哲学框；理由：建立身体动作的可达空间/距离；不是抽象信息图。
- UI：无技术metadata；Text：Who executes whom?；短词/名字或明确作者问题；非歌词/新增角色对白。
- Character：Kris，original geometric rough blocking; production art pending；SOUL：心与手均在，未作下一章决定。
- 连续动作：5030–5048手/心显；5048–5051保持未接触；5051–5057作者问题显；5057–5085hold，不闪不返黑。
- In：提示退，Kris衣袖与心回低光；Out：5086 exclusive片结束。
- Colour：['#070A14', '#75A58B', '#C7E4EC', '#F04462']；Effects：少量接触光/水纹；拒绝靠generic glitch提升预算；纯黑区无后期残影。
- 复用：film/tui_pv_world_execute_20260926/tuikit.py:font / film/tui_pv_world_execute_20260926/continuity_full_v2/cuts.py:independent carrier/mask principle (design reuse)；KEEP整数timing/分层；REPLACE静态左右pane与哲学分支图；REMOVE常驻ticker/舞者。
- 实现：film/deltarune_poc/scenes.py:unresolved / film/deltarune_poc/stage.py:posed_characters / film/deltarune_poc/renderer.py:frame；PIL，零旧monkey patch；HTML不必需；生产原创透明asset可后替换。
- 素材：rough geometry; game visual R01–03 / production art pending；仍待：作者文字不是游戏角色台词；最终美术/情绪仍待验收。
- QA frames：[5030, 5042, 5058, 5085]；关键事件：['K11']。

## 连续关键事件

下列帧是PV导演动作，不是game tick。事件贯穿身体、同一心和摄影机；不可用替换poster冒充动作。

### K01 — identity_reassignment / PV02

| [a,b) | 连续动作 |
|---|---|
| 130–142 | 灰vessel退，心保持身份 |
| 142–156 | 绿色Kris身体显露，主体非输入表格 |
| 156–177 | hold同一锚点，无第二SOUL |

### K02 — SOUL_separation / PV17,PV18

| [a,b) | 连续动作 |
|---|---|
| 2644–2650 | 手靠胸，心仍inside |
| 2650–2662 | 同一心沿胸→手路径 |
| 2662–2674 | 越胸边/连接断，身体不消失 |
| 2674–2693 | 手带心到笼位置 |
| 2693–2728 | 心在笼移而身体不跟 |
| 2728–2754 | Kris独步，camera同时保心 |
| 2754–2784 | hold两个独立运动者，禁止cut海报 |

### K03 — control_reentry / PV20

| [a,b) | 连续动作 |
|---|---|
| 2928–2940 | choice在房内竖成门 |
| 2940–2972 | 同一心从vent跨菜单入口 |
| 2972–2996 | 穿房内至胸；body/heart锚点连续 |
| 2996–3014 | 重入接触后hold，私域暖光被挤 |

### K04 — weird_lock_in_and_recoil / PV22

| [a,b) | 连续动作 |
|---|---|
| 3093–3117 | 手腕接近，尚有拒绝间隙 |
| 3117–3149 | 接触红裂，角色脸不猎奇 |
| 3149–3185 | 一次抽出/落容器 |
| 3185–3209 | 一踢，震动回到身体 |
| 3209–3232 | hold代价，不写free |

### K05 — story_spatial_reveal / PV35

| [a,b) | 连续动作 |
|---|---|
| 4654–4734 | 湖/身体缩入有厚度CRT表面 |
| 4734–4814 | camera露input plug/机身，操作点也在表面 |
| 4814–4863 | hold可辨Kris，禁止再套大白框 |

### K06 — character_control_handoff / PV27

| [a,b) | 连续动作 |
|---|---|
| 3902–3938 | HERO穿屏面，背景mask不裁carrier |
| 3938–3962 | camera追HERO而Kris留边缘，control未返回Kris |
| 3962–3988 | hold错误中心，攻击方向接近他者 |

### K07 — protection_then_disconnection / PV28

| [a,b) | 连续动作 |
|---|---|
| 3988–4000 | 攻击预示，SOUL未换位置 |
| 4000–4012 | Kris手先动 |
| 4012–4030 | 拉Susie离开旧位，camera抢回 |
| 4030–4040 | 攻击只落旧空位 |
| 4040–4052 | Susie伸手到connector |
| 4052–4064 | 断controller连接，HERO退显 |
| 4064–4072 | hold同一SOUL与两身体 |

### K08 — character_world_reverses_input / PV31,PV32

| [a,b) | 连续动作 |
|---|---|
| 4259–4319 | Noelle手越向input源，连接方向反转 |
| 4319–4344 | choice被带入角色世界 |
| 4344–4430 | Stop可读/留差异痕，身体仍小前移 |
| 4430–4436 | hold原两词 |
| 4436–4442 | Stop退字，心不换身份 |
| 4442–4448 | 同文Proceed出现 |
| 4448–4460 | selector左→右，body不同节奏 |
| 4460–4519 | 手迟疑，4495peak不遮主体 |

### K09 — cease_is_not_a_button / PV33,PV34

| [a,b) | 连续动作 |
|---|---|
| 4519–4531 | 输入pulse不再到来，SOUL仍在 |
| 4531–4543 | 关切反射显，冷痕未抹 |
| 4543–4574 | hold后果，不给pause按钮 |
| 4574–4601 | 继续侧手势再次要求确认 |
| 4601–4621 | 第二确认收缩；停止痕迹仍在 |
| 4621–4654 | 世界影响UI读区，准备CRT揭示 |

### K10 — final_hard_cut / PV37,PV38

| [a,b) | 连续动作 |
|---|---|
| 4929–4935 | 最后歌锚点亮接点 |
| 4935–4962 | Kris手/心hold |
| 4962–4970 | 收画布，4969只1px |
| 4970–4994 | 纯黑24帧，无chime |
| 4994–5002 | 章提示淡入 |
| 5002–5030 | 未来空位hold，不画下一章 |

### K11 — unresolved_hand_then_author_question / PV39

| [a,b) | 连续动作 |
|---|---|
| 5030–5048 | 绿色衣袖/同一心低光显 |
| 5048–5051 | 接触未完成，留空隙 |
| 5051–5057 | 作者问题淡入 |
| 5057–5086 | 末帧hold，无结局判定 |

## 导演验收边界

本版情绪曲线、全部67镜去向及删除理由见09。数据覆盖/技术pass不代表最终音乐PV成立；第二轮目视反馈与完整rough review见10。无自备歌曲所以始终 AUDIO REVIEW PENDING。
