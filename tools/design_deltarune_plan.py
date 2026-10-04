"""v0.3 lyric-led direction. Generates plan, Bible, lyric ledger and rewrite.
Text-free timing is retained. No full lyrics or gameplay assets are distributed.
"""
from pathlib import Path
from collections import Counter
import hashlib,json
ROOT=Path(__file__).resolve().parents[1]
# end | title | act | budget | scene | evidence | purpose | motion | camera | risk
ROWS='''
93|开机与保护角|Creation|SUPPORT|power_protection|E01|Switch启用输入；Protection先是容器保护|1点亮；43起四角沿供电线合拢；不闭成牢笼|空场一点到部件台中景|保护是作者双关，不能首秒宣判恶意
177|可选择的头身腿|Creation|SUPPORT|pieces|E01|Pieces/Object具体建立配置Vessel的期待|93–130头身腿分层入；130–156被选部件组合；156–177hold|三层部件位置稳定，组装身体居中|Vessel不给Kris头发和衣色，非创建Kris
243|参数属于造物|Creation|SUPPORT|parameters|E01|Parameters配置姓名/偏好，创建期待暂成立|177–211两小槽逐次填；211–243Vessel稳定等待启动|组合Vessel左中、参数槽右侧|槽标签NAME/TRAIT为作者示意，不编造游戏完整参数
269|初始化收回主体权|Creation|HERO|discard|E01|Initialization断裂期待，Player没有最终主体选择权|243–251造物及槽退暗；251–269空位，无Kris重叠|固定空台后269硬切另一空间|禁止morph、换色或与Kris同锚点叠化
385|同一世界的两种尺度|Creation|SUPPORT|arrival|E01 E02|World是角色生活，Simulation是输入者可回访的接口|269–306Kris已在房内；306–385门光引至地面，SAVE细线短显后退|既存卧室里完整Kris居右|不判哪侧更真实，不把接口当创造身体
476|输入帮得上忙|Union|SUPPORT|help_path|E03|输入解决一次间隙，walking together是情感基础|385–432Kris跨路；432–476Susie另步跟上|世界横向宽景，小输入大动作|作者合作blocking，非新游戏剧情
567|拒绝仍属于同行者|Union|SUPPORT|refusal|E03|Susie拒绝一次方向与后续自愿合作形成变化|476–500提示；500–535Susie偏离；535–567回看Kris|同一地面camera留Kris|不表示永远不可指挥或背叛
715|愿意伸来的手|Union|HERO|welcome|E03|We成立之前先让合作成为可以相信的关系|567–615Susie靠回；615–655手相近；655–715停留呼吸|暖地面两人中近景，UI退|握手是作者关系比喻，不新增canon对白
890|测得轨迹不是整个人|Union|SUPPORT|math_points|E21|If/Then是条件给予，可建模不等于主体被穷尽|715–803步点；803–840地面圆弧；840–890手越预测弧|斜光完整身体，测量只在地面|不把Kris变成点/圆，不声称越出地图规则
1066|模型无法回答的手|Union|SUPPORT|math_wave|E21|Sine/tangents/infinity/limitations是接触机会与边界|890–980波线预测步幅；980–1014脚停手动；1014–1066线碰边界|身体中景、波线低地面|模型线不是Kris本体或无限能力
1235|模式切换而身体仍同一|Union|TRANSITION|mode_switch|E03|AC/DC/vision/dizzy是状态/观测切换|1066–1145光暗域横移；1145–1192视野短窄；1192–1235回归|共同地面同一身体、同一胸心|禁止Dark被控/Light自由等号
1417|我们在此停留|Union|BREATH|party_breath|E03|We/unite是真实相互温度|1235–1322三人同路；1322–1417等彼此并呼吸|宽景慢横移，Kris在前|时空用旧脚印反光概括，不新增时间旅行或Ralsei管理员
1591|想再看看另一条路|Consumption|SUPPORT|curiosity|E02 E08|Simulations/Only/Satisfaction从探索渐成独占满足|1417–1513第一次回访；1513–1551旁路再亮；1551–1591伙伴等待|同地面回访弱影渐多，身体为实|不生成/删除真实时间线，不立即Snowgrave
1774|第一次执行可以帮助|Consumption|HERO|first_execute|E03|首Execution是run/action/cooperation；共有可达边界|1591准备；1637–1667输入触发抬路板；1667–1718Susie过；1718–1774拉宽见路边|木板、手、同伴占大面积|首次无血/冰/坠落；暖行为为作者blocking
1951|给养只是一餐|Consumption|SUPPORT|giving|E03|Eggplant/Tomato/Give是普通给予，不需meta奖励|1774–1865Kris递食物；1865–1902Susie接过；1902–1951缓坐|暖桌中景，紫长形与红圆道具|野餐是生活性作者隐喻，不假造canon新事件
2043|无需命令的回应|Consumption|BREATH|cat_care|E03|Tabby/purr/enjoyment留日常陪伴|1951–1991猫近手；1991–2043抚摸/回蹭，Susie远处放松|低机位手/猫，绿袖可辨|猫不命名canon角色，不上宏大meta
2125|控制也需要世界回应|Consumption|HERO|dependency|E01 E21|Only God/proof是控制者的权力依赖接口与世界|2043–2080输入无完成反馈；2080–2125身体回应后接点亮，世界一直在|先输入尝试，再完整身体/手|不声称Kris没有Player就无法存在；不确认谁是God
2382|切换的是关系角色|Consumption|SUPPORT|role_switch|E03 E21|gender/role/AM-PM/S-M转译呈现、队形、工作/控制角色|2125–2205光暗衣装；2205–2295同手日常；2295–2382队形和接点换|同一身体横穿光域，短接点非属性表|不改变Kris性别；S/M性双关强度留艺术gate
2650|连接曾经确实完整|Consumption|SUPPORT|shared_rhythm|E03 E21|Vibrations/completion是功能和关系合拍|2382–2485各自动；2485–2571同拍；2571–2644胸心/body完整；2644–2650手近胸|慢近到胸/肩/手，同房间|完整不等于缺Player就缺人格/不能生存
2838|同一次缺席反复确认|Consumption|HERO|absence|E04|Left重复同一次absence，双方仍存在而空间分隔|2650–2674取出同心；2674–2693入笼；2693–2728心移；2728–2784身体走开；2784–2838距离hold|连续同房间拉宽，同时见身体和笼心|禁止六次抽心/退出，不表示永久自由
3014|无用是目标赋予的判断|Consumption|HERO|pruning|E08|Fragments/erase是目标导向可能性剪枝|2838–2885三路；2885–2928一条标亮；2928–2972旁路压灰；2972–3014身体沿窄路|俯视下到身体，灰路不消灭人物|不声称时间线物理删除；I暂取目标优化位
3232|谁向谁提交参数|Execution|HERO|illegal_attempt|E15 E16 E28|God/Arguments并存Kris↔输入与Player↔实现规则|3014–3093Kris收手；3093–3149外输入仍撞边；3149–3232被上游入口退回|身体/接点/尽头边界三空间平面|不锁死God或主语，不给Story/Gaster脸
3549|特殊结果需要更多条件|Execution|SUPPORT|threshold|E08 E15|器乐积累压力，偏离也遵守另一套门槛|3232–3340折返；3340–3450侧门渐暗；3450–3549路窄且输入频率加|从俯视缓到侧视，Kris最大|Sword非Snowgrave必然续篇，条件压缩非完整攻略
3821|同一个词十二种恶化|Execution|HERO|execution_chain|E04 E09 E10 E18 E19 E20 E24 E26 E32 E33 E34|Execution变强制/消灭阴影/过程身份，每次推进关系|十二原起音触发不同接点/身体/路径动作；Kris稳定载体，见十二状态表|Kris左中，右Noelle/TV/vent主题换载体|跨章预演非chronology；只有一冰封节点，不能等同十二击杀
3902|不同输入同一接口|Execution|TRANSITION|count_interfaces|E14 E15|多语计数是同接口可重复调用的作者回声|3821–3880三弱线依次到同一心；3880–3902端点归HERO|实体TV、左前景Kris/controller|各国Player不是canon，不用有脸Player群像
3988|Them：输入离开身体|Execution|HERO|screen_exit|E18|Them明确传播第三者；对象与Kris可分离|3902–3938HERO跨屏；3938–3962camera追；3962–3988Kris侧缘，输入端点仍HERO|TV/carrier/Kris三平面，来源固定画面|不把HERO变成人类Player灵魂或Kris新身体
4072|过程无法穷尽这只手|Execution|HERO|protect|E19|Only execution压缩主体成过程，但身体动作反证|3988–4000攻击预示；4000–4012Kris先伸手；4012–4030拉Susie；4030–4040攻击旧空位；4040–4064Susie拔线；末hold|身体抢回camera，两人不遮挡；输入到断线都留HERO|保护不是零责任证书；红心断线后仍在
4164|想要回来成为重新进入|Execution|HERO|reentry|E20 E24 E26|Have you back/run同时含依恋、恢复接口与入侵|4072–4084竖菜单门；4084–4110vent到门；4110–4138至胸；4138–4164身体微退|暖门内Kris/Noelle，外暗vent，同心连续路径|Ch4主题切换非Ch3必然下一刻；不假造道歉目击
4259|我们仍被困在关系里|Execution|SUPPORT|bed_drag|E31|We/trapped含双方，输入成本增加而身体不归零|4164–4200撑地；4200–4259更多输入只抬少许|低机位大身体、小pulse，绿色衣袖持续|迟缓原因未知，不能配仇恨Player独白
4430|学习爱，学习被回答|Recursion|SUPPORT|love_training|E32 E33|Love先是感情回应；Noelle主动索求不证明自由|4259–4319她主动伸手；4319–4344才带菜单；4344–4430Stop留差异痕仍前行|湖双手世界先于UI，回收暖动作|不新增告白；love不等于LV，I暂不锁单人
4519|答对也未拥有爱|Recursion|SUPPORT|love_algebra|E33 E34|Questions/algebra把关系变合规答案仍无法完成握手|4430–4436两词hold；4436–4442Stop退；4442–4448同文；4448–4460心换位手不同步；末迟疑|两手近景加小回答框；人先于字|一瞬UT/LV阴影属作者联想，不替代感情本义
4574|You能停下这次输入|Recursion|BREATH|cease_input|E36|Free此句明确Player相对停止/离开能力|4519–4531pulse停/menu退；4531–4543关切余影；4543–4574心/身体/后果留|camera拉宽，无PAUSE按钮|停止可改变进程，不是所有伤害RESET
4654|I仍等待关系回应|Recursion|SUPPORT|continue_input|E32 E34|Trapped in Love是依恋与接口纠缠，不只是暴力指数|4574–4601再伸手；4601–4621第二回答收窄；4621–4654心趋白、手未握住|先未完成的手距离后小Proceed|不诊断角色心理，不化约love成Level Of Violence
4863|离开身体后还有边界|Recursion|HERO|crt_reveal|E35|相对自由成立后，才揭有效操作的上游边界|4654–4734持续动作世界拉成CRT；4734–4814露机身/input plug；末hold可辨Kris|唯一大边界，实物厚度/桌脚|Story不拟人；不证明所有人完全不自由
4929|边界里的手仍未完成|Recursion|BREATH|hand_aftermath|E04 E36|尾奏保人物余波，不给全层级零自由答案|4863–4895绿袖缓进；4895–4929手停、水纹/呼吸动|手近景，心与掌心有空隙|不把伸手定求死、同意或获救
4970|最后调用者不署名|Recursion|TRANSITION|final_pulse|E35|最后Execution让executor/executable方向开放|4929–4935接点亮；4935–4962hold；4962–4970收至4969的1px扫描线|手/心/接点，无新人物或更大框|硬切继承timing，AUDIO REVIEW PENDING
5030|下一章是要求也是缺口|Recursion|SUPPORT|chapter_cut|E35|章界接住越界但不提供未来剧情|4970–4994纯黑24帧；4994–5002短提示；5002–5026hold；5026–5030退|纯黑后36帧短章提示|Side B未证明自由，不画未发布Chapter7
5086|谁执行谁仍是问题|Recursion|BREATH|unresolved|E35 E36|结尾是层级问题，非三方善恶答案|5030–5048袖/心低光；5048–5051空隙；5051–5057作者问题；末hold|开放手/心不闭框、不胜利pose|作者问题不是角色canon对白
'''
STATES={
'Creation':('配置/输入可用，但最终主体权被收回','独立于造物的既存主体','已有世界关系，不由Player初始化创造','开场流程提供权限又撤回'),
'Union':('能帮助与合作，不统辖全部回应','技能/身体/手超出被读到的数据','拒绝、自愿靠回、等彼此','可达空间与接口有限但关系真实'),
'Consumption':('回访欲望渐强，独占满足和剪枝成为危险','仍是持续主体，功能合拍不等于生存绑定','生活性回应不等于可调用价值','非目标路径被搁置，而非世界被删除'),
'Execution':('输入传播、对象转移、过程收窄','低伏/保护/分离/重入均保独立身体','Susie拒绝/介入；Noelle服从与主动纠缠','越界亦通过已实现门槛，非有脸反派'),
'Recursion':('可停止/离开，相对自由是真的；不能写新章节','手/衣袖留后果，不归零为函数','主动索求不证明自由，回答不穷尽爱','章界/可接受结果限定有效行动')}
EXECUTION=[
(67,'要求','command','E10','心→Kris手→Noelle前压'),(68,'拒绝未停止指令','refusal','E10','Noelle手后退而输入仍进'),(69,'声音越过低伏身体','voice','E09','Kris低伏，接点直接到Noelle'),(70,'消灭语义进入','freeze','E10','远蓝轮廓冰封；不判死亡'),(71,'结果锁住旁路','lock','E08 E10','侧路灰退，人物不删'),(72,'对象换内屏','target','E18','端点从Kris移向HERO'),(73,'越屏仍被指挥','cross','E18','HERO跨边，心线仍到它'),(74,'身体先保护别人','protect','E19','Kris拉手挡开Susie'),(75,'输入与身体分隔','separate','E04 E20','心到通道，身体仍动'),(76,'重入带来反冲','reentry','E24 E26','心近胸，身体手退'),(77,'第三者主动索求','request','E32','Noelle手向input伸'),(78,'趋同与继续期限','deadline','E33 E34','同文Proceed与收框；仍能停止')]
# Per sung-line semantic groups; expand ranges to individual rows. Keywords only.
# ids | keywords | English paraphrase | dual sense | pronouns/DR | visual | avoid | decision
LEDGER='''
0|Switch / power|Enable an input channel|电路/接口被允许|外输入→创建台|一点沿线路到台|不是从无创造Kris|采用
1|Protection|Prepare a protective container|保护/边界伏笔|创建者→Vessel|四角先作邀请|不是首秒牢笼|采用
2|Pieces|Arrange separate parts|部件/对象化可能|对象尚非Kris|头身腿分层选配|不止灰人站着|采用
3|Object / creation|Construct a configured object|对象创建/主体所有权期待|Player→临时Vessel|部件组成完整灰形|造物不是Kris|采用
4|Parameters|Supply configurable values|参数/主体不可穷尽|Player→Vessel|名字/偏好槽亮|不造Kris参数表|采用
5|Initialization|Start the configured process|启动/权限收回|Story撤回配置主体权|创建台退暗→空位|禁止Vessel morph Kris|采用
6|World / our|Establish a shared world|共同经历/角色生活|I为关系供给端；our为连接双方|既存卧室/身体|不判世界假|采用
7|Simulation|Begin an interactive run|可回访game/不可抹平生活|Player可读接口与Kris实景并存|SAVE边缘暂现|非模拟论canon|采用
9-10|If / Then / Give / dimension|Offer dimensions under a condition|条件给予/可读性质|I偏Kris经验，you偏输入者|脚步点投影|可建模≠可穷尽|采用
11-12|If / Then / circumference|Offer a boundary when modelled|测量/可达关系|you读取范围不等于拥有全部人|脚边弧，手超出预测|不把身体变圆|采用
13-14|If / Then / sine / tangents|Offer contact along a wave|函数/接触机会|双方连接可有亲近|波线贴地，手另动|不堆图标|采用
15-16|If / Then / infinity / limitations|Invite limits near an unbounded value|极限/关系边界|you能提供限制有两义|模型延到边，人完整|不声称无限能力|采用
17-18|Switch / AC / DC|Change the current mode|电流/呈现状态|归属看心/行为，不看颜色|光暗横移身体|Dark≠受控；Light≠自由|采用
19-20|vision / dizzy|Limit vision and disrupt orientation|感官/观测范围|可见范围不是世界范围|camera偏移后归位|不是病理诊断|采用
21-22|We / AD / BC|Imagine travelling together through time|想象/回访|we真实共经历|共同脚印反光|不新增时间旅行canon|采用
23-24|We / unite / deeply|Describe a deep union|组合/亲密合作|Kris与输入者可以合拍，伙伴亦回应|等彼此，UI退出|union不是占有|采用
25-26|If / Give / simulations|Offer multiple possible runs|可能性/内容消费种子|you偏Player curiosity|第一次回访与旁路|不立即Snowgrave|采用
27-28|Then / Only / Satisfaction|Seek exclusive fulfilment|优化目标/独占满足|I趋向内容供给过程|伙伴等，路径标光增多|Only有危险但不纯恶Player|采用
29|If / happy|Link action to another’s happiness|输出/关切|you可开放到输入者或关系对象|Kris准备帮抬路板|happy不是杀戮快感|采用开放you
30|Execution|Run an action intended to help|run/协作执行|I=行动中Kris，输入有帮助|抬路板，Susie通过|首次无血/冰/坠落|采用
31-32|We / Trapped / Simulation|Recognise shared bounds|程序可达域/关系约束|we含两端，有限不虚假|拉宽看路边|非人人零自由|采用
33-34|If / Then / Give / eggplant / nutrients|Offer ordinary nourishment|供给/照顾|you转普通受赠同伴|暖桌紫食物|不强贴宏大meta|采用角色间you
35-36|If / Then / tomato / antioxidants|Offer everyday care|营养/非功利给予|Kris/Susie日常|红食物接手|野餐不是canon新事件|采用
37-38|If / Then / tabby / purr / enjoyment|Respond with simple comfort|回应/陪伴|you允许日常对象|猫回蹭绿袖手|无猫God理论|采用
39-40|If / Then / Only / God / proof|Make power depend on a responding world|权限/关系证明|I暂取Player-like控制位；you=Kris/world回应|接口等身体后亮，世界不消失|不无Player就死，不确定神身份|采用暂换叙述位
41-42|Switch / gender / F / M|Switch an identity presentation|性别歌词/状态转译|原歌双关开放；身体始终Kris|光暗呈现切换|不改Kris性别|采用呈现转译
43-44|whatever / AM / PM|Extend actions across the day|时间覆盖/随时可达|角色也有自身日常|同一手日夜劳动|不是控制全部人生|采用
45-46|Switch / role / S / M|Exchange relational roles|支配服从/性双关开放|controller/controlled位置可变|队形和接点换|不替Kris定性倾向|本轮角色转译，字面强度待艺术gate
47-48|We / trance|Enter absorption together|投入/同拍失神阴影|双方连接有效|手/同伴动作趋同|不直接canon洗脑|采用关系投入
49-50|If / vibrations|Sense a partner’s response|输入振动/感应|I偏Kris，you=连接回应|分别动作靠同拍|无SOUL电磁设定|采用
51-52|Then / completion|Experience functional completion|完成/合拍|人格完整不依接口|完整身体胸心手同框|无Player不能存在禁止|采用
53-58|You / left / isolation|Recognise one continuing absence|离开接口/关系缺席|you偏Player，控制空间分隔|同心一次入笼、身体一次走开|非六次抽心或角色消失|采用持续absence
59-60|If / erase / pointless / Fragments|Discard options judged unhelpful|剪枝/意义被优化|I暂取目标优化位，Player-like视角|旁路灰退，人还在|无物理时间线删除|采用目标视角
61-62|Then / maybe / disheartened|Hope that pruning prevents loss|优化希望/被留下感情|I/you不唯一，双方均可读|身体在窄路，灰路仍留|不替伤害免责|采用开放代词
63|Challenging / your / God|Challenge a higher authority|局部冲突/上游规则|you可Player，God可rules；保留Kris↔input|身体收手/外输入撞界同时|不锁死Kris挑战Player/Gaster|采用双层
64-65|You / Arguments / illegal|Submit unacceptable inputs|参数校验/关系越界|you偏输入者，由更高接口判定非法|接点离体又被门槛退回|不把作者判Player有罪|采用双层
79-82|count / Execution|Count across languages via one procedure|多语/同接口调用|多Player是作者隐喻，非canon|三弱输入落同接点|不国家Player事实化|采用弱隐喻
83-84|If / Give / Them / Execution|Extend the process beyond a pair|传播/第三者执行|them明确Noelle/Susie/HERO，you偏Player|HERO出屏，Kris仍主体|后半非Noelle击杀MAD|采用Them扩展
85-86|Then / Only / Execution|Reduce a self to a process|过程身份/处决阴影|I有Kris被过程化的一层，手反证非空壳|Kris保护抢camera，Susie拔线|压缩是危机不是本体|采用动作反证
87-88|If / back / Execution|Seek reunion by restarting a process|依恋/接口恢复及入侵|I/you维持关系与控制双义|心穿门重入，身体退|重入不等于自愿|采用
89-90|We / Trapped|Repeat a shared constraint|程序限制/关系难脱|we含双方，不抹相对自由|起床迟缓，输入成本增|不是人人零agency|采用
91-92|I / studied / Love|Learn a way to offer affection|学习关切/训练回应|I不锁单人，Noelle让关系反转|主动手回收暖动作后才menu|love先感情不等于LV|采用开放I
93-94|question / answer / Love|Treat affection as answerable|答题/回应不等于关系完成|Noelle索求，Kris与Player各处回答层|Stop有差异痕仍前移|主动不等于自由|采用
95|algebraic / expression / Love|Claim a formal expression for affection|代数形式/主体超出公式|I开放；程序能答而人未握手|同文、左右心、迟疑手；一瞬LV|LV仅UT作者回声非love定义|采用；阴影强度待艺术gate
96|You / Free|Grant relative freedom to the addressee|退出能力/观察层级|此句稳定you=Player|pulse停，身体/后果持续|先承认停止能力|采用稳定you
97-98|I / Trapped / Love|Remain caught in seeking a response|依恋/接口约束|I偏关系内Kris，Noelle为镜但不锁独白|绿袖/心有空隙，再求回答|不心理诊断或暴力数值化|采用
100|Execution|Leave the final caller unresolved|运行/谁执行谁|I/you不署名|接点→扫描线→黑→章界→手|不杀Player，不展示未来结局|采用开放caller
'''
OLD_REASONS='''供电具体化;保护先邀请;部件真实选配;Object组装期待;恢复Vessel参数;否定同锚点叠化;另处已有Kris;输入帮助;同行身体动作;Susie拒绝;合作延长;删除早SAVE插断;测量不能代人;删圆菜单;波线贴地手另动;模型未完成;模式切换非控制切换;camera视野非TV教程;旅行弱影非时间canon;真实同伴温度;删除过早NEO;删除首次执行前切线;首次执行重做帮助;删除过早坠落;日常食物替organ;普通给予非理论卡;猫与回应;权力依赖世界而非SAVE占有;同一身体呈现;日夜同手;关系role非性别改造;技能与input共存;真实合拍;completion不生存绑定;同心一次离体;合并持续absence;合并身体不随心;保护边回收成笼;一次自主走开;同次缺席hold;删除此处私话改剪枝;重入移have-back;God双层冲突;锁定移十二节点;反冲移十二节点;越身体命令移节点;门槛作器乐压力;删除无限套框;前六变关系状态;后六变对象/边界/主动;计数为作者接口回声;保留出屏空间;保留保护拔线;归来重做物理重入;We双侧迟缓成本;主动索求留Love感情;Stop留差异非全无效;同文与未完成手并置;先承认Player能停;爱与接口纠缠;唯一上游CRT揭示;实体机身非大框;身体余波;最后caller不署名;章界不画未来;开放手与心;作者问题不善恶判决'''.split(';')
BEATS=[(0,16,1,'Creation：期待→权利断裂'),(16,29.79,2,'Union：谨慎→温暖'),(29.79,44.42,3,'Union：好奇/建模未尽'),(44.42,59.04,2,'Union：真实合拍'),(59.04,73.92,3,'Consumption：探索→独占→善意执行'),(73.92,88.54,1,'Consumption：生活暖→权力依赖'),(88.54,103.54,4,'Consumption：角色投入'),(103.54,118.25,5,'Consumption：完整→持续缺席'),(118.25,134.67,7,'Execution：剪枝→两层违规'),(134.67,147.875,8,'Execution：条件压力'),(147.875,162.583,10,'Execution：十二关系滑移'),(162.583,177.458,8,'Execution：失控→保护→重入'),(177.458,190.583,9,'Recursion：依恋→合规不等于爱'),(190.583,202.625,6,'Recursion：相对自由→上游边界'),(202.625,211.917,3,'Recursion：余波→未决')]

