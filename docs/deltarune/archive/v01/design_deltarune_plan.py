"""Authoring source for the v0.1 shot plan. No lyric text or game assets.

Regenerates data/deltarune_shot_plan.json and docs/deltarune/06_SHOT_BIBLE.md.
Every row is a directed shot, not a generated filler. Frames are half-open.
"""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
TUI = "film/tui_pv_world_execute_20260926/"

# Agency descriptions are directorial emphasis, not measurements of canon.
STATES = {
    "offer": ("输入可定制，但主体选择最终被收回", "尚未出现；Kris身份将由切换揭露", "未出现", "creation/discard流程决定可接受主体"),
    "normal": ("可帮助、选择，不能替角色决定所有回应", "有身体/偏好，选择与表达可能不同", "可拒绝或主动合作", "菜单提供有限行动与已设结果"),
    "separate": ("仍可移动SOUL，暂不能指挥Kris身体", "身体继续自主行动，动机不替其裁定", "私话/世界动作不由当前输入直接操纵", "scene/空间边界仍规定SOUL可达范围"),
    "nested": ("在Kris与小游戏之间切换控制对象", "可抵抗输入、保护他人、退出某控制链", "Susie可介入；舞台规则也约束角色", "越界须经过游戏已有障碍与触发器"),
    "weird": ("输入影响强但维持路线条件严格", "被代行命令并保留局部抵抗/反冲", "Noelle拒绝/执行/察觉不同声音", "规定命令与锁定限制其他解法"),
    "reverse": ("可移selector但当前两项结果趋同；仍可停止输入", "动作迟缓/手迟疑，动机未知", "Noelle主动要求旧命令并否定拒绝", "湖段先收窄选择，再以时限要求持续确认"),
    "halt": ("停止输入可改变这段进程，不抹除后果", "身体/关系仍留痕，非全部恢复", "Susie关切；Noelle既往变化仍在", "续章及成功提前结束都是已编写出口"),
    "boundary": ("可继续等待或离开，不能提供未发布的下一章", "主体被留在边界内，未来未知", "他者不接管最后主体地位", "Chapter/route接口接住越界；Story是作者隐喻"),
}

LAYOUTS = {
    "split": {"camera": "固定1280×720；左主体24,56,384,604，右世界404,56,1164,604；上框/底带不随镜头变换",
              "reuse": [TUI+"continuity_full_v2/kit.py: transparent her_layer/chrome separation (design reuse)", TUI+"tuikit.py: font/scale_alpha/post"],
              "new": ["dr_ui.control_pane", "dr_ui.kris_study", "dr_layers.world_body"]},
    "full": {"camera": "世界占满24,56,1164,604；Kris必须在世界中有锚点；控制框可退到边缘，底带固定",
             "reuse": [TUI+"continuity_full_v2/v2.py: FULL_ART slide staging (design reuse)", TUI+"tuikit.py: post"],
             "new": ["dr_layers.full_world", "dr_timeline.integer_slide"]},
    "nested": {"camera": "右侧世界内再置TV内框；左侧Kris维持同尺寸；跨界对象不缩放chrome",
               "reuse": [TUI+"continuity_full_v2/cuts.py: Frame/content/over concept", TUI+"continuity_full_v2/kit.py: carrier positioning (design reuse)"],
               "new": ["dr_layers.inner_game", "dr_layers.hero_carrier", "dr_timeline.control_target"]},
    "close": {"camera": "右世界占主要面积；左仍留Kris胸/手轮廓；选择框最小字高24px；心不被glow盖住",
              "reuse": [TUI+"tuikit.py: font/post", "film/pv_dsh_frontend_20260927/dsh_her.py: LEAD readability principle (design reuse)"],
              "new": ["dr_ui.choice_box", "dr_layers.hand_detail", "dr_timeline.choice_events"]},
    "black": {"camera": "全黑；仅保留一个中央边界/问题及低亮Kris手；无ticker、无词带假唱词",
              "reuse": [TUI+"continuity_full_v2/v2.py: HARD_CUT integer4970 (timing reuse)"],
              "new": ["dr_layers.chapter_boundary", "dr_layers.final_question"]},
}

