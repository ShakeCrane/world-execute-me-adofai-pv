"""Source of truth: authored v0.2 direction, not the archived v0.1 plan.

39 actual editorial shots. Sung anchors are preserved; cuts need not occur on
every word. Generates JSON, Bible, and continuity/motif/production metadata.
"""
from pathlib import Path
from collections import Counter
import json

ROOT = Path(__file__).resolve().parents[1]
TUI = "film/tui_pv_world_execute_20260926/"
STATES = {
 "offer":("输入先能选择临时形体","尚未揭露，不等同vessel","尚未出现","创建流程可收回提供的主体"),
 "arrival":("主体选择被收回，仍有行动输入","Kris已有身份/身体，不由表格创生","世界已有关系","被实现的开场限定主体"),
 "normal":("输入可帮助，但不能规定所有回应","技能/气质在共同动作中存在","拒绝或主动合作","有限菜单不消灭日常关系"),
 "nested":("controller/小游戏仍受舞台条件","主体在外层，对输入有身体反应","角色可介入","内外屏幕是实际可见通道"),
 "separate":("仍能移同一SOUL，不能由它决定身体步伐","身体继续有动作，动机不裁定","私域/关系不依当前选择更新","笼/vent限制可达位置"),
 "weird":("影响强，维持路线的条件窄","代行/反冲并保留动作及代价","拒绝/执行/察觉不同声音","预设条件与锁定规定推进"),
 "handoff":("仍黏在HERO，camera错跟不是Kris意愿","可退后/拉开Susie","Susie可介入断线","出屏也属于已实现分支"),
 "reverse":("selector可移，结果趋同；仍可停止输入","身体/手有另一节奏，动机未知","Noelle主动索求不等于自由","确认时限要求继续执行"),
 "halt":("可停止输入，当前段可被中止","身体/既往后果留存","Susie关切/Noelle变化未重置","中止续章也是已编写出口"),
 "boundary":("可等待/离开，不能提供未来章节","手/衣色仍使Kris成为最终主体","不接管最后主体位置","实体屏幕/章节断点是作者的上游边界隐喻")
}

CAMERAS = {
 "vessel":"中心暗场，SOUL中心640,330；一个vessel姿态，不建三栏UI",
 "arrival":"Kris从640,540中景显露；镜头从vessel位置接近身体，不再左pane肖像",
 "help_path":"宽景地面，Kris约460,540/Susie约860,540；输入小而动作轨迹大",
 "refusal":"同一地面，Susie横向离队；camera留Kris，不追攻击对象",
 "welcome":"两角色中近景，手回到共同地面；少UI，让身位靠近可读",
 "body_projection":"斜光中的身体，地面点/弧是投影而非常驻choice圆",
 "organ_intro":"45度键盘前景，Kris手在近处；地平线/键格关联，非数学字幕",
 "tv_intro":"Kris背/手在左前景，实体TV在右；一次建立内外屏幕平面",
 "party_breath":"宽景三人同路，UI退出；地平线低，缓慢横向tracking",
 "last_wire":"低位手/单线/悬吊轮廓，抬视线；最后线留hold，不三候选菜单",
 "wire_fall":"落下的轮廓与Kris手同框；线的空位保留，机位不追到底",
 "organ_care":"暖房间，Kris手/肩的奏乐动作；不再把波形占满半屏",
 "friend_breath":"街道中景，Susie回头，Kris衣色在同一地面；无SOUL离体预告",
 "save_identity":"SAVE卡只遮身体小部分，Kris身形持续可见；只一次名字覆盖",
 "light_dark":"相同身体横移穿过光/暗色域，窗帘边作match，非属性切换卡",
 "shared_rhythm":"手与party动作相合，缓慢靠近胸/肩，为下一镜留真实关系",
 "separation":"Kris胸/手近景，约身体540,560；同一心先在胸，再移手，camera不跳",
 "isolated":"延续同一房间，camera拉宽见笼及远离的身体；后段笼格match成vent",
 "private":"隔墙低机位，心在前景vent，门内两个人处暖光；private/recollection有明确距离",
 "reentry":"延续门/vent同几何，菜单竖成房内入口；心路径跨墙至胸，非字卡切换",
 "route_gates":"俯视折返地面/有限步点；Kris可走路径有限，UI不列条件表",
 "lock_recoil":"腕/接触前景→房间反冲宽景一次pullback；red crack不血腥",
 "down_command":"低伏Kris在近景，Noelle远处仍面向屏外pulse；命令越过身体",
 "sword_pressure":"同一TV地面抵住方向；camera逐渐到内屏边，删第二个套框",
 "execution":"侧向世界构图，12起音依次使冰/路径压力积累；第二半镜头进深，不靠12cut",
 "target_shift":"controller手→内HERO控制接点的match；不写KRIS/YOU说明字",
 "screen_exit":"HERO跨实体屏幕平面；camera追它，Kris暂在侧缘但不消失",
 "protect":"camera被Kris横向拉开动作抢回；Susie移走后攻击落空，再拔connector",
 "blank_reply":"静默两人中景，四空格短显；雨/呼吸取代持续输入ticker",
 "bed_drag":"手撑地的低机位，身体大、pulse小；身位迟缓不等于明确抗议动机",
 "noelle_lead":"湖全宽，Noelle从右主动伸手跨向input来源；Kris大体量/手仍为焦点",
 "converged_choice":"两只手、菜单和红心的近景；一条水线，不左右技术pane",
 "cease_input":"pulse停止到来，心/冷痕不删；关切作为续章比较的反射，不画暂停按钮",
 "continue_input":"实际手势再要求确认，保留停止支线的关系余痕；不做两条按钮分支图",
 "crt_reveal":"湖/人物作为实体CRT表面，camera拉后露机身/stand/input plug；唯一大边界揭示",
 "hand_aftermath":"回近景Kris衣袖/迟疑手与水面残影；最后20秒仍有身体",
 "final_pulse":"最后一次接触pulse，屏幕从完整像收为1px扫描线；无更大矩形",
 "chapter_cut":"4970–4993纯黑24帧；4994–5029短章提示；不画下一章",
 "unresolved":"5030起绿色衣袖和同一心，接触未完成；5051起作者问题，hold至5086"
}


