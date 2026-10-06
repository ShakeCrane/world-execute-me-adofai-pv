# 素材授权来源与核实范围

核实范围：上游来源为 2026-09-30 的既有核实，DELTARUNE 本地素材为 2026-10-05—06 的取得与核验。本页记录事实和证据边界，不替代各许可全文。

## DELTARUNE 技术验证素材

2026-10-05 通过 [Deltarune Wiki MediaWiki API](https://deltarune.wiki/api.php) 的 `imageinfo` 获取 URL，并实际下载、解码以下文件。本机输入在 `input/deltarune/`；该目录随整个 `input/` 被 Git 忽略，未把游戏素材重新许可或打包入开源代码。

| 原文件名 | 核实格式与大小 | 用途 |
|---|---|---|
| [Kris_and_Berdly_screenshot_truce.png](https://deltarune.wiki/wiki/File:Kris_and_Berdly_screenshot_truce.png) | PNG，640×480 | 真实游戏画幅、像素观感和窗口合成；自带对白，不是干净场景背景 |
| [Kris_overworld_Dark_World.png](https://deltarune.wiki/wiki/File:Kris_overworld_Dark_World.png) | PNG，38×74，透明 | 独立角色图层 |
| [Kris_overworld_SOUL_remove.gif](https://deltarune.wiki/wiki/File:Kris_overworld_SOUL_remove.gif) | GIF，84×69，61 帧 / 13.29 s | SOUL 取出动作与透明帧合成 |
| [Kris_overworld_SOUL_insert.gif](https://deltarune.wiki/wiki/File:Kris_overworld_SOUL_insert.gif) | GIF，76×66，17 帧 / 8.00 s | SOUL 放回动作与透明帧合成 |
| [Kris_overworld_8bit.gif](https://deltarune.wiki/wiki/File:Kris_overworld_8bit.gif) | GIF，64×64，2 帧 | 前景越窗机制；不能视为 HERO_SWORD 素材 |

取得的是 wiki 发布的游戏截图/角色动画，不是本机录屏或从自有游戏提取的原文件；wiki 图片的尺寸和动画停顿不一定等于游戏内部资源。DELTARUNE 的游戏美术、角色及动画权利属于 Toby Fox 等原权利人，不因 wiki 可下载而成为 MIT 或 CC BY-NC-SA 的资产。实际下载 URL 与 SHA-256 记录在本机 `sources.json`；技术使用方式与验证范围见 [技术可行性报告](HOW_IT_WORKS.md#deltarune-改编技术可行性报告)。

### Castle Town Art / Tech 保留证据（2026-10-06）

这些新增素材仅在本机 `test/art_tech_poc/`，连同派生视频 / PNG 受 `.gitignore` 保护，未自动升级为正式制作素材。当前视觉选择已整理为 [Art Direction Draft](deltarune/ART_DIRECTION_DRAFT.md)，待艺术验收；草案不重新许可或分发游戏像素。

| asset → source | type | local / Git status | confidence |
|---|---|---|---|
| Castle Town 庭院 → [Wiki 原图](https://deltarune.wiki/w/File:Castle_Town_location.png)，640×480 | DIRECT_SOURCE | 收束样片仍需的本地源图；旧分层缓存已清理，Git 忽略 | 高：公开游戏截图，非原作 room / 隐藏几何数据 |
| Castle Town 商店街 → [Wiki 原图](https://deltarune.wiki/w/File:Castle_Town_location_Chapter_2.png)，1120×688 | DIRECT_SOURCE | 保留商店街对照的来源，Git 忽略 | 高：公开游戏截图，非自主录屏 |
| Seam Castle Town 独立 sprite → [Wiki 文件页](https://deltarune.wiki/w/File:Seap_location_Castle_Town.png)，208×226，native 104×113 | DIRECT_SOURCE | 单体体积研究，Git 忽略 | 高：完整源正面；文件页标识 spr_castle_shop_new；没有提供隐藏几何 |
| 第一章 Seam 商店 → [Wiki 截图](https://deltarune.wiki/w/File:Seam%27s_Shop_location.png)，640×480 | DIRECT_SOURCE | 布篷 / 折痕 / 黑色负形参考，Git 忽略 | 高：造型与 Castle Town 不同，不能冒充后者侧面依据 |
| Kris 四方向各四帧 → [DELTAModKit revision c61032a](https://github.com/deltamodders/deltamodkit/tree/c61032a2a6370706242f625b992132ed23b9bd7b/sprites)，19×38，按各 `.yy` 元数据帧序 | DIRECT_SOURCE | 本地研究，Git 忽略 | 较高：公开 Chapter 1/2 项目提供；down 0/2 裁成 19×37 与独立 Wiki sprite 逐像素相同；未从自有游戏提取 |
| 正面 / 道路 / 背景裁切 → 商店街；前景 → 上轮 Wiki Castle Town 原图分层 | DERIVED_SOURCE | 本地合成，Git 忽略 | 像素可追溯；重排位置与深度并非原游戏 room 数据 |
| 侧面、不可见地面、全部推定空间几何、灯光 | AUTHORED_EXTENSION | 技术示例，Git 忽略 | 非原作事实；需要 Art Review |

本地实验清单保留固定下载 URL、revision 和 SHA-256；实际核验了原图 / sprite 哈希与上述独立像素一致性。素材类型描述视觉来源，不能把“表面像素来自原作”误读成“重建的三维空间来自原作”。新增单体的正面分件贴图为 DERIVED_SOURCE；所有深度 / 弯曲、侧帘、侧篷、连接面及折痕布局为 AUTHORED_EXTENSION，即使使用源调色板也不是 canon geometry。所检查的 DELTAModKit revision 未包含所查两个商店 sprite 名称，未取得这座 Castle Town 建筑真实侧后方资料。源色 dominant LOD 与角色封闭孔修补属于派生像素整理；生成 / 恢复模型未参与本轮。

DELTAModKit 的代码许可不被扩张解释为游戏像素再分发许可；未打包游戏素材入 Git。真实姿态可以使用，动画时钟为作者重定时，尚未校准实机步速。当前成果和边界归纳在现有技术报告，删除实验目录不会删除项目主干的来源解释。

当前 18 秒收束样片复用上述庭院原图与 Kris up 四帧、right / down 站姿；没有新增下载或生成素材路线。分层、远景孤立点删除 / 结构线加强和 nearest 姿态 resize 为 DERIVED_SOURCE；入口道路由源图 16×8 紫色色块重复设计，不宣称该色块是原作道路贴图。其布局、所有推定深度、折面背部、边框空间结构、投影词与三档材质光为 AUTHORED_EXTENSION。远景像素改造是设计选择，不是未经修改的 canon 截图。没有使用 B 的整图重建、帧间 AI 重绘或虚构角色动画；仍粗糙的作者几何不被当作来源未知的模型补全。

原庭院 SHA-256 为 `edff8cbbf560cf1b7f955c9e52146850c195e2f884ed5893744f1f54774d27ed`。各角色帧继续使用表中固定 revision 和对应来源哈希；本地样片保留独立来源清单。音乐仍来自既有 `input/song.mp3`，片段时间仅服务本轮视觉节拍，不构成正式歌词映射。素材范围、粗糙处及当前收束判断在技术报告和艺术草案中完整保留，不以实验视频作为唯一解释。

整理后的实验只保留最近代表性对照和有价值反例，不把截图 / sprite / authored scene 批量迁成正式素材。旧静态与 micro-scene 下载脚本已退休，来源 URL、固定 revision、帧序及哈希仍保留；当前庭院源图、四方向源 sprite 与 Seam 两份参考用于本地回看 / 重算，未加入 Git。正式需要的输入仍在 `input/`，删除实验不会删除它们。

后续镜头若采用这些素材，应先在正式输入位置独立取得 / 整理并记录同一 provenance，不能让正式工程读取实验路径。`DIRECT_SOURCE` / `DERIVED_SOURCE` / `AUTHORED_EXTENSION` / `TEMP_PLACEHOLDER` 分类继续适用。新正式工具 `tools/pixel_scene.py` 仅包含数学与栅格操作，没有携带任何游戏像素、来源未知补面或新的获取路线。

## 鲸鱼娘美术

1. 原角色：上善无形 / 上善。署名和许可链见下游保留的 NOTICE；[原作者授权动态](https://www.bilibili.com/opus/1231977657712771073)是进一步核对入口。本次未能实时读取该 B 站动态，不把下游引用写成已实时核验原帖。
2. 女仆二次设计：ZipZipPipe。[Pixiv《AI娘化》](https://www.pixiv.net/artworks/148186519)，作者 ID `18604994`、作品 ID `148186519`。本次通过 [Pixiv 公开接口](https://www.pixiv.net/ajax/illust/148186519)实时核实作者与说明：允许取用，要求标注作者、非商业使用；其中 DeepSeek 娘基于上善鲸鱼娘，遵循 CC BY-NC-SA 4.0。其他角色不能直接套用这项 CC 声明。
3. 立绘：Small-tailqwq / [dsh-deep-whale 的 maid-atelier](https://github.com/Small-tailqwq/dsh-deep-whale/tree/main/maid-atelier)，按上游美术许可链使用。
4. 表情：JAdpp / [dsh-whale-galgame NOTICE](https://github.com/JAdpp/dsh-whale-galgame/blob/main/NOTICE.md)，列明立绘来源与八种新增表情的改编关系。

本仓库保留署名链和上游 NOTICE，许可全文在 `LICENSES/CC-BY-NC-SA-4.0.txt`。改动包括裁切、缩放、调色、像素化、合成、替身摆动及字符网格；只对相应改编部分沿用该许可。上游许可声明不构成对全部潜在第三方权利的保证。

## 音乐与歌词

[Mili Copyright Guidelines](https://projectmili.com/copyright-guidelines)允许个人非商业二创；商业用途按指引另行确认。对全部或部分使用 AI 的同人内容，指引要求明确标注。不得暗示官方作品或官方认可。

原曲和完整歌词不随仓库分发。LRCLIB 下载接口的可访问性不等于音乐或歌词的开源授权。短前缀和连续五词扫描只是打包实现与内容检查，不是法律阈值。

## 原片的 MMD 参考链

原片曾使用 YYB 伯爵女仆模型及动作 01（ドーナツホール，あひるP，编舞足太ぺんた）、02（ハッピーシンセサイザ，ろみ，编舞めろちん）作为参考，再生成舞者画面。

- 模型整包说明包含禁止改造、二配及商业使用等限制；部件的宽松条款不能覆盖整模条款。
- 动作 01 有非商业、使用内容限制、改编与再分发条件；动作 02 允许修改和再分发，并要求合理使用。
- **OPEN QUESTION**：这些现存说明没有明确覆盖 AI 推理参考及其衍生视频。本项目未取得可证明覆盖此用途的补充授权；也不把“没有明确提及 AI”直接解释为禁止。

这些模型、动作、参考视频和生成舞蹈缓存均不在仓库内。默认构建使用立绘替身，原片权限问题仍独立保留。发布原舞者版本前应核清相关条款；无需把第三方模型或动作下载到本仓库才能构建。

## 软件和字体

- dsh 前端及所用 client-ui 样式：DeepSeek，MIT；保留包版本、LICENSE 和来源说明。
- 前端 bundle 内 React / JSX runtime / React DOM / scheduler：保留原标头，附 `LICENSES/React-MIT.txt`。
- Space Mono 与 Anton：随字体保留 OFL；Windows 系统字体不分发。
- 品牌名称和商标不因代码、美术许可而授予额外权利。