# end frame, title, section, chapter, route, evidence, state, layout,
# semantics, purpose, foreground, background, UI, text, SOUL, motion, transition-out, open question
ROWS = [
 (43,"连接先于身体","connect","1","opening","E01","offer","full","启动供电","先让观众体验输入的到来","中央一点红心；未出现角色","黑色空场与微弱水平线","只有外框四角","CONTACT（游戏窗口概念）","由一点长成几何心","1–8帧红点出现，随后心轻浮；无random glitch","水平线变成白框边","首帧是否要0还是首词frame1：目前0黑/1显现"),
 (93,"保护的双义","connect","1","opening / visual foreshadow","E01 E04","offer","full","安全保护与边界","保护图形以后回成囚心的cage","红心位于未闭合白框","四角缓慢连接，无角色","框内输入仍可移动","无","中心到左侧，尚无身体连接","白框从四角闭合，保留一边缺口","框角拆成vessel零件","这是作者预示，不伪装opening实有cage"),
 (130,"可以制造的形状","connect","1","opening","E01","offer","split","零件排列","先授予可定制的错觉","灰头/躯干/腿的几何部件","左pane形成，右三个部件位置","稀疏选择格","HEAD / BODY / LEGS（菜单短词）","selector依次定位三个部件","部件按2次beat定位，禁止角色鬼脸","零件贴合到左主体槽","vessel不使用导出原sprite"),
 (177,"接受主体","connect","1","opening","E01","offer","split","对象被创建","输入只决定临时vessel，不等于Kris","灰色vessel组合轮廓","右侧空的角色世界框","接受位置被心指向","ACCEPT（短菜单）","心落在接受项，线连临时身体","轮廓合并，不发胜利闪光","选择格延展为参数行","不要暗示这个vessel将在本PV拥有自主剧情"),
 (243,"身份表格","connect","1","opening","E01 E02","offer","split","填写参数","身体信息和creator name是不同层","左vessel轮廓，右name两栏","无DarkWorld截图","名字卡和光标","VESSEL / CREATOR（作者分类标记）","在两行之间移动","name卡滑入，轮廓保持不动","表格突然失去vessel栏","不显示虚构输入者姓名"),
 (269,"收回选择","connect","1","opening","E01","offer","close","初始化的断点","最早的自由收回发生在路线分歧之前","vessel槽变空；Kris轮廓接入","白框完整而选项消失","输入格退到框外","KRIS（主体名）","原selector停在空格，身体不由它改形","243–248淡去vessel；249–254显Kris；255以后hold","黑空格扩为房间","discard文字不贴整句原对白"),
 (306,"世界已有其人","connect","1","normal","E01 E02","normal","split","新世界建立","Kris已有身体/家庭空间，非从零人格","Kris遮眼轮廓与手","程序化卧室地面/窗/门","输入小框出现于左上","无","心由menu进入胸口位置","窗光从右进，不把Kris改成噪声","门的白线延展成道路","房间布局是原创概括，非游戏像素复刻"),
 (385,"输入与行动","connect","1","normal","E03","normal","split","开始可行动的世界","先建立控制可带来共同探索","Kris沿右向路径走，左保留主体框","门连到一条可走的地图线","四方向点一次，右侧响应一次","无","胸口心随身体位置，输入来源在屏外","两次清晰input→step，0.2s以内回应","路径延长，镜头驻留","不能把映射延迟说成游戏实际输入延迟"),
 (476,"一起向前","normal","1","normal","E03","normal","split","器乐第一次舒展","在冲突前建立帮助/信任","Kris居中，Susie远端影子","DarkWorld简化地面无敌人素材","ACT/SPARE格只作可选动作grammar","ACT / SPARE","心选一项，白线由Kris连到他者","角色轮廓相距一pane，不跑动刷屏","合作线遇到另一条自发动作线","具体combat复刻等后续游戏QA"),
 (567,"不接受命令","normal","1","normal","E03","normal","split","器乐动作重拍","他者不是永远服从Player","Kris手留在指挥位置；Susie自发前冲","battle地面和空目标格","Susie的命令位置退灰，自动攻击轨迹仍亮","无","仍指menu，不能随她攻击轨迹走","按键闪一次、她从自身位置动作一次","两条轨迹分开后重新靠近","不画Susie永远不受控；下一镜必须回合作"),
 (655,"合作是关系变化","normal","1","normal","E03 E19","normal","split","器乐回收","从拒绝到主动共同动作","Kris和Susie轮廓站同一地面","右世界框暖光恢复","选择位置可读但不是占有许可","无","心回Kris，不新增Susie soul","白连接改双向，角色各停一步","双向线落入SAVE卡","不要让双向图解变成canon灵魂机制"),
 (715,"谁的存档名","normal","1","normal","E02","normal","close","器乐末尾停驻","控制记录不等同身体身份","Kris仍在卡旁，手不变","SAVE单slot从右世界浮出","Kris name层被creator层覆盖","KRIS → CREATOR（作者示意）","心停在SAVE动作位置","只做一层名字覆盖，保留身体轮廓","slot像素拆成身体点云","首次SAVE概念，非多周目全角色记忆"),
 (803,"点与身体","identity","1 / 4","normal / thematic crosscut","E01 E21","normal","split","以点集定义自己","可计算形体不等于可拥有意愿","点落成Kris衣/手，脸无写实表情","右pane相同点密度栅格","选中一片点而不是人格面板","无","心有具体位置，不随全点归类成模型","稀点到实轮廓；手在点归齐前先动","点环绕身体成一个圆","不使用旧whale点云采样源"),
 (890,"圆内可选","identity","1 / 5","normal / motif foreshadow","E04 E33","normal","split","圆与边界长度","有多个位置未必有多个结果","Kris位于环外、心在环内","圆形menu路径","4个位置相同边框，结果暂未露","无","沿弧从一端到另一端","圆旋转但Kris静止，避免眩晕","圆展开为两条并行波","这里仅预示，不能提前宣称所有选项都一样"),
 (980,"同一波不一样的手","identity","4","normal","E21","normal","split","波形和可接触轨道","输入与Kris已有能力可共存","Kris手对着简化键盘","一条输入波和一条奏乐动作波","小方向格，不放虚构乐谱","无","胸口心稳定，手不完全随selector","两波开始同相，后半手的节奏微提前","波延长撞到最右边界","运动提前是作者隐喻，不是游戏时延事实"),
 (1066,"无限仍在框内","identity","1 / 3","normal / sword motif","E01 E15","normal","full","趋向无限与限制","扩展可达空间仍受边界","Kris沿路径站在左三分之一","网格往外伸，外白框再次出现","选择格仅显示当前两格","无","心接近框角，身体不穿框","远景增格不增加字号，最终框阻止路径","frame1066电路切向内屏幕","不要把原数学科普参数留在DR画面"),
 (1145,"切换控制通道","nested","3","common / nested motif","E13","nested","nested","切换电流方向","控制者也坐在别人的规则里","左Kris手握抽象controller","右世界里一台无品牌TV框","屏外input→Kris→内游戏连接","无","由胸到TV中心的示意连线，不多出第二颗主心","连线方向分段点亮","TV边框加粗挡住外侧信息","controller图形原创，不打包游戏道具sprite"),
 (1235,"只能看此处","nested","3","sword","E13 E15","nested","nested","视野关闭与眩晕","局部视角不能等于世界全貌","Kris仍可见，内游戏角色往边缘走","TV内小地图、TV外DarkWorld地面","内框裁掉越界方向","无","小心留在内selector位置，主身体层不全黑","TV内轻旋≤2度，外层稳定","小地图展开为SAVE时间格","旋转是作者视觉语法，不复刻角色晕眩事实"),
 (1322,"时间也是接口","nested","1 / 3","normal / thematic crosscut","E02 E15","nested","split","前后时间位置的旅行","改变记录受slot/route条件限定","Kris在固定身体位置","两张相同slot先后覆盖","SAVE时刻格不显示虚构chapter6","SAVE（短词）","停在当前slot，不分裂成多玩家","已选路径留下淡线，回退卡不让他者苏醒","时间格变成party连接位","不得暗示Kris记得每次reload"),
 (1417,"靠近不是合并","normal","1 / 3","normal / thematic crosscut","E03 E19","normal","split","结合与亲近","三人仍有各自行动方向","Kris前景，Susie/Ralsei小影子","同一地面，没有舞台统计","菜单退到边缘，世界略亮","无","留Kris胸口，线能回馈却不吞并角色","角色靠近后保持一身宽间距","三条线成为并列可能性","Ralsei只承担合作，不加管理员暗示"),
 (1513,"可提供的可能性","normal","2","normal","E06 E07","normal","split","可能世界与满足","Player想帮助也可能误判结果","Kris手对着三条候选细线","NEO线的原创新几何轮廓，只一镜前示","ACT选择浮出，其他格淡退","无","心选snap概念位置","候选线依次伸至同一身体轮廓","选中的线抬起，其他线退","NEO是主题镜子，不发展成boss介绍"),
 (1591,"最后一根","normal","2","normal","E06","normal","close","满足的条件","操作上成功不保证自由有支撑","Kris手/心与一个悬吊小轮廓","只剩一根绿白细线，非Kris实物线","确认位置在左，线在右","无","selector接近确认，未消失","hold至少12帧后断线；下坠不加blood","断线末端落进Kris手边","不配胜利banner"),
 (1683,"动作也可以保护","normal","3","sword / thematic crosscut","E19","normal","split","快乐与运行行动","Kris不是所有命令的顺从延长线","Kris手拉Susie离开内游戏攻击路径","小TV框保留淡边，标此处是重访","危险轨迹与拉开轨迹分色","无","在攻击接口，身体手另行动","攻击线到达前手先横向带走他者","保护的线回成NEO断线","不同章节交叉，不声称发生于同场战斗"),
 (1774,"落空的自由","normal","2","normal","E06 E07","normal","full","仍受困的模型","解绑与可行动不是同一个变量","NEO轮廓小幅坠落；Kris接住视线非身体","DarkWorld地面，断线在上","控制menu仍在边缘，不假装关闭世界","无","停在已按位置，Kris胸口示意不叠第二心","坠落12帧、后停留；无随机碎片","断线重组成键盘线","不是角色死亡/虚无的断言"),
 (1865,"供给的能力","care","4","normal","E21","normal","split","给予营养的功能","供给词被映射为有个性的能力","Kris奏乐手与遮眼头","原创organ键格，音波进入右世界","输入格很小、可退","无","稳定留在Kris层","手指按两键、身体不消失于谱线","波纹变成另一人的返向光","不逐字复制蔬果素材，不虚构喂食情节"),
 (1951,"给予不等于讨好","care","5","normal","E30","normal","split","供给保护的功能","自主行为也能关照友谊","Kris与Susie小轮廓走在同一地面","原创新街道/归家路径","拒绝格淡于世界路径","无","漂浮于一只轮廓balloon中，身体另走","balloon随风轻移，Kris步伐稳定","路径弧变成回波纹","属于normal条件分支，不放在weird lake同一时间"),
 (2043,"角色的回应","care","1 / 5","normal / thematic crosscut","E03 E30","normal","split","让他人快乐的功能","别人可以回应Player也可以回应Kris","Kris左、Susie回头的小动作","温灰地面替代恐怖氛围","可用选项不持续滚动","无","低亮但不降到看不见","回波从他者到Kris手，主体先回应再UI","回波进入SAVE名字框","不编写新游戏对白或love confession"),
 (2125,"存在不靠所有权","care","1","normal / author metaphor","E02","normal","close","唯一存在与证明","creator和角色不能互相吞没","Kris轮廓与两张name卡","卡下保留身体影子","SAVE卡上下两层","KRIS / CREATOR（作者标记）","在保存位置，不能把名字变成脸","两name层接近但保持2px缝","name卡白边变衣服色带","Player不是本作创世神的canon结论"),
 (2205,"同一个人","care","1 / 2","normal / author metaphor","E01 E05","normal","split","身份属性切换","不让歌曲身份词抹掉Kris","Kris同一遮眼/手，衣色域变化","Light暖灰与Dark靛蓝分界","输入没有gender selector","无","留同一身体锚点","只切环境与衣色，不切身体身份/性别","窗光从亮切暗","Light/Dark具体角色美术待原创新设计"),
 (2295,"日夜之外的动作","care","2 / 5","normal / thematic crosscut","E05 E29","normal","split","一天时段与不同活动","Kris在输入间隙仍有动作","Kris手靠窗，另一手暂藏SOUL","夜窗/日窗只作时间背景","输入框暗下，世界继续","无","局部被布边遮，但不画彻底断电死亡","手关窗6帧，心漂移受容器限制","窗外框变TV舞台框","不要给离体时长具体生理解释"),
 (2382,"舞台角色套住输入","nested","3","common","E13","nested","nested","角色切换的关系","Player进入Kris、Kris又被节目定位","Kris留左，内TV的角色格在右","节目舞台只有框/聚光，无Tenna整幅图","内层controller状态","无","输入轨迹依次经过三个框","同一move分三层显示，不三心分裂","舞台轨迹变奏乐键格","不保留原S/M直译，更不重写角色性别"),
 (2485,"能力与输入共存","care","4","normal","E21","normal","split","进入感应与专注","角色不是无输入就无能力的空壳","Kris手按organ，肩姿与input不同步","只两道音波，背景空净","choice框退后，不写AI参数","无","胸前亮、手主动动作","每beat肩动1px、手独立按键","两个节奏逐渐同相","不是声称Ch4全部演奏无Player作用"),
 (2571,"共同振动","normal","1 / 4","normal / thematic crosscut","E03 E21","normal","split","感应与共振","合作可以发生，不需要消灭一方意志","Kris手与伙伴轨迹","右世界有可走的地面","菜单保留两种不同选项","无","身体心和menu选择只用接触闪示意","input波落时动作波相接，hold6帧","连线包围身体成为完整轮廓","保留作者比喻标记于metadata"),
 (2650,"完整不是拥有","normal","1 / 4","normal / thematic crosscut","E03 E04 E21","normal","full","完成的感觉","在分离前给连接真实情感重量","Kris完整轮廓站右世界近中心","暖细光与空地面，无人数统计","menu存在但弱亮","无","胸口亮，接触边缘不放大满屏心","身体停一拍，最后6帧手靠胸","进入分离手势，场景暖色退","此处非宣称游戏特定chapter终局"),
 (2693,"离开身体","separation","1","ending","E04","separate","close","第一次离开","失去control并不让Kris消失","Kris的手抽出红心","左pane仍有身体轮廓","输入框与身体间连线断一段","无","从胸口到手外，手比selector先运动","2650–2655拉出；2656–2661离胸；之后hold","输入框停止响应身体","不是宣布Kris认识现实Player"),
 (2718,"输入仍在","separation","1","ending / author staging","E04","separate","split","再次离开","观众仍能操作心的位置却不能身体","Kris保持右向朝向","左主体pane轮廓/右心的空间不同","小方向input仍亮，身体行不亮","无","右移一步，Kris不跟随","方向格闪一下只移动心","身体和心的两个区间分开","UI拆除是作者结构，不是游戏实际CSS"),
 (2734,"世界不跟输入退场","separation","1","ending / author staging","E04","separate","split","第三次离开","连接断裂不是整个角色世界结束","Kris肩和手仍有动作","世界地面留下，输入pane边线收回","退一个框角，底带保留","无","悬于右边，不能变箭头样另一心","框角8帧退去，身体保持","心进入实体容器轮廓","不能把黑场叫Kris死亡"),
 (2754,"保护变容器","separation","1","ending","E04","separate","close","第四次离开","回扣开头白框的双义","Kris轮廓在cage外","与02相同四角变cage格线","menu框让位给物理cage","无","在cage内可左右移不穿边","十帧心移向边、边阻住","Kris手离开cage，身体向外","原game birdcage形状以后原创新美术"),
 (2784,"身体独自行动","separation","1 / 2","ending / thematic crosscut","E04 E05","separate","full","第五次离开","离开输入不等于善良/邪恶判决","Kris向世界深处自主一步","cage在小角落仍可见心","input只照角落","无","留容器，不随Kris走","Kris一步16帧；input脉冲只让心一像素动","房间门白线接到vent","不画邪恶笑或Knight身份暗示"),
 (2838,"隔离是空间问题","separation","4","common / thematic crosscut","E20 E23","separate","split","隔离的结果","从完全断开转为可窥视有限空间","Kris远处门内影子，SOUL在vent","gift-room/vent三段原创线布局","input受vent通道裁切","无","沿L形通道走，到门内视线边缘","身体不重绘成当前心，心贴通道","私话层慢亮","章1→章4是主题cut，不是一条连续房间"),
 (2928,"不是菜单制造的声音","separation","4","weird / remembered report","E23 E25","weird","split","旧片段与可抹去的痕迹","Kris离开输入时也有关系/表达","Kris与Noelle门内影子面对面","门外vent里红心；门内暖色残留","私话没有player对话按钮直到尾段","VOICE / KRIS（作者回忆标记）","留vent，choice末尾出现靠近房内位置","熟悉声波从Kris发出；红input波与其不同形","choice框跨过vent边界","道歉由Noelle回忆，画法标remembered，非证实镜头目击"),
 (3014,"菜单是一扇门","weird","4","weird","E24","weird","close","希望把连接取回","Player选择物理位置，重新占住输入接口","Kris手/胸口在门内；Noelle保持另一侧","vent与房间边界连续","Proceed在房内，拒绝位置留vent","Proceed / ...（短选项grammar）","从vent跳choice位置再移动到Kris胸前","2928–2933迁移；2934–2941进入房间；2942–2947接触；之后重入","连接重新形成但右世界暖色退","精确游戏layout/time limit待R02，不沿用游戏tick当PVframe"),
 (3093,"偏离也有条件","weird","2 / 4","weird / thematic crosscut","E08 E24","weird","split","挑战上游的规则","强力影响与狭窄可选结果并存","Kris轮廓/手，Noelle远景","一条backtrack路线过三个门槛","required输入格逐个关闭其他分支","无","按条件路径移动，每到门槛停一帧","路径折返、正确输入开门但外框不变","门槛落成ring锁定边缘","不把剧情条件写作真实游戏code snippet"),
 (3149,"路线锁定的代价","weird","4","weird","E25 E26","weird","close","参数不再被接受","锁定经由Kris手施加给Noelle","Kris手与Noelle手腕轮廓，ring只作红裂线","人物脸退远不作猎奇","option分支合并后锁线闭合","无","仍在命令位置，身体手运动与心不是同一物","3093–3101抓腕图形；3102–3110裂线扩展；之后hold","红线回冲至Kris胸边","采用当前red crack意象，原像素/玫瑰动画不混合"),
 (3232,"反冲到接口","weird","4","weird","E26 E28","weird","split","不合法动作与冲突","Kris反击连接却仍承受自身代价","Kris脚/手把SOUL放进垃圾桶意象","程序化浴室容器和稳定地面","input框停留但暗，底带保留","无","落入容器，被震动而非消失","一次抽出、一踢、震动回到心，随后停止；不反复自伤爽感","容器框变倒下身体边线","不给反冲加自由胜利文本"),
 (3323,"命令没有随身体倒下","weird","2","weird / thematic crosscut","E09 E12","weird","split","器乐第一层压力","异常声音的来源不等于当前身体动作","Kris低姿态，Noelle远端仍面向命令","冰白小空间保留battle线","命令格仍亮但Kris手不动","无","menu接口仍可见，不作魂出窍生理说明","input波越过倒下Kris到Noelle，身体不给同步走动","输入波形成小游戏控制线","DOWN不是死亡，不能画grave碑"),
 (3412,"逃离需先拿到钥匙","nested","3","sword","E15 E16","nested","nested","器乐第二层压力","越界被关卡设计引导，不是作者随意glitch","Kris手握controller，HERO_SWORD在内层","简化board障碍/门，不放原地图","输入下箭头与角色向上阻力","无","内游戏control中心，Kris肩仍有动作","上下两方向冲突重复两次，角色不穿墙","门上边界延展成第二框","不凭shelter门下结论说Kris是Knight"),
 (3549,"框外还有框","nested","3","sword / author metaphor","E15 E16 E18","nested","full","器乐蓄压至执行前","Player的越界愿望仍落入可实现区域","Kris靠左内边，内游戏小人靠第二边","被剪开的第一框外有另一个相同框","choice/门槛符号消失但边界留","无","随小游戏对象移动，身体锚点不变","3412–3423出第一框；3424–3435新外框显；之后hold","第二框回缩成execution命令格","此镜越界空间是PV隐喻，不声称游戏无限套娃"),
 (3682,"命令一至六","execution","2","weird / condensed replay","E08 E10","weird","split","重复执行前半","让每次命令可读为再选择而非杀敌爽点","Kris的手留前景，Noelle施法方向远端","冰空位逐个留下，非具体六只敌人名单","单命令格pulse-index六次","无","每起音轻接触menu，仍同一心","line67–72起音各一次框收窄，12帧以内hold","同格继续，不切换六张游戏画面","六pulse是歌曲计数，不是canon杀敌数"),
 (3821,"命令七至十二","execution","2","weird / condensed replay","E10 E11","weird","close","重复执行后半","重复越过拒绝，身体与命令归属渐分","Kris手更僵，Noelle手势停在执行方向","Berdly空位/冰几何一次，不能每拍死亡","拒绝的可见空间减少，菜单仍相同","无","每起音压一次选择位置，位置并不等于意志","line73–78各pulse；frame3795末次后hold至3821","输入归属从身体旁迁到UI边","末第12起音3795保留在本镜，不与计数混算"),
 (3902,"谁发出最后呼唤","execution","2 / 3","weird / sword thematic crosscut","E11 E18","nested","nested","多语言计数与呼唤归属","叙述主语和control对象可以改变","左Kris不动，右小游戏HERO形状待跨界","计数格不是chapter列表","主体状态格与input格分离","KRIS / YOU（作者主语标记）","从Kris接口迁向小游戏对象的control轨迹","79–81三组轻计数；82收束","HERO脚步到TV白边","不配现实人发声、不宣告YOU=全知玩家"),
 (3988,"走出屏幕","execution","3","sword","E18","nested","nested","把执行交给他者","输入对象不再与Kris绑定","HERO_SWORD跨TV边；Kris退后保持主体大比例","TV内地面与外地面断口同高","left input连接新对象，Kris接口空","无","control载体跟HERO，不能另生第二心","3902–3907至边；3908–3913跨边；3914–3925Kris后退；之后hold","HERO前进方向转向Susie/Kris","R01连续录像未看，先画关系geometry"),
 (4072,"Kris会保护别人","execution","3","sword","E19","nested","nested","执行作用反转","Kris不只抵抗，也能给他者留空间","Kris把Susie拉出HERO攻击线","外TV/内游戏地面同框","controller线最终被拔，input仍存在于框外","无","失去当前对象，不退化成死心","3988–3995攻击线接近；3996–4003拉离；4004–4011断线；之后hold","断线落为四空选项","不声称Kris用这动作使全游戏自由"),
 (4164,"归来的空白","execution","4","weird / thematic crosscut","E27 E28","weird","close","取回接口与再受困","恢复输入不保证能表达自己的答复","Kris胸/手，Susie提问姿态小影子","雨线暂停只作为原场景意象","四个空白slot；不是四个隐藏回答","无","selector可移动但文本为空","4072–4083框显；之后slot高亮变化而Kris不说话","四格收成起床方向格","不把blank选项填成作者希望的Kris独白"),
 (4259,"起床的阻力","reverse","5","weird","E31","reverse","split","受困反复","输入多却只换来小幅身体进度","Kris床上起身轮廓，手勉强落地","简化卧室床/地面，后窗暮色","方向input重复，身体进度小","无","在胸前微弱，方向input红边一次次亮","每两次pulse身体上抬1px；无机械数值百分比","暮光延展为湖面水平线","动作动机未知，不给抗议独白"),
 (4344,"她开始索求命令","reverse","5","weird","E32","reverse","split","学习关系的方式","Noelle的主动并不证明已自由","Kris近景手迟疑，Noelle远端手向左伸","湖面+岸边无终末戏剧云","choice框由Noelle方向滑向心","无","被索求的接口留于框内；身体不主动扑向她","Noelle手到Kris腕前，线由她向menu发出","choice框停为两项","不把受创伤的主动浪漫化成爱情救赎"),
 (4430,"拒绝仍然向前","reverse","5","weird","E33","reverse","close","被质问并作答","Player的当下拒绝与既往施压发生冲突","Kris手颤/轮廓仍为主要面积；Noelle手引向湖","湖面抬高一小层；岸线仍在","Stop/Proceed同时可读，心先落Stop","Stop / Proceed","在Stop项，身体仍前进微步；留下一点拒绝痕迹","4344–4355心移动；4356–4367角色前移；4368后hold","文字槽保留，Stop字形开始失去区别","Stop计数留差异；不标完全无效"),
 (4519,"两个位置同一结果","reverse","5","weird","E33 E34","reverse","close","把关系化为表达式","selector还能移动，结果空间却收窄","Kris近景握手；Noelle另一侧维持牵引","湖面与两个菜单槽同宽；外框若隐若现","第7组概念压缩：Stop→Proceed；两槽同文","Proceed / Proceed","由左到右位置可变，frame4495仍看清红心","4430–4435保留Stop；4436–4441文字变形；4442–4447落为Proceed；4448–4518心移位不改变身体方向","外input停顿显现，故事框继续存在","PV压缩prompt次数，非逐一重演73组输入"),
 (4574,"停止也是输入的边界","reverse","5","interrupted weird / counterfactual comparison","E34 E36","halt","split","看似自由的对照","承认不持续按可以改变当前进程","左Kris手留痕；右Susie关切的小轮廓","成功与停止两条路径只以线区分","确认pulse暂停，外框留两个出口","无","停止selector操作，但心不被删除","4519–4530pulse退去；4531–4542续章路径显；之后hold","两路线灰线回到一颗心","图形比较不是canon同时发生的多宇宙"),
 (4654,"继续的代价","reverse","5","weird / compare to interrupted","E34 E36","reverse","close","受困与持续关系的尾唱","继续要求重复确认；停止支线的后果不能抹去","Kris握手仍清楚；Noelle远端将命令推回","逐渐趋白湖面，停止支线只留关切影子","选择同文，时限只有收缩边不写游戏tick","Proceed","红心接近白但保持红轮廓；框要求确认","4574–4600间一次收框后复位；后一次更窄；不把静默关切消失","湖面折成一个框内画面","E34时限不是每组严格单调，不复刻错误线性倒计时"),
 (4760,"把湖留在画面里","boundary","5","weird / author metaphor","E35","boundary","full","器乐收束开始","故事接收越界而非被它击破","Kris手与身体轮廓保留；Noelle退到已发生场景","湖面成为白框内图像","外chapter框出现但不显示未来场景","无","从choice到框边稳定停留","缩小世界frame不缩Kris识别尺寸；手锚点保持","湖框外再长一圈章框","不画湖底新世界/死亡真相"),
 (4863,"上游也有接口","boundary","1 / 3 / 5","cross-route / author metaphor","E01 E15 E35","boundary","nested","尾奏递归","Player控制台也成为路线里的对象","Kris左pane维持；右input框被外框包围","仅三层矩形，不无限缩放难读","menu→route→chapter层位次依次亮","无","最外边心仍能移，不再声称它是最高层","frame4760先亮内框；4800亮route；4840亮chapter","三框间连线退去，留下手","Story是隐喻第四力，不给它角色脸"),
 (4929,"不急于给答案","boundary","5","cross-route / author metaphor","E35 E36","boundary","full","无唱词尾奏停驻","让角色承受与观众思考有停留","Kris手和遮眼轮廓，无他者主视角","三框退到灰白，中心大片负空间","输入可停止的边沿开口仍留","无","静止但非暗灭；闪烁降至无","只湖线每beat1px，Kris不消融为代码","最后单次执行pulse落在外框","这是作者结尾悬置，不编写角色内心结论"),
 (4970,"提交至章节边界","boundary","5","weird / author cut","E35","boundary","full","最后执行和硬切","把操作归于当前章节，而非杀掉Player","Kris最后轮廓与手留下到4969","世界白框在末8帧压成线","章边沿亮一次，不新增红命令","无","4948短接触外框，4969仍留一红点","4929pulse；4962–4969压线；4970切黑（global event）","帧4970硬切","音乐未在本机试听，4970继承上游精确选择"),
 (5004,"要求来自下一层","final","5","weird / chapter boundary","E35","boundary","black","黑场尾音停留","边界仍以chapter/interface语言要求继续","无新人物，美术只留Kris手极低亮","纯黑","小CRT边框，未发布章位置留空","CHAPTER 7 / SIDE B（短提示意象）","框外一小红点，不穿未来门","4970全黑；4982–4993短字显；4994以后hold","章框变回一条连接","完整终屏文字只转录依据，具体画面待R03"),
 (5051,"调用方向未定","final","1–5","author synthesis","E04 E18 E33 E35 E36","boundary","black","音乐停止后的关系残留","不把caller/subject身份固定成胜负","Kris手轮廓与红心，两者间隔至少32px","原初白框，但一角未闭","一条从两端均可起亮的connection","无","停于一端，线从另一端亮一次","5004–5015Kris手显；5016–5027两向各亮一半；5028以后hold","线退成最后问题的baseline","不写execute(player)为真实游戏函数"),
 (5086,"谁在执行谁","final","1–5","author synthesis","E01 E04 E18 E33 E35 E36","boundary","black","尾段保持至片尾","让问题落在保留的角色/输入上","Kris手与红心均留，问题不遮主体","纯黑、最外框开口仍在","无ticker/虚构回复","Who executes whom?（作者文字）","稳定红心，未发送/未作下一章决定","5051–5056问题显；5057–5085hold，不闪烁不返黑","片结束于5086 exclusive","最后字不是Mili歌词也不是游戏对白"),
]