def S(end,title,section,chapter,route,refs,state,budget,scene,legacy,semantic,purpose,fg,bg,ui,text,soul,motion,out,risk):
    return dict(end=end,title=title,section=section,chapter=chapter,route=route,refs=refs.split(),state=state,
                budget=budget,scene=scene,legacy=[f"DR{int(n):02d}" for n in legacy.split()],semantic=semantic,
                purpose=purpose,fg=fg,bg=bg,ui=ui,text=text,soul=soul,motion=motion,out=out,risk=risk)


SHOTS = [
 S(130,"输入先到来","connect","1","opening","E01","offer","SUPPORT","vessel","1 2 3 4",
   "供电/形体的组装","只建立心与临时主体，首次观看不背部件表","一点到红心、灰vessel合拢手势","暗场中的一组开口保护角","小的接受位置，无三栏/双姓名","ACCEPT","始终同一红心",
   "0–8点亮；8–93部件慢合；93–129心停于接受位置；动作少而留hold","灰部件退，绿色身体占住同一视觉锚点","vessel形状是原创概括；不写官方完整opening对白"),
 S(306,"世界已有其人","connect","1","opening → normal","E01","arrival","HERO","arrival","6 7",
   "接受/参数/启动","选择被收回，但Kris很早成为可识别主体","Kris遮眼头、绿色衣带、自己的手","卧室门与一束窗光，原vessel槽成为空位","接受位置消失，不追加name表","KRIS","由接受位置靠近胸但不宣称本体身份",
   "130–142灰vessel退；142–156Kris显；156–243缓推身体；243–305窗光/手先动而非表格","门光落到可走的地面","提前剪接是导演节奏，不改游戏opening事实顺序"),
 S(476,"行动可以帮助","normal","1","normal","E03","normal","SUPPORT","help_path","8 9",
   "开始行动/器乐建立","先让输入帮助同行，后面的控制才有关系重量","Kris跨过地面间隙，Susie在同一世界","两块暖地形与可走路径","小方向pulse只在动作之前出现","无","胸/行动接口亮一次即可",
   "306–385输入→Kris一步；385–432步幅跨缺口；432–475同地面停住，Susie另走半步","Susie突然选择自己的方向","原创blocking概括合作，不假造新剧情/输入延迟"),
 S(567,"她有自己的方向","normal","1","normal","E03","normal","SUPPORT","refusal","10",
   "器乐重拍","他者的拒绝用偏离队形读出，不贴refusal说明","Kris停、Susie独自前冲","刚建立的共同地面还在","小命令格闪一次后退灰","无","仍留Kris位置，不追Susie",
   "476–500Susie准备；500–535向另一方向行动；535–566Kris留原位看她，camera不追","Susie回望，主动靠回","不宣称Susie永远不可指挥"),
 S(715,"愿意同行","normal","1 / 3","normal / author staging","E03","normal","HERO","welcome","11",
   "器乐回收","温暖关系成为后半会失去的东西","Kris与Susie的手、各自完整身体","低地平线与暖反光","menu退场，动作先于框","无","低亮留接口，不制造第二颗心",
   "567–615Susie回到同地面；615–655伸手回应；655–714两人停留而非又加SAVE概念","共同地面渐成斜投影","手势是作者合作比喻，不新增canon握手对白"),
 S(890,"身体不是参数表","identity","1 / 4","normal / author metaphor","E01 E21","normal","SUPPORT","body_projection","13 14",
   "点/几何定义","保留数学趣味但让身体先于定义，删同结果菜单预告","Kris手和身体、少量点投影","斜光/地面弧，不是choice环","无常驻圆菜单","无","保持身体锚点",
   "715–803点从脚边聚合；803–889投影环从地面滑过，身体不被切成数据","点距变成前景键格","点/弧是作者视觉，不对人物能力下数学定义"),
 S(1066,"已有的能力","identity","4","normal","E21","normal","SUPPORT","organ_intro","15",
   "波/可接触轨道/限制","普通输入也能与Kris的能力共同作用","键盘与Kris手的两次动作","暖暗室、稀疏乐纹","方向点很小，不占半屏","无","胸前稳定，手在世界前景",
   "890–980手落键；980–1030两键相继按下；1030–1065持手/听波纹，不撞新白框","键盘角match到controller手","没有音频，只用现有唱词timing，奏乐不是实际乐谱复刻"),
 S(1235,"屏幕里面还有行动","nested","3","common / sword foreshadow","E13 E15","nested","SUPPORT","tv_intro","17 18",
   "电流/视角受限","一次建立后面会被穿透的实体屏幕平面","Kris背/握controller的手，内HERO","带厚度的TV与地面","控制接点在屏幕内，非三层解释图","无","输入到内游戏对象的路径短显",
   "1066–1145手/TV依次亮；1145–1190内角色向边走；1190–1234边阻住但外身体仍在","TV暖光淡到party地面","不复刻未经R01核对的具体原地图"),
 S(1417,"共同世界的停留","normal","1 / 3","normal / thematic crosscut","E03","normal","BREATH","party_breath","20",
   "时空可能/深度结合","给关系呼吸，不把合作再解释成双向线","Kris主体，Susie/Ralsei各留一身间距","宽地面与暖远光","无","无","不抢视线，只留低亮锚点",
   "1235–1322慢tracking同路；1322–1416脚步停下、肩/呼吸继续；不逐词加动作","远光落在一根悬吊线上","Ralsei不成为管理员/全知解释者"),
 S(1591,"最后一根支撑","affinity","2","normal","E06 E07","normal","SUPPORT","last_wire","21 22",
   "提供可能/满足的条件","观众先期待切线能帮助，结果才会有落差","Kris伸手与悬吊轮廓/一根线","宽暗地面和上方支撑点","只一个确认位置","无","在确认接点，保持一个主要心",
   "1417–1513线仍支撑轮廓；1513–1578手接近、hold；1578–1590接点释放","切后身体坠落，camera不庆祝","NEO只是关系镜子，不做boss介绍/胜利banner"),
 S(1774,"落空后留下手","affinity","2","normal","E06 E07","normal","HERO","wire_fall","24",
   "执行/仍然受困","动作成功和可行动不是一回事；让落空有余韵","落下轮廓、Kris悬空未收回的手","断线空位保持，世界不消失","确认框撤出","无","停于刚按过的位置，不消灭接口",
   "1591–1637小轮廓坠落；1637–1683空线轻摆；1683–1773Kris手留住，呼吸降强度","空线摆动变成暖键格影","不画角色死亡/全员解放，不提前演保护Susie"),
 S(1951,"会给予的身体","care","4","normal","E21","normal","SUPPORT","organ_care","25",
   "给予能力/保护","能力不是菜单制造的空壳；日常抵消恐怖的单一情绪","Kris肩、手与前景键格","暖室/窗纹","可用输入轻亮后退出","无","胸口低亮，动作在世界中发生",
   "1774–1865两次手/肩表演；1865–1950光从键面流向窗，身体保留而非变波形","窗光延长成街道","删前段balloon离体，保护110秒首次明确分离"),
 S(2043,"回应属于关系","care","1 / 5","normal / author staging","E03","normal","BREATH","friend_breath","27",
   "让他者快乐/回应","Susie也可回应Kris，关切需要在压力前熟悉","Kris与回头的Susie","暖街道/同一地面，少线","无","无","很低亮仍可辨",
   "1951–1991同行；1991–2042Susie回头/Kris衣袖轻动；不加love confession","两人影子间出现一次SAVE卡","普通友情的作者概括，不冒充Ch5 balloon事件"),
 S(2205,"名字写入而身体留下","identity","1","normal / thematic recall","E02","normal","SUPPORT","save_identity","12 28",
   "存在/身份","SAVE名字只出现一次；有身体才不变哲学图表","Kris衣色和手持续，单卡小范围覆盖","街道暗下但身体不消散","SAVE一slot，一次name覆盖","KRIS / CREATOR","在保存位置，不把名字变成脸",
   "2043–2080slot显；2080–2125名字覆盖；2125–2204卡退一半/身体继续呼吸","卡白光变窗光边","不虚构输入者名字或多周目全角色记忆"),
 S(2382,"同一个人穿过光","care","1 / 2","normal / author metaphor","E01","normal","TRANSITION","light_dark","29 30",
   "日夜/身份情境","舞台变化不能更改Kris身份；不第二次套TV","同一遮眼头/衣袖，拉帘的手","Light暖色→Dark靛蓝，一次色域变化","无属性卡或gender项","无","身体锚点不断，不提前藏心",
   "2205–2295手拉光边；2295–2381身体横越色域，环境变而身形连续","暗光进入共同动作的近景","窗口动作是导演match，不声称某段自主剧情"),
 S(2571,"合拍也有重量","normal","1 / 4","normal / thematic crosscut","E03 E21","normal","SUPPORT","shared_rhythm","32 33",
   "感应/共振","分离前留一次确实成立的合作，不能所有连接都负面","Kris手与伙伴回应动作","小暖光、不满屏光谱","menu弱退，不比较两种wave数据","无","胸前完整、不过度放大",
   "2382–2485两种动作靠近；2485–2530相合一次；2530–2570在完整身体上hold","camera留在同一胸/手，暖光开始退","相合是作者表演，不当精确输入时延事实"),
 S(2693,"第一次身体与心分开","separation","1","ending / director staging","E04","separate","HERO","separation","34 35",
   "完成→离开","第一次明确认知断裂：心可离开，身体没有随它退场","Kris胸、同一只手、同一SOUL","房间地面/门；不切换人物海报","接口在接触时断，不逐词拆CSS","无","胸→手→胸外，不能生成替身心",
   "2571–2644留完整身体；2644–2650手准备；2650–2674连续拉出；2674–2692手带心到笼位置","同一房间拉宽，身体/心同时能看见","不写Kris认识/憎恨现实Player；抽心细节仍是原创staging"),
 S(2838,"输入仍在，身体走开","separation","1 / 4","ending → vent thematic match","E04 E20","separate","BREATH","isolated","36 37 38 39 40",
   "反复离开→隔离","把五次短拆层合成一个因果空间：心动、身体不跟","Kris向门独走，前景心在笼/后续vent","同一地面拉宽，2784后格线主题match通道","外读区随身体退让，不补新字","无","同一心保持可见锚点，笼内移动不穿边",
   "2693–2728心在笼移；2728–2754Kris离开；2754–2784两者同框hold；2784–2837格线match到vent","门内暖光露出私域","Ch1→Ch4是主题match，不宣称房间真实连通；不能穿笼造canon"),
 S(2928,"门内不是命令窗口","private","4","weird / private space with remembered report","E20 E23","separate","BREATH","private","41",
   "清理片段/希望留住","隔墙的距离使外心成为观察者，给私话重量","门内Kris/Noelle，外面SOUL小但清楚","房间暖光与vent暗角，缺一条控制连接","无VOICE/KRIS解释卡","无","留在前景通道，看得到身体但够不到",
   "2838–2885门内身位靠近；2885–2927只肩/手的微动作，外心停；不新增对白","一个choice物体在房内立起来","歉意只由Noelle回忆支持，不把旧回忆画成确证录像"),
 S(3014,"菜单闯进私人空间","reentry","4","weird","E24","weird","HERO","reentry","42",
   "希望重获连接","外面的心沿实体choice进入，再占回身体接口","同一SOUL越墙到胸；Kris/Noelle仍是身体","门与vent延续前镜坐标","choice竖成门一样的世界物体","Proceed","vent→房内菜单→Kris胸，只有一次心",
   "2928–2940门显；2940–2972心穿通道；2972–2996到胸；2996–3013重入，暖空间受挤","房间地面转为折返路径","原游戏layout/time limit待R02，PV frame不冒充game tick"),
 S(3093,"有力量仍需走规定的路","weird","2 / 4","weird / thematic crosscut","E08 E24","weird","SUPPORT","route_gates","43",
   "挑战/条件限制","偏离的强影响与狭窄路径在俯视地面同时出现","Kris走回自己留下的足位","三处实际窄口，回退弧","不列requirements文字","无","沿有限路径，不能任意跳到另一世界",
   "3014–3054折返；3054–3092逐窄口停一步，出口仍窄","窄口接触点match到腕","不写真实游戏code或虚构剧情条件"),
 S(3232,"接触的代价回到身体","weird","4","weird","E26","weird","HERO","lock_recoil","44 45",
   "锁定/非法参数/反冲","抓腕施加与接口反冲在同一角色上，不是胜利恐怖特效","Kris/Noelle腕接触、红裂、随后Kris手/脚反冲","接触close拉后见稳定浴室容器","分支只短暂收束，不常驻glitch","无","命令位置→被放入容器，震动仍有心",
   "3093–3117手接近；3117–3149裂；3149–3185抽心放容器；3185–3209一次踢/回震；3209–3231静止","回震低姿态match到另一章低伏身体","Ch4→Ch2是主题cut；不浪漫化自伤/不判断动机"),
 S(3323,"身体倒下，命令继续","weird","2","weird","E09 E12","weird","SUPPORT","down_command","46",
   "器乐施压","声音/命令归属不能由倒下身体概括","低身位Kris在近处，Noelle远处应对","冰白空间保留地面与空位","屏外pulse越过Kris而非自胸发出","无","接口可见，Kris不随pulse起身",
   "3232–3270身体低伏，pulse越过；3270–3322Noelle远处动作一次，Kris维持","pulse源落到controller接点","DOWN不等于死亡，不配现实玩家声音"),
 S(3549,"内世界抵住方向","nested","3","sword","E15 E16","nested","SUPPORT","sword_pressure","47 48",
   "器乐蓄压/越界条件","控制链在实际小游戏边界积压，不再增加概念框","Kris/controller、内HERO在shelter方向受阻","有厚度TV内两段地面和门槛","内方向点与身体退步不同节奏","无","连接到内HERO，Kris不被替换",
   "3323–3412向门/阻力重复两次；3412–3500慢推至屏面；3500–3548留edge压力","镜头压紧的空间接到12pulse世界","不猜shelter/holder身份；精确动作待R01"),
 S(3821,"十二次命令改变空间","execution","2","weird / condensed execution","E08 E10","weird","HERO","execution","49 50",
   "十二次重复执行","每次输入留下世界压力与代价，不能成12个杀敌flash","Kris手保持，Noelle施法方向和空位逐渐受挤","侧景地面被冰纹/窄列挤压；第二半camera进深","一命令位置短亮，每pulse后留hold","无","同一心触同一接口，不生成12心",
   "line67–78每起音一次空间压力；前6侧向压，后6camera沿深度推；末3795后hold到3821","最后压力线match到TV内控制接点","12是歌曲次数，不是canon敌人数；Berdly冰封不当死亡确证"),
 S(3902,"摄影机将跟错对象","execution","2 / 3","weird → sword thematic cut","E11 E18","nested","TRANSITION","target_shift","51",
   "计数/呼唤归属","叙述主语不用标签解释，input目标迁到内HERO","Kris握controller仍大，HERO在另一平面","TV屏面和外世界不同深度","接点从身体移至HERO，不写KRIS/YOU","无","只有一个主要心，输入指向HERO",
   "3821–3880控制接点移；3880–3901HERO脚至内屏边；camera预先偏向它","HERO载体开始跨实体屏面","不擅自把第二人称配成人类玩家声音"),
 S(3988,"控制对象走出屏幕","handoff","3","sword","E18","handoff","HERO","screen_exit","52",
   "执行交给他者","camera跟HERO使观众短暂丢失对Kris的中心感；输入归属仍清楚","HERO跨厚TV边，Kris退后但留左侧","TV内地面只裁背景，跨屏carrier独立","input接点跟HERO，不跟Kris","无","连接目标始终HERO，跨边不另造心",
   "3902–3938HERO跨平面；3926–3942Kris退；3938–3962camera追HERO；3962–3987停在错误中心","攻击方向逼近Susie，Kris准备横移","crossing与camera都是原创演出，游戏连续画面待R01"),
 S(4072,"Kris把她拉开","handoff","3","sword / condensed branch staging","E19","handoff","HERO","protect","53",
   "执行作用反转","全片最明显的非当前selector主导动作；他者可介入控制链","Kris手拉Susie离开攻击旧位置，Susie再拔connector","同TV/外地面，camera因拉开被抢回","输入仍对HERO，拔线后它失去载体","无","选择点未先移动，手先动；断线不抹心",
   "3988–4000预攻击；4000–4012Kris先伸手；4012–4030拉离；4030–4040攻击落空；4040–4064Susie拔线；4064–4071hold","空的旧攻击位成为一段沉默","合并相关分支用于导演staging，不声称同一游戏录像必然连续如此"),
 S(4164,"回来却没有字","aftermath","4","weird / thematic crosscut","E27","weird","BREATH","blank_reply","54",
   "取回接口/回应不可能","不立刻制造第三个高潮，让Kris/Susie之间的停顿可见","Kris胸/手、可辨的Susie侧影","雨/低光地面，关系距离","四空slot短显后不刷说明","无","可移而无文本，身体不替作者说话",
   "4072–4100格显；4100–4130selector一移；4130–4163只有雨/肩呼吸","低身位落向床边","不能给空项填作者希望的Kris独白"),
 S(4259,"手撑着慢慢起身","reverse","5","weird","E31","reverse","SUPPORT","bed_drag","55",
   "受困/反复输入","急输入与慢身体以低机位呈现，不用进度条","Kris手撑地、身形低而大","床边与后窗冷光","小pulse急于身体，非百分比","无","留身体接口，弱亮但不消失",
   "4164–4200手压地；4200–4258重复pulse而身体只抬很小距离","窗冷光延伸成湖岸","迟缓动机未知，不诊断其自伤/拒绝/认知现实玩家"),
 S(4430,"她把命令带进世界","lake","5","weird","E32 E33","reverse","HERO","noelle_lead","56 57",
   "学习/索求/拒绝仍前进","Noelle第一次从角色层主动跨向输入源；Player拒绝与既往塑造冲突","Noelle伸向input的手、Kris独立慢身位/手","全宽湖/岸，角色大，UI少","choice被她的手势带到世界，而非静态左pane","Stop / Proceed","先停Stop，身位仍在她引导方向小移",
   "4259–4319她跨向输入；4319–4344菜单入世界；4344–4367Stop/手引导；4367–4429角色hold与水移动","两只手夹住菜单进入近景","主动不是自由/爱情解救；保留Stop回应/计数差异的短痕迹"),
 S(4519,"位置变了，手仍被带着","lake","5","weird / prompt condensation","E33 E34","reverse","HERO","converged_choice","58",
   "关系变成表达式","不解释式子，让selector可变而手/身体保持另一节奏","Kris与Noelle两只手占主要面积，红心在菜单","一条湖水线/外冷光","两格同文，menu已经在世界内","Proceed / Proceed","左→右，4495可读；无假Stop出口",
   "4430–4436Stophold；4436–4442退字；4442–4448同文；4448–4460心移；4460–4518手迟疑/湖留痕","屏外pulse停止到来，UI失去节奏","不重演全部prompt；身体迟疑是作者情绪设计非动机证明"),
 S(4574,"停止到来的输入","halt","5","interrupted weird / comparative staging","E34 E36","halt","BREATH","cease_input","59",
   "似自由/受困的反证","停止是输入没有再到来；后果不能被按钮洗净","Kris手松、红心保留、关切关系的反射","冷痕/空位未退；续章关切作为灰暖反射","确认pulse退去，不画暂停按钮","无","不被物理删除，停止selector操作",
   "4519–4531pulse消失；4531–4543关切反射显；4543–4573人物/冷痕留hold","反射不删，继续側手势重新要求输入","比较不是同时canon多宇宙；不称全部reset"),
 S(4654,"继续重新组织了控制","lake","5","weird + interruption comparison","E32 E34 E36","reverse","TRANSITION","continue_input","60",
   "持续确认的代价","继续不是Player胜利，角色世界向接口要求下一次执行","Kris迟疑手，Noelle掌势把menu推回","湖压力和停止侧关切余痕共在但不对称","一次confirmation收窄，再一次更紧；不画两分支按钮","Proceed","趋白但留红外轮廓，仍能停止输入",
   "4574–4601第一次收框；4601–4621第二次更紧；4621–4653世界水线抬，input小而身体大","水面成为屏幕表面的一层光","不是每个原game timeout单调减少；只PV压缩"),
 S(4863,"连观察的位置也是屏幕","boundary","3 / 5","weird / author spatial metaphor","E13 E35","boundary","HERO","crt_reveal","61 62",
   "器乐递归/章节接收越界","唯一大边界揭示：内世界和操作点在实体CRT同一表面","Kris身体仍在湖图像，绿色衣袖保持识别","camera拉后露厚机身/stand/input plug，非三白框","小操作点也在屏幕上，不新增route/chapter标签","无","在表面内停留，不能称现实人被强制按键",
   "4654–4734世界拉后/机身露；4734–4814input plug显；4814–4862保持主体尺寸可辨","camera回到衣袖/手的余波","CRT是作者Story隐喻，不声称Kris逃出或现实玩家可见"),
 S(4929,"最后仍是一个人","boundary","1 / 5","author aftermath","E04 E36","boundary","BREATH","hand_aftermath","63",
   "尾奏留停顿","最后20秒保住角色情绪，少于一个解释图表","Kris绿色衣袖与未完成的伸手","水/屏光反射一层，不加新框","无ticker/箭头","无","相距足够，没有最终谁占有谁",
   "4863–4895衣袖慢入近景；4895–4928手停，只有反射/呼吸移动","最后pulse落到手与心之间的接点","不把伸手读作确定求死/同意/仇恨"),
 S(4970,"最后一次接点","final","5","weird / author compression","E35","boundary","TRANSITION","final_pulse","64",
   "最后执行/硬切","结束当前执行而非杀掉Player或角色","Kris手/心、实体屏幕的残光","机身/湖只一层残像","最后pulse不引入新矩形","无","仍同一颗心到4969",
   "4929–4935接点亮；4935–4962手hold；4962–4969画布收缩；4969只1px；4970切纯黑","完整24帧黑，不继承DSHchime","AUDIO REVIEW PENDING，4970来自原timing未听音校准"),
 S(5030,"沉默以后仍被要求继续","final","5","weird early chapter ending","E35","boundary","SUPPORT","chapter_cut","65",
   "黑场/章边界","黑有时间重量，短提示只提出未来缺口，不展示答案","先无主体；随后只两行章提示","纯黑，禁止恢复ticker/世界glitch","不仿官方启动品牌","Insert Chapter 7 / Side B","黑场不叠SOUL",
   "4970–4994全黑24帧；4994–5002淡入；5002–5029短字hold36帧范围","提示退，Kris衣袖与心回低光","终屏转录待R03精确版画面核对；不画未发布章节"),
 S(5086,"谁在执行谁","final","1–5","author unresolved question","E01 E04 E18 E33 E35 E36","boundary","BREATH","unresolved","66 67",
   "未解决的余韵","问题在迟疑手/心之后才到来，调用身份不固定成胜负","Kris绿色衣袖/手与同一心，接触留空隙","黑/低光，不重新套上哲学框","无技术metadata","Who executes whom?","心与手均在，未作下一章决定",
   "5030–5048手/心显；5048–5051保持未接触；5051–5057作者问题显；5057–5085hold，不闪不返黑","5086 exclusive片结束","作者文字不是游戏角色台词；最终美术/情绪仍待验收")
]

