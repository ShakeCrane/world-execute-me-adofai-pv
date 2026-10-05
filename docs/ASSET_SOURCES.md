# 素材授权来源与核实范围

核实日期：2026-09-30。本页记录事实和证据边界，不替代各许可全文。

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