def build():
    timing=json.loads((ROOT/'data/timing/word_timeline_notext.json').read_text(encoding='utf-8'));words=timing['skeleton']['words'];shots=[];start=0
    old=json.loads((ROOT/'docs/deltarune/archive/v01/shot_plan.json').read_text(encoding='utf-8'))['shots']
    for i,line in enumerate(ROWS.strip().splitlines(),1):
        end,title,act,budget,scene,refs,purpose,motion,camera,risk=line.split('|');end=int(end);refs=refs.split();sid=f'LR{i:02d}';pp,kk,oo,ss=STATES[act]
        on=[dict(line_id=w['line_id'],word_index=w['word_index'],source_seconds=w['start'],frame=round(w['start']*24)) for w in words if start<=round(w['start']*24)<end]
        shots.append(dict(id=sid,title=title,section=act,start_frame=start,end_frame=end,start_time=start/24,end_time=end/24,frame_interval='[start,end)',song_cue=dict(semantic_description=purpose,line_ids=sorted({w['line_id'] for w in words if w['start']<end/24 and w['end']>=start/24}),word_onsets=on,instrumental=not on),
         chapter='Ch1–5 thematic; each evidence defines its event',route='normal/author metaphor' if act in {'Creation','Union'} else 'thematic, not chronological route walkthrough',canon_evidence=refs,evidence_usage={e:purpose+'；仅01该E可见事实；细节为作者blocking' for e in refs},claim_scope='歌词转译/跨章主题cut，非新canon或游戏连续录像',narrative_purpose=purpose,
         player_state=pp,kris_state=kk,other_character_state=oo,story_state=ss,agency_preset=act,shot_budget=budget,scene=scene,layout=scene,camera=camera,legacy_source_shots=[s['id'] for s in old if s['start_frame']<end and s['end_frame']>start],
         foreground=dict(description='Kris持续身体/手；前三镜仅Vessel，LR04空台',reason='人物先于概念'),background=dict(description=camera,reason='可达空间和距离'),ui_elements=dict(description='接点/参数/边界需要时才显，无ticker',reason='接口不能代替表演'),text=dict(content='NAME/TRAIT' if scene=='parameters' else 'Insert Chapter 7 / Side B' if scene=='chapter_cut' else 'Who executes whom?' if scene=='unresolved' else 'Stop/Proceed' if scene in {'love_training','love_algebra','continue_input','execution_chain','reentry'} else '无',provenance='短接口词/作者问题，非歌词全文',reason='一镜一个关系变化'),character=dict(primary='Vessel或空台；Kris另一个既存主体' if end<=269 else 'Kris',art_status='本轮仅文本分镜；既有几何材料为历史机制参考',reason='他者用于关系参照'),soul=dict(description='同一主要输入接点；与身体可分；不裁定本体',reason='可追踪对象'),
         transition_in='黑场一点' if not shots else shots[-1]['transition_out'],transition_out=('空台后硬切另处Kris' if scene=='discard' else '动作/地面/手的主题match到下一空间；具体见11'),transition_intention='人物、接点或地面的主题match；不复用DSH填洞',colour=['#19202D','#75A58B','#D5BE8A','#F04462'],motion=motion,movement_intention=motion,effects='接触光/水纹与明确动作，无generic glitch',original_repo_components_reused=['film/tui_pv_world_execute_20260926/tuikit.py:font'],original_elements_decision='KEEP timing；REPLACE旧pane；REMOVE旧DSH画面',new_code_required=[f'film/deltarune_poc/lyric_scenes.py:{scene}','film/deltarune_poc/renderer.py:frame'],assets_required=[dict(asset='原创几何人/世界/手',source='程序绘制，无游戏sprite',status='BLOCKING ONLY')],unresolved_question=risk,validation_frames=sorted({start,min(start+12,end-1),(start+end)//2,end-1}),key_events=[],implementation_status='textual shot analysis; no visual implementation acceptance this round',technical_implementation=dict(medium='PIL/RGB per-frame authored world',new_section_path_planned=f'film/deltarune_poc/lyric_scenes.py:{scene}',legacy_monkey_patch='none',proof_renderer='film/deltarune_poc/renderer.py',proof_scope='space/actions only, human ART GATE pending')))
        start=end
    pulses=[dict(line_id=i,frame=round(min(w['start'] for w in words if w['line_id']==i)*24),meaning=m,mode=mode,evidence=refs.split(),action=action) for i,m,mode,refs,action in EXECUTION]
    events=[]
    for scene in ['discard','absence','pruning','illegal_attempt','execution_chain','screen_exit','protect','reentry','cease_input','crt_reveal','chapter_cut']:
        s=next(s for s in shots if s['scene']==scene);eid=f'K{len(events)+1:02d}';s['key_events'].append(eid);events.append(dict(id=eid,kind=scene,shots=[s['id']],start=s['start_frame'],end=s['end_frame'],steps=[[s['start_frame'],s['end_frame'],s['motion']]]))
    return dict(schema_version=3,design_version='0.3',checked_on='2026-10-04',status='NARRATIVE AND SHOT ANALYSIS ONLY',rendering_excluded_this_round=True,baseline_commit='cb63fb6ba5832da38d79f95b8469464c1e2ddbf4',fps=24,resolution=[1280,720],nominal_duration_seconds=211.9,encoded_duration_seconds=5086/24,frame_count=5086,hard_cut_frame=4970,black_hold_frames=[4970,4994],timing_source='data/timing/word_timeline_notext.json',timing_source_sha256_expected=timing['sha256'],evidence_register='docs/deltarune/01_CANON_RESEARCH.md',minimum_reference='docs/DR_PV_MINIMUM_STORY_REFERENCE.md',audio_review='PENDING',game_visual_review='R01–03 PENDING',art_review='EXCLUDED THIS ROUND; later human gate only',execution_pulse_anchors=pulses,execution_shot=next(s['id'] for s in shots if s['scene']=='execution_chain'),frame_events=events,shots=shots)


def write_bible(p):
    out=['# 211.9秒 Shot Bible v0.3','','歌词与作者意图高于旧方案。source of truth：tools/design_deltarune_plan.py。38镜/5086帧/24fps；395个原逐词起音保留。源脚本同时生成06/09/10与JSON。','','AUDIO REVIEW PENDING；R01–03待核。本轮仅剧情和分镜分析，不做任何艺术加工；此前几何PoC和无声rough仅保留为历史机制材料，不作为本轮交付或验收依据。','','## 结构与预算','',str(dict(Counter(s['shot_budget'] for s in p['shots']))),'','| 镜/预算 | [a,b) | 时间s | 目的 |','|---|---|---|---|']
    for s in p['shots']:out.append(f"| {s['id']} / {s['shot_budget']} | {s['start_frame']}–{s['end_frame']} | {s['start_time']:.3f}–{s['end_time']:.3f} | {s['title']} |")
    for s in p['shots']:
        out.extend(['',f"## {s['id']} — {s['title']}",'',f"[{s['start_frame']},{s['end_frame']})；{s['section']} / {s['shot_budget']}；词行IDs{s['song_cue']['line_ids']}。",f"歌词意图：{s['narrative_purpose']}。",f"Player：{s['player_state']}。Kris：{s['kris_state']}。Other：{s['other_character_state']}。Story：{s['story_state']}。",f"空间/camera：{s['camera']}。",f"动作：{s['motion']}。",f"入：{s['transition_in']}。出：{s['transition_out']}。",f"输入：{s['soul']['description']}。文字：{s['text']['content']}。",f"证据：{' / '.join(s['canon_evidence'])}；{s['claim_scope']}。",f"误读边界：{s['unresolved_question']}。",f"分镜时间复核：{s['validation_frames']}；历史机制参考：{s['technical_implementation']['new_section_path_planned']}，不在本轮实施。",'范围：只分析空间、动作、叙事与剪辑；造型、画面加工和艺术实现均不在本轮进行。'])
    out.extend(['','## 十二次Execution关系状态','','同一LR24载体、原起音；跨Ch2–5主题预演，后续长镜再展开；不是chronology或必然route。','','| 行/帧 | 状态 | 空间动作 | 证据 |','|---|---|---|---|'])
    for a in p['execution_pulse_anchors']:out.append(f"| {a['line_id']} / {a['frame']} | {a['meaning']} | {a['action']} | {' '.join(a['evidence'])} |")
    out.extend(['','09逐行语义；10否定/去向/曲线/motif；11实际render/视觉检查。全文歌词只在忽略input，本稿不复制。'])
    (ROOT/'docs/deltarune/06_SHOT_BIBLE.md').write_text('\n'.join(out)+'\n',encoding='utf-8')


def write_ledger(p):
    words=json.loads((ROOT/p['timing_source']).read_text(encoding='utf-8'))['skeleton']['words'];rows={}
    for line in LEDGER.strip().splitlines():
        ids,*v=line.split('|');a,b=map(int,ids.split('-')) if '-' in ids else (int(ids),int(ids))
        for i in range(a,b+1):rows[i]=v
    for n in p['execution_pulse_anchors']:rows[n['line_id']]=['Execution',['Enforce an input','Persist across refusal','Transmit beyond the body','Introduce elimination','Lock alternative paths','Transfer the controlled target','Cross a screen under control','Act autonomously to protect','Separate input and body','Re-enter with recoil','Request commands actively','Converge results and require continuation'][n['line_id']-67],'从run转强制/消灭阴影/过程化','关系第'+str(n['line_id']-66)+'次变化',n['action'],'不是第'+str(n['line_id']-66)+'次击杀','采用']
    sung=sorted({w['line_id'] for w in words});assert sorted(rows)==sung,(set(rows)^set(sung))
    out=['# LYRIC INTENT / DIRECTOR LEDGER v0.3','','2026-10-04。作者最新意图→01事实→02反证→最低参考→英语结构与timing→历史03–08/PoC。已完整读本地英文歌词；表只列关键词和英文语义转述。98非空唱词行各一行，行ID承接原timing；8/66/99器乐段不造歌词。','','## 条件结构与代词','','If/Then先是提供自己的可读性质/接触机会，再成为满足you的极端优化；Only使目标排他，Them把输入扩到第三者，最后I被压成执行过程的危险却被Kris的保护手反证。','','I/you不全歌锁死：数学/合拍偏Kris经验与输入者；日常you开放到同伴；God/proof暂取控制位与世界依赖；剪枝暂取目标优化位；God/arguments保留局部意愿与上游rules；Love的I开放；Free这一句明确you=Player能停，再在尾奏拉出上游边界。这些是作者转译，非新增角色知道现实Player的对白。','','Execution三义：LR14善意run→LR22/23条件施压→LR24十二关系恶化/消灭阴影/过程身份；最后caller不署名。World与Simulation同一空间两观察位，不判谁更真实。Love先感情，LV仅跨作品阴影。','','确认策略：本轮没有需要暂停结构实施的必答项。数学、God双视角、S/M角色转译、开放Love叙述位均作可复审导演选择；S/M性字面强度、LV显著度、表演读法待下一独立人类艺术gate，不逐镜询问。','','## 逐行语义','','| 行 / 起音s / frame | 一级词 | English sense（转述） | 技术/关系双关 | DR关系/代词 | 视觉/镜 | 不应误读 | 确认 |','|---|---|---|---|---|---|---|---|']
    for i in sung:
        f=round(min(w['start'] for w in words if w['line_id']==i)*24);kw,en,dual,rel,vis,avoid,decision=rows[i];sid=next(s['id'] for s in p['shots'] if s['start_frame']<=f<s['end_frame'])
        # If and Then are individual rows even when they share one relationship.
        grammar='条件前件；' if i in [9,11,13,15,25,29,33,35,37,39,49,59,83,87] else '条件结果；' if i in [10,12,14,16,27,34,36,38,40,51,61,85] else ''
        out.append(f'| {i} / {f/24:.3f} / {f} | {kw} | {en} | {grammar}{dual} | {rel} | {sid}：{vis} | {avoid} | {decision} |')
    (ROOT/'docs/deltarune/09_LYRIC_DIRECTOR_LEDGER.md').write_text('\n'.join(out)+'\n',encoding='utf-8')
    return sung

def write_rewrite(p):
    old=json.loads((ROOT/'docs/deltarune/archive/v01/shot_plan.json').read_text(encoding='utf-8'))['shots'];assert len(OLD_REASONS)==67
    out=['# DIRECTOR REWRITE v0.3','','2026-10-04。v0.1的67镜及暂停v0.2都是历史；本轮38镜歌词驱动，不保护旧实现。09_DIRECTOR_REVIEW.md仍保留为上轮记录，新上位导演稿为本文件与09_LYRIC_DIRECTOR_LEDGER.md。','','## 主要否定','','1. 灰Vessel退/绿Kris在同锚点显出不足以防误读。改具体部件/参数→空台→另处既存Kris硬切。','2. 数学图标和常驻pane代替人；改脚步预测/手超模型，保完整身体。','3. 首Execution切最后线/坠落过早阴森；删除此处NEO，改帮助抬路板。','4. 碎片段私话/重入服务事件而非erase语法；改剪枝，重入移have-back。','5. 十二冰柱虽连续仍近击杀计数；改十二次不同关系状态。','6. Love不能只是湖菜单；先回收自愿伸手/给予，再显合规答案不能完成关系。','7. Free先承认Player能停；之后才见上游边界，不能一句话取消相对自由。','','## 五幕与每10–20秒观看问题','','| 秒区间 | 第一眼与情绪变化 |','|---|---|']
    for a,b,v,m in BEATS:out.append(f'| {a:.3f}–{b:.3f} | {m}；主观紧张{v}/10 |')
    out.extend(['','曲线为导演预期，非已听音测量。每段第一眼Kris或开场Vessel；关系列在06及逐行09。完整silent rough只验空间/剪辑，音乐同步保持PENDING。','','![预期情绪曲线](figures/emotion_curve_v03.svg)','','## Motif建立、三次变义、回收','','| motif | 建立/熟悉 | 第二义 | 第三义/回收 |','|---|---|---|',
    '| 输入/同一心 | 配置、善意行动/合作 | 传播、交接、与身体隔离 | 主动索求反转来源；输入能停但接口仍有章界 |',
    '| 手 | 靠近、抬板、给予/抚摸 | 取心、收手、保护、拔线 | 求回应与迟疑；正确答案未完成握手 |',
    '| 条件路径 | If/Then提供接触 | 更多可能变Only目标剪枝 | 特殊结果也走既有门槛，不物理删时间线 |',
    '| 保护边 | 邀请/保护容器 | 笼隔开input与body | 机身/章界接住越界，但Player仍能离开 |',
    '| Execution | LR14中性善意run | 条件强制与消灭阴影 | Only过程身份被手反证，最后caller不署名 |',
    '| Love | 普通给予、等彼此 | 学习回应被优化成合规答案 | 能停也不消后果/依恋，LV只阴影 |','','## 预算','',''+str(dict(Counter(s['shot_budget'] for s in p['shots'])))+'。12 HERO集中在关系变化与动作/空间。Breath有肩/水纹/低幅动作或有意hold；不是静态图片填时长。本轮不作任何艺术加工；原几何实验不作为本轮验收。','','## 全67旧镜去向','','新编号为LR；旧画面不复用。对应表按实际时间交叠，允许多对多重排，理由明确必要性/视觉新意/情绪的替换。','','| 旧镜/秒 | 新载体 | 决定与N/V/E理由 |','|---|---|---|'])
    reviewed=[]
    for i,o in enumerate(old):
        targets=[s['id'] for s in p['shots'] if s['start_frame']<o['end_frame'] and s['end_frame']>o['start_frame']];reason=OLD_REASONS[i];action='删除旧事件/替换' if reason.startswith(('删除','否定','删')) else '重做/合并' if len(targets)==1 else '拆分/重排'
        reviewed.append(dict(old_id=o['id'],targets=targets,action=action,reason=reason));out.append(f"| {o['id']} / {o['start_frame']/24:.3f}–{o['end_frame']/24:.3f} | {'/'.join(targets)} | {action}：{reason} |")
    out.extend(['','## 下一独立艺术gate','','全部38镜都要用户造型/材质复审。高风险：LR02/04 Vessel≠Kris；LR08暖回应；LR09/10投影不是本体；LR14木板重量；LR15/16食物/猫生活性；LR17依赖视角；LR18 S/M强度；LR20同一心取出；LR21剪枝非毁世界；LR22 God两层；LR24十二状态可读；LR26/27保护空间；LR28重入触感；LR30/31 Love与LV显著度；LR32停止余痕；LR34 CRT材质；LR38未完成手。先复审表演/空间，再选风格，不进行最终美术扩张。','','## 15项自检落点','','本轮只进行剧情/分镜逻辑复核，以下是设计落点，不声称实际画面艺术验收；11为先前几何实验的历史记录。'])
    checks=['LR02–04部件/参数/丢弃空位，配置权非主体权','LR05另处既存Kris，不morph','LR06–08/12可信合作','LR09/10身体完整且手超预测','LR14首执行帮助无杀戮','LR13回访→21剪枝→23门槛→24升级','LR15/16普通食物与猫','LR17世界不灭、控制需回应','LR20一次absence持续','LR21灰路保留，目标导向剪枝','LR22局部收手与上游退回并置','LR24十二状态，只有一冰封不判死亡','LR30/31 Love先感情，LV短阴影','LR32先能停，34才上游','LR38手/心开放问题不判三方善恶']
    for i,c in enumerate(checks,1):out.append(f'{i}. {c}。')
    (ROOT/'docs/deltarune/10_DIRECTOR_REWRITE.md').write_text('\n'.join(out)+'\n',encoding='utf-8')
    (ROOT/'data/deltarune/director_review_v03.json').write_text(json.dumps(dict(design_version='0.3',reviewed_shots=reviewed,emotion_beats=BEATS),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    curve=[(0,1),(9,3),(10.4,5),(16,2),(25,1),(42,3),(56,1),(64,3),(70,2),(80,1),(87,3),(101,4),(110,3),(115,5),(123,6),(134,7),(148,8),(158,10),(166,9),(170,7),(176,8),(185,9),(190,7),(194,6),(202,7),(205,4),(207,0),(211.9,3)]
    pts=' '.join(f'{65+t/211.9*1140:.1f},{350-v*28:.1f}' for t,v in curve)
    svg=['<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="440">','<rect width="1280" height="440" fill="#111b29"/>','<g fill="#d3d9e4" font-family="Microsoft YaHei, sans-serif" font-size="18"><text x="65" y="32">v0.3 情绪曲线 · 导演预期 / AUDIO REVIEW PENDING</text>']
    for v in range(0,11,2):svg.append(f'<text x="30" y="{356-v*28}">{v}</text><path d="M65 {350-v*28}H1205" stroke="#2d3c50"/>')
    for t in [0,30,60,90,120,150,180,211.9]:svg.append(f'<text x="{65+t/211.9*1140-8}" y="383">{t}</text>')
    svg.extend(['</g>',f'<polyline points="{pts}" fill="none" stroke="#e2bc86" stroke-width="4"/>','<text x="65" y="420" fill="#95b4aa" font-size="17">期待 → 合作 → 消费 → 条件/执行 → 相对自由与上游边界 → 未决</text>','</svg>'])
    (ROOT/'docs/deltarune/figures/emotion_curve_v03.svg').write_text('\n'.join(svg),encoding='utf-8')

def main():
    p=build();(ROOT/'data/deltarune_shot_plan.json').write_text(json.dumps(p,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');write_bible(p);sung=write_ledger(p);write_rewrite(p)
    print(json.dumps(dict(version=p['design_version'],shots=len(p['shots']),sung_lines=len(sung),frames=p['frame_count'],budgets=dict(Counter(s['shot_budget'] for s in p['shots']))),ensure_ascii=False))
if __name__=='__main__':main()