EVENTS = [
 {"id":"K01","kind":"identity_reassignment","shots":["PV02"],"start":130,"end":177,"steps":[[130,142,"灰vessel退，心保持身份"],[142,156,"绿色Kris身体显露，主体非输入表格"],[156,177,"hold同一锚点，无第二SOUL"]]},
 {"id":"K02","kind":"SOUL_separation","shots":["PV17","PV18"],"start":2644,"end":2784,"steps":[[2644,2650,"手靠胸，心仍inside"],[2650,2662,"同一心沿胸→手路径"],[2662,2674,"越胸边/连接断，身体不消失"],[2674,2693,"手带心到笼位置"],[2693,2728,"心在笼移而身体不跟"],[2728,2754,"Kris独步，camera同时保心"],[2754,2784,"hold两个独立运动者，禁止cut海报"]]},
 {"id":"K03","kind":"control_reentry","shots":["PV20"],"start":2928,"end":3014,"steps":[[2928,2940,"choice在房内竖成门"],[2940,2972,"同一心从vent跨菜单入口"],[2972,2996,"穿房内至胸；body/heart锚点连续"],[2996,3014,"重入接触后hold，私域暖光被挤"]]},
 {"id":"K04","kind":"weird_lock_in_and_recoil","shots":["PV22"],"start":3093,"end":3232,"steps":[[3093,3117,"手腕接近，尚有拒绝间隙"],[3117,3149,"接触红裂，角色脸不猎奇"],[3149,3185,"一次抽出/落容器"],[3185,3209,"一踢，震动回到身体"],[3209,3232,"hold代价，不写free"]]},
 {"id":"K05","kind":"story_spatial_reveal","shots":["PV35"],"start":4654,"end":4863,"steps":[[4654,4734,"湖/身体缩入有厚度CRT表面"],[4734,4814,"camera露input plug/机身，操作点也在表面"],[4814,4863,"hold可辨Kris，禁止再套大白框"]]},
 {"id":"K06","kind":"character_control_handoff","shots":["PV27"],"start":3902,"end":3988,"steps":[[3902,3938,"HERO穿屏面，背景mask不裁carrier"],[3938,3962,"camera追HERO而Kris留边缘，control未返回Kris"],[3962,3988,"hold错误中心，攻击方向接近他者"]]},
 {"id":"K07","kind":"protection_then_disconnection","shots":["PV28"],"start":3988,"end":4072,"steps":[[3988,4000,"攻击预示，SOUL未换位置"],[4000,4012,"Kris手先动"],[4012,4030,"拉Susie离开旧位，camera抢回"],[4030,4040,"攻击只落旧空位"],[4040,4052,"Susie伸手到connector"],[4052,4064,"断controller连接，HERO退显"],[4064,4072,"hold同一SOUL与两身体"]]},
 {"id":"K08","kind":"character_world_reverses_input","shots":["PV31","PV32"],"start":4259,"end":4519,"steps":[[4259,4319,"Noelle手越向input源，连接方向反转"],[4319,4344,"choice被带入角色世界"],[4344,4430,"Stop可读/留差异痕，身体仍小前移"],[4430,4436,"hold原两词"],[4436,4442,"Stop退字，心不换身份"],[4442,4448,"同文Proceed出现"],[4448,4460,"selector左→右，body不同节奏"],[4460,4519,"手迟疑，4495peak不遮主体"]]},
 {"id":"K09","kind":"cease_is_not_a_button","shots":["PV33","PV34"],"start":4519,"end":4654,"steps":[[4519,4531,"输入pulse不再到来，SOUL仍在"],[4531,4543,"关切反射显，冷痕未抹"],[4543,4574,"hold后果，不给pause按钮"],[4574,4601,"继续侧手势再次要求确认"],[4601,4621,"第二确认收缩；停止痕迹仍在"],[4621,4654,"世界影响UI读区，准备CRT揭示"]]},
 {"id":"K10","kind":"final_hard_cut","shots":["PV37","PV38"],"start":4929,"end":5030,"steps":[[4929,4935,"最后歌锚点亮接点"],[4935,4962,"Kris手/心hold"],[4962,4970,"收画布，4969只1px"],[4970,4994,"纯黑24帧，无chime"],[4994,5002,"章提示淡入"],[5002,5030,"未来空位hold，不画下一章"]]},
 {"id":"K11","kind":"unresolved_hand_then_author_question","shots":["PV39"],"start":5030,"end":5086,"steps":[[5030,5048,"绿色衣袖/同一心低光显"],[5048,5051,"接触未完成，留空隙"],[5051,5057,"作者问题淡入"],[5057,5086,"末帧hold，无结局判定"]]}
]