# Critical intervals are in PV frames, NOT original game ticks. These are director's
# staging instructions. Continuous formulas, not stateful previous-frame movement.
EVENTS = [
 {"id":"K01","kind":"identity_reassignment","shots":["DR06"],"start":243,"end":269,"steps":[[243,249,"vessel alpha=1-smooth((n-243)/6);心位置固定"],[249,255,"Kris alpha=smooth((n-249)/6);不创建第二颗SOUL"],[255,269,"hold新主体，输入仍停空slot"]]},
 {"id":"K02","kind":"SOUL_separation","shots":["DR34","DR35","DR36"],"start":2644,"end":2718,"steps":[[2644,2650,"手移到胸口；SOUL仍inside"],[2650,2656,"同一心从胸→手沿线性x路径移12px"],[2656,2662,"手抬心越胸外边，connection alpha降到0"],[2662,2693,"身体保持，心可移；无死亡/自由label"],[2693,2718,"input只移动心；Kris世界位置不由该pulse决定"]]},
 {"id":"K03","kind":"control_reentry","shots":["DR42"],"start":2928,"end":2954,"steps":[[2928,2934,"心由vent位置直接落choice物理槽，边界不断线"],[2934,2942,"SOUL沿房内路径移到胸前"],[2942,2948,"胸口接触：原心缩到内部锚点，线亮，不生成新心"],[2948,2954,"hold已重入状态；Noelle手退，暖光减弱"]]},
 {"id":"K04","kind":"weird_lock_in","shots":["DR44"],"start":3093,"end":3120,"steps":[[3093,3102,"Kris手与Noelle腕图形接近但保留空隙"],[3102,3111,"red crack由接触点扩展；option分支收束"],[3111,3120,"lock线闭合，身体/选择层仍分离"]]},
 {"id":"K05","kind":"world_boundary_break","shots":["DR48"],"start":3412,"end":3442,"steps":[[3412,3424,"HERO越内框，载体在独立RGBA层不裁掉脚"],[3424,3436,"外白框从角显现，主体Kris保持亮度"],[3436,3442,"hold外框与越界对象，拒绝glitch遮挡"]]},
 {"id":"K06","kind":"character_control_handoff","shots":["DR52"],"start":3902,"end":3926,"steps":[[3902,3908,"HERO脚在TV内；SOUL input连接仍到HERO"],[3908,3914,"HERO carrier越白边，tv mask只裁背景"],[3914,3926,"Kris退6px并松controller；control保持HERO，绝不伪装Kris自主攻击"]]},
 {"id":"K07","kind":"refusal_and_other_intervention","shots":["DR53"],"start":3988,"end":4012,"steps":[[3988,3996,"HERO攻击线预示；Kris手先移"],[3996,4004,"Kris拉Susie横移24px，attack线落在原空位"],[4004,4012,"Susie断controller线；HERO透明度归零，心不灭"]]},
 {"id":"K08","kind":"player_story_reversal","shots":["DR57","DR58"],"start":4418,"end":4519,"steps":[[4418,4430,"Stop仍可读，心选中；世界仍向湖方向前进；留拒绝小痕迹"],[4430,4436,"hold二种文字，框不变"],[4436,4442,"左文字缩短/清除6帧；心与Kris不换位置"],[4442,4448,"左字出现Proceed；两项同文，无假Stop出口"],[4448,4460,"心从左至右smooth移位；Kris身体移动量与两位置无关"],[4460,4519,"hold同结果；frame4495作为情绪peak，手仍迟疑"]]},
 {"id":"K09","kind":"cease_input_alternative","shots":["DR59","DR60"],"start":4519,"end":4610,"steps":[[4519,4531,"原pulse停止，不把SOUL物理删除"],[4531,4543,"灰线显示续章出口，Susie关切影子留下"],[4543,4574,"两出口留白；不称事件没发生"],[4574,4601,"返回继续侧一次收框/confirm，另一出口仍有后果影子"],[4601,4610,"后一确认更短；仅为PV压缩，并非全部game timeout单调"]]},
 {"id":"K10","kind":"final_hard_cut","shots":["DR64","DR65"],"start":4929,"end":5004,"steps":[[4929,4935,"最后歌起音亮外框；不是增加一次杀敌"],[4935,4962,"Kris手/心hold，看清边界"],[4962,4970,"画布world高度按clamp((4969-n)/7)收缩，4969保留1px横线"],[4970,4982,"全部黑12帧，无DSH chime"],[4982,4994,"章要求短文本淡入"],[4994,5004,"hold未来空位，不开下一章"]]},
 {"id":"K11","kind":"final_question","shots":["DR66","DR67"],"start":5004,"end":5086,"steps":[[5004,5016,"Kris手低亮显现，心从点回几何形"],[5016,5028,"connection两端各亮一半；不出现方向终判"],[5028,5051,"hold两者，保留最外框开口"],[5051,5057,"作者问题淡入"],[5057,5086,"hold29帧；结束不判角色生死/未来路线"]]},
]