def build():
    timing = json.loads((ROOT/"data/timing/word_timeline_notext.json").read_text(encoding="utf-8"))
    words = timing["skeleton"]["words"]
    shots, start = [],0
    for i,row in enumerate(SHOTS,1):
        end = row["end"]
        sid = f"PV{i:02d}"
        pp,kk,oo,ss = STATES[row["state"]]
        onsets = [{"line_id":w["line_id"],"word_index":w["word_index"],"source_seconds":w["start"],"frame":round(w["start"]*24)} for w in words if start<=round(w["start"]*24)<end]
        lines = sorted({w["line_id"] for w in words if w["start"]<end/24 and w["end"]>=start/24})
        shots.append({"id":sid,"title":row["title"],"section":row["section"],"start_frame":start,"end_frame":end,
          "start_time":start/24,"end_time":end/24,"frame_interval":"[start,end)",
          "song_cue":{"semantic_description":row["semantic"],"line_ids":lines,"word_onsets":onsets,"instrumental":not lines},
          "chapter":row["chapter"],"route":row["route"],"canon_evidence":row["refs"],
          "evidence_usage":{ref:row["purpose"]+"；仅采用01该E记录可见事实，不扩展角色动机" for ref in row["refs"]},
          "claim_scope":"原创导演staging/主题剪接；非游戏连续录像或新增canon",
          "narrative_purpose":row["purpose"],"player_state":pp,"kris_state":kk,"other_character_state":oo,"story_state":ss,"agency_preset":row["state"],
          "shot_budget":row["budget"],"legacy_source_shots":row["legacy"],"layout":row["scene"],"scene":row["scene"],"camera":CAMERAS[row["scene"]],
          "foreground":{"description":row["fg"],"reason":row["purpose"]},
          "background":{"description":row["bg"],"reason":"建立身体动作的可达空间/距离；不是抽象信息图"},
          "ui_elements":{"description":row["ui"],"reason":"只在输入归属/边界必须可读时介入"},
          "text":{"content":row["text"],"provenance":"无" if row["text"]=="无" else "短词/名字或明确作者问题；非歌词/新增角色对白","reason":"减到观众需要记住的一个动作，不以解释代替表演"},
          "character":{"primary":"Kris（PV01尚未揭露）" if i==1 else "Kris","art_status":"original geometric rough blocking; production art pending","reason":"身体/衣色/手持续，不让他者接管叙事"},
          "soul":{"description":row["soul"],"reason":"同一输入入口空间连续；不裁定本体身份"},
          "transition_in":"黑场一点显" if i==1 else shots[-1]["transition_out"],"transition_out":row["out"],
          "colour":["#070A14","#75A58B","#D5BE8A" if row["state"]=="normal" else "#C7E4EC","#F04462"],
          "motion":row["motion"],"movement_intention":row["motion"],"transition_intention":row["out"],
          "effects":"少量接触光/水纹；拒绝靠generic glitch提升预算；纯黑区无后期残影",
          "original_repo_components_reused":[TUI+"tuikit.py:font",TUI+"continuity_full_v2/cuts.py:independent carrier/mask principle (design reuse)"],
          "original_elements_decision":"KEEP整数timing/分层；REPLACE静态左右pane与哲学分支图；REMOVE常驻ticker/舞者",
          "new_code_required":[f"film/deltarune_poc/scenes.py:{row['scene']}","film/deltarune_poc/stage.py:posed_characters","film/deltarune_poc/renderer.py:frame"],
          "assets_required":[{"asset":"原创posed Kris/其他角色/该镜地面与道具","source":"程序化作者blocking，不导出游戏sprite","status":"rough geometry; game visual R01–03 / production art pending"}],
          "unresolved_question":row["risk"],"key_events":[e["id"] for e in EVENTS if sid in e["shots"]],
          "validation_frames":sorted({start,min(start+12,end-1),(start+end)//2,end-1}),
          "implementation_status":"authored_rough_blocking_spec; actual render status in v02 manifest",
          "technical_implementation":{"medium":"PIL/RGB + per-frame authored geometry/carrier",
             "direct_renderer_reuse":[TUI+"tuikit.py:font"],"adapted_data_components":"text-free word timing, inherited24fps/4970",
             "legacy_monkey_patch":"none","new_section_path_planned":f"film/deltarune_poc/scenes.py:{row['scene']}",
             "new_components_planned":["posed characters","world depth","short-lived UI"],"html_playwright":"not required",
             "prerender_asset":"optional original production art later","reusable_abstraction":"stage pose/camera/carrier; scene keeps its own blocking",
             "proof_renderer":"film/deltarune_poc/renderer.py","proof_scope":"rough staging, not final art/gameplay recreation"}})
        start=end
    pulse_anchors=[]
    for line in range(67,79):
        ws=[w for w in words if w["line_id"]==line]
        pulse_anchors.append({"line_id":line,"frame":round(min(w["start"] for w in ws)*24)})
    return {"schema_version":2,"design_version":"0.2","status":"director_rewrite / AUDIO REVIEW PENDING",
      "checked_on":"2026-10-01","baseline_commit":"cb63fb6ba5832da38d79f95b8469464c1e2ddbf4","fps":24,"resolution":[1280,720],
      "nominal_duration_seconds":211.9,"encoded_duration_seconds":5086/24,"frame_count":5086,"hard_cut_frame":4970,
      "black_hold_frames":[4970,4994],"timing_source":"data/timing/word_timeline_notext.json","timing_source_sha256_expected":timing["sha256"],
      "evidence_register":"docs/deltarune/01_CANON_RESEARCH.md","prior_plan":"docs/deltarune/archive/v01/shot_plan.json",
      "audio_review":"PENDING","game_visual_review":"R01–03 PENDING","art_review":"PRODUCTION ART PENDING",
      "execution_pulse_anchors":pulse_anchors,"execution_shot":"PV25","frame_events":EVENTS,"shots":shots}


def write_bible(p):
    out=["# 211.9秒 Shot Bible v0.2","","39镜导演重写；5086帧/24fps。source of truth：tools/design_deltarune_plan.py；JSON保留395个原word锚点，不提交歌词。v01已归档，DR编号只出现在legacy字段，不是当前shot或旧ALL index。","",
         "AUDIO REVIEW PENDING。CANON事实与原创blocking/主题cut分开，R01–03和production art未验收。镜头数量减少不是简化为静态图：每镜有运动与转场意图。","",
         "## 预算与连续时间线","",f"预算：{dict(Counter(s['shot_budget'] for s in p['shots']))}。HERO成本集中在动作/空间；BREATH主动减少UI。","",
         "| shot / budget | frames [a,b) | seconds | title | legacy | evidence |","|---|---|---|---|---|---|"]
    for s in p["shots"]:
        out.append(f"| {s['id']} / {s['shot_budget']} | {s['start_frame']}–{s['end_frame']} | {s['start_time']:.3f}–{s['end_time']:.3f} | {s['title']} | {'/'.join(s['legacy_source_shots'])} | {'/'.join(s['canon_evidence'])} |")
    out += ["","## 逐镜导演与实现"," "]
    for s in p["shots"]:
        out += [f"### {s['id']} — {s['title']} / {s['shot_budget']}","",
          f"- 时间：[{s['start_frame']},{s['end_frame']})；{s['start_time']:.6f}–{s['end_time']:.6f}s；legacy {s['legacy_source_shots']}。",
          f"- Song cue：{s['song_cue']['semantic_description']}；line IDs {s['song_cue']['line_ids']}；所有word/frame锚点在JSON。",
          f"- Chapter/Route：{s['chapter']} / {s['route']}；E {' '.join(s['canon_evidence'])}；{s['claim_scope']}。",
          f"- 必要性：{s['narrative_purpose']}。",
          f"- Player：{s['player_state']}；Kris：{s['kris_state']}；Other：{s['other_character_state']}；Story：{s['story_state']}。",
          f"- Camera / spatial novelty：{s['camera']}。",
          f"- Foreground：{s['foreground']['description']}；理由：{s['foreground']['reason']}。",
          f"- Background：{s['background']['description']}；理由：{s['background']['reason']}。",
          f"- UI：{s['ui_elements']['description']}；Text：{s['text']['content']}；{s['text']['provenance']}。",
          f"- Character：{s['character']['primary']}，{s['character']['art_status']}；SOUL：{s['soul']['description']}。",
          f"- 连续动作：{s['movement_intention']}。",
          f"- In：{s['transition_in']}；Out：{s['transition_intention']}。",
          f"- Colour：{s['colour']}；Effects：{s['effects']}。",
          f"- 复用：{' / '.join(s['original_repo_components_reused'])}；{s['original_elements_decision']}。",
          f"- 实现：{' / '.join(s['new_code_required'])}；PIL，零旧monkey patch；HTML不必需；生产原创透明asset可后替换。",
          f"- 素材：{s['assets_required'][0]['status']}；仍待：{s['unresolved_question']}。",
          f"- QA frames：{s['validation_frames']}；关键事件：{s['key_events']}。",""]
    out += ["## 连续关键事件","","下列帧是PV导演动作，不是game tick。事件贯穿身体、同一心和摄影机；不可用替换poster冒充动作。",""]
    for e in EVENTS:
        out += [f"### {e['id']} — {e['kind']} / {','.join(e['shots'])}","","| [a,b) | 连续动作 |","|---|---|"]
        out += [f"| {a}–{b} | {desc} |" for a,b,desc in e["steps"]]
        out.append("")
    out += ["## 导演验收边界","","本版情绪曲线、全部67镜去向及删除理由见09。数据覆盖/技术pass不代表最终音乐PV成立；第二轮目视反馈与完整rough review见10。无自备歌曲所以始终 AUDIO REVIEW PENDING。",""]
    (ROOT/"docs/deltarune/06_SHOT_BIBLE.md").write_text("\n".join(out),encoding="utf-8")


def main():
    plan=build()
    (ROOT/"data/deltarune_shot_plan.json").write_text(json.dumps(plan,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    write_bible(plan)
    print(f"Shot Bible v{plan['design_version']}: {len(plan['shots'])} authored shots, {dict(Counter(s['shot_budget'] for s in plan['shots']))}, [0,5086)")


if __name__=="__main__":
    main()