def build():
    timing = json.loads((ROOT / "data/timing/word_timeline_notext.json").read_text(encoding="utf-8"))
    words = timing["skeleton"]["words"]
    shots, start = [], 0
    for idx, row in enumerate(ROWS, 1):
        end, title, section, chapter, route, evidence, state, layout, sem, why, fg, bg, ui, text, soul, motion, out, question = row
        sid = f"DR{idx:02d}"
        pp, kk, oo, ss = STATES[state]
        config = LAYOUTS[layout]
        onsets = [{"line_id": w["line_id"], "word_index": w["word_index"], "source_seconds": w["start"],
                   "frame": round(w["start"] * 24)} for w in words if start <= round(w["start"] * 24) < end]
        # Include line semantic coverage even if onset is in the preceding short shot.
        lines = sorted({w["line_id"] for w in words if w["start"] < end / 24 and w["end"] >= start / 24})
        colours = ["#070A14", "#E7E9F2", "#F04462", "#75A58B"]
        if state == "weird" or state == "reverse":
            colours[-1] = "#C7E4EC"
        shots.append({"id": sid, "title": title, "section": section, "start_frame": start, "end_frame": end,
                      "start_time": start / 24, "end_time": end / 24, "frame_interval": "[start,end)",
                      "song_cue": {"semantic_description": sem, "line_ids": lines, "word_onsets": onsets,
                                   "instrumental": not lines},
                      "chapter": chapter, "route": route, "canon_evidence": evidence.split(),
                      "claim_scope": "依据可见事实的作者镜头设计；非原游戏连续录像或新增canon事件",
                      "narrative_purpose": why, "player_state": pp, "kris_state": kk, "other_character_state": oo,
                      "story_state": ss, "agency_preset": state, "layout": layout, "camera": config["camera"],
                      "foreground": {"description": fg, "reason": "把主体动作/受输入的对象放在第一阅读层"},
                      "background": {"description": bg, "reason": "提供该镜空间边界与关系，避免无意义装饰"},
                      "ui_elements": {"description": ui, "reason": "显现可选行动、输入归属与当前限制"},
                      "text": {"content": text, "provenance": "无" if text == "无" else "短菜单/名称或明确作者标记，非歌词/新增角色对白",
                               "reason": "无则减少信息负担；有则标当前操作或关系，禁止metadata进入作品"},
                      "character": {"primary": "Kris" if idx > 6 else "Kris（主体将揭露；vessel不等于Kris）",
                                    "art_status": "原创程序化轮廓study；最终美术未验收", "reason": "保持Kris为叙述中心；他者只提供对照"},
                      "soul": {"description": soul, "reason": "指示同一输入入口的空间位置，不裁定灵魂本体身份"},
                      "transition_in": "从黑场显现" if idx == 1 else f"承接{shots[-1]['id']}：{shots[-1]['transition_out']}",
                      "transition_out": out, "colour": colours, "motion": motion,
                      "effects": "仅接触点窄glow、低强scanline；冲突段可路线触发glitch，不能遮心/手/选项",
                      "original_repo_components_reused": config["reuse"],
                      "original_elements_decision": "KEEP分层/读区；ADAPT pane/载体；REPLACE原DSH/模型视觉；REMOVE本片舞者",
                      "new_code_required": config["new"] + [f"s_dr_{section}.shot_{sid.lower()}"],
                      "assets_required": [{"asset": "Kris原创轮廓与该镜几何场景", "source": "程序绘制/原创作者设计",
                                           "status": "study可程序化；生产美术与游戏画面核对待完成"}],
                      "unresolved_question": question, "key_events": [e["id"] for e in EVENTS if sid in e["shots"]],
                      "validation_frames": sorted({start, min(end-1, start+6), (start+end)//2, end-1}),
                      "implementation_status": "planned"})
        shots[-1]["technical_implementation"] = {
            "medium":"PIL/RGB + independent RGBA carriers",
            "direct_renderer_reuse":[TUI+"tuikit.py:font"],
            "adapted_data_components":config["reuse"],
            "legacy_monkey_patch":"none in initial DR entry",
            "new_section_path_planned":f"film/deltarune/s_dr_{section}.py",
            "new_components_planned":config["new"],
            "html_playwright":"not required for this shot; only reconsider for demonstrated complex layout need",
            "prerender_asset":"optional original character/setting transparent assets; no exported game sprite",
            "reusable_abstraction":config["new"],
            "proof_renderer":"film/deltarune_poc/renderer.py" if idx in range(57,61) or idx in range(64,68) else None,
            "proof_scope":"selected mechanism study; not full shot fidelity" if idx in range(57,61) or idx in range(64,68) else "not yet rendered"
        }
        start = end
    return {"schema_version": 1, "design_version": "0.1", "status": "directed_plan_pending_game_visual_QA_and_audio_review",
            "checked_on": "2026-10-01", "baseline_commit": "cb63fb6ba5832da38d79f95b8469464c1e2ddbf4",
            "fps": 24, "resolution": [1280,720], "nominal_duration_seconds": 211.9,
            "frame_count": 5086, "encoded_duration_seconds": 5086/24, "hard_cut_frame": 4970,
            "timing_source": "data/timing/word_timeline_notext.json",
            "timing_source_sha256_expected": timing["sha256"],
            "evidence_register": "docs/deltarune/01_CANON_RESEARCH.md",
            "frame_events": EVENTS, "shots": shots}


def write_bible(plan):
    p = ROOT / "docs/deltarune/06_SHOT_BIBLE.md"
    out = ["# 211.9秒 Shot Bible v0.1", "",
           "2026-10-01；导演稿，已完整覆盖5086帧，尚待游戏视觉与听音验收。机器源由 tools/design_deltarune_plan.py 生成，修改设计需同步生成JSON与本文。每镜使用E证据编号，见01；作者隐喻不作canon。", "",
           "24fps；帧区间均[start,end)，end不画；时刻由frame/24计算。字幕仅在本地恢复，本文只含语义概括。编号不是原v2 ALL index；不把它们直接填CUTS。", "",
           "## 连续时间线", "", "| Shot | frame | seconds | section | title | evidence |", "|---|---|---|---|---|---|"]
    for s in plan["shots"]:
        out.append(f"| {s['id']} | {s['start_frame']}–{s['end_frame']} | {s['start_time']:.3f}–{s['end_time']:.3f} | {s['section']} | {s['title']} | {'/'.join(s['canon_evidence'])} |")
    out += ["", "## 逐镜头元素与实现", ""]
    for s in plan["shots"]:
        out += [f"### {s['id']} — {s['title']}", "",
                f"- 范围：{s['start_frame']}–{s['end_frame']} exclusive；{s['start_time']:.6f}–{s['end_time']:.6f}s。",
                f"- 音乐：{s['song_cue']['semantic_description']}；line IDs {s['song_cue']['line_ids']}。详细word/frame锚点保存在JSON，不复制歌词。",
                f"- Chapter/Route：{s['chapter']} / {s['route']}；证据 {' '.join(s['canon_evidence'])}。",
                f"- 叙述目的：{s['narrative_purpose']}。",
                f"- Player：{s['player_state']}；Kris：{s['kris_state']}；他者：{s['other_character_state']}；Story：{s['story_state']}。",
                f"- Camera/Layout：{s['layout']}；{s['camera']}。",
                f"- Foreground：{s['foreground']['description']}。用途：{s['foreground']['reason']}。",
                f"- Background：{s['background']['description']}。用途：{s['background']['reason']}。",
                f"- UI：{s['ui_elements']['description']}。用途：{s['ui_elements']['reason']}。",
                f"- Text：{s['text']['content']}；{s['text']['provenance']}。",
                f"- Character：{s['character']['primary']}；{s['character']['art_status']}。",
                f"- SOUL：{s['soul']['description']}；{s['soul']['reason']}。",
                f"- In：{s['transition_in']}；Out：{s['transition_out']}。",
                f"- Colour：{', '.join(s['colour'])}；Motion：{s['motion']}；Effects：{s['effects']}。",
                f"- 复用：{'；'.join(s['original_repo_components_reused'])}。保留/替换：{s['original_elements_decision']}。",
                f"- 新代码：{', '.join(s['new_code_required'])}（此处是实现计划，并非已经实现）。",
                f"- 技术：PIL/RGBA；直接复用font；旧monkey patch为零；section计划路径 {s['technical_implementation']['new_section_path_planned']}。HTML不必需；原创透明角色/布景预渲染可选。",
                f"- PoC：{s['technical_implementation']['proof_renderer'] or '无'}；{s['technical_implementation']['proof_scope']}。",
                f"- Asset：{s['assets_required'][0]['asset']}；{s['assets_required'][0]['status']}。",
                f"- 待问/限制：{s['unresolved_question']}。",
                f"- Still QA：{s['validation_frames']}；关键事件：{s['key_events']}。", ""]
    out += ["## Frame-aware关键事件", "", "这些是PV的导演帧；不冒充游戏实际tick。每个区间包含连续变化规则与hold，跨镜头保留同一个载体/心。", ""]
    for e in EVENTS:
        out += [f"### {e['id']} — {e['kind']} / {', '.join(e['shots'])}", "", "| frame [a,b) | 连续行为 |", "|---|---|"]
        out += [f"| {a}–{b} | {desc} |" for a,b,desc in e["steps"]]
        out += [""]
    out += ["## 全片审查", "",
            "情绪：连接/合作→身份/规则→亲密落空→能力/自主→分离→越界/反冲→重复执行→他者反向索求→边界/开放问题。器乐段09–12、46–48、61–63各有独立动作目标，不用‘蒙太奇’填空。", "",
            "信息密度：身份/私话/锁定/选项反转处每镜最多两组短字；短‘离开’镜头只做一项拆层，35–39必须用连续心/手而非换角色图。12次执行用共同场景与留痕，不做12张杀敌flash。", "",
            "重复motif：02框→38 cage→48外框→62 chapter框；12 SAVE→28身份卡；18内屏→52出屏；57拒绝→58同文→59停输入。Normal友情/能力多次回访，不靠Weird高潮支撑整首。", "",
            "Chapter采用主题重访：1建立、2镜子/施压、3套层/越界、4私话/反冲、5反向索求/章节。Kris从开头揭露后每镜有身体/手/锚点，其他角色不能接管结尾；开头vessel段是主体选择被收回的必要例外。", "",
            "Normal/Weird并非各50%硬配比。全部route标签、区间与统计可由validate脚本查看；交叉镜头明确标记，不合并成游戏连续事件。末段保留停止输入反证，避免Player单一邪恶或必然无自由。", "",
            "开放验收：R01–03游戏画面；指定自备音频的对齐/听音；原创角色美术；短range节奏。完整覆盖与数据通过不等于PV已叙事/视觉验收，不能据此标goal complete。", ""]
    p.write_text("\n".join(out), encoding="utf-8")


def main():
    plan = build()
    target = ROOT / "data/deltarune_shot_plan.json"
    target.write_text(json.dumps(plan, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    write_bible(plan)
    print(f"Authored {len(plan['shots'])} shots, {len(EVENTS)} critical events, frames [0,{plan['frame_count']})")


if __name__ == "__main__":
    main()
