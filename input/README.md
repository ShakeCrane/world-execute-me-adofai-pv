# input/：你自己准备的东西

歌曲和歌词受版权保护，不在本仓库里。构建前，把它们放到这个文件夹。

## song.mp3（必需）

Mili 的《world.execute(me);》完整音频。

这支片子按下面这个文件逐帧对齐，时间零点就是它解码出来的第一个采样。`data/song.json` 里有同样的数字：

| 项目 | 值 |
|---|---|
| sha256 | `79c4e53663c7966b7160bff19326e614658485d4ce0199ff82715ea9d0a418fc` |
| 时长 | 211.913 s |
| 格式 | MP3，320 kbps，44.1 kHz，立体声 |

- 你的文件和这个不一样也能出片，`python build.py check` 会提示。
- 片头如果多出或少掉一段静音，唱词和镜头会整体提前或推后。可以用 ffmpeg 裁掉或补上静音，让两份的起唱点对齐。

### 本机 DELTARUNE 技术验证用音源

当前本机 `song.mp3` 是已对齐的替代版本，不是上表的母带。来源为公开第三方项目 [world.execute-me-ascii 的 v1.0.0 release](https://github.com/yym8224961/world.execute-me-ascii/releases/tag/v1.0.0)，读取校验通过的 `world-execute-mv.pyz` ZIP 内 `media/song.mp3`，未执行该包代码；此来源不是 Mili 官方发行渠道。

- 原候选 SHA-256：`2da5fb306fc83b178617da9283b94e65933ae0c9c99d40b0b91be5266ed21a40`。
- 本机处理后 SHA-256：`50809b79b6226d41cc5364ad5bf7687fa0c8c0b7a2d3740cbcce048f8b946a09`；解码时长 211.913016 s，320 kbps、44.1 kHz、立体声。
- 处理：裁去开头 124 ms，重新置零时间戳，尾部补静音并限制到 211.913 s。FFmpeg 滤镜为 `atrim=start=0.124,asetpts=PTS-STARTPTS,apad,atrim=duration=211.913`，编码 `libmp3lame -b:a 320k -ar 44100 -ac 2`。
- 与既有参考 RMS 包络对比，七个窗口最佳残差均为 +1 ms；封装为 AAC 后仍相同。不是逐词听审，也不能保证声音与原始母带完全相同。原逐词时间本身也是自动对齐草案。
- `data/song.json` 保留原工程的母带指纹；`build.py check` 对当前音源提示版本不同属于预期。歌曲文件仍被 Git 忽略。

## deltarune/（本机游戏素材输入）

已取得可重复获取的游戏截图、角色 PNG 和透明 GIF，保留在本机 `input/deltarune/`。`sources.json` 记录原文件名、获取 URL、大小、帧数与 SHA-256。清单及用途边界见 [素材来源](../docs/ASSET_SOURCES.md)；这些文件不适用项目代码的 MIT 许可，也不随 Git 分发。

## lyrics.lrc（可选）

- 没有这个文件时，`python build.py lyrics` 会从 LRCLIB（https://lrclib.net ，条目 36914646）下载同步歌词，保存到这里。
- 也可以放你自己的 LRC。它要和那个版本一行一行对应；合成时逐行校验，对不上的地方会明确报出来。
- 歌词只用来在你的本机生成两份文件：`film/world_execute_word_timing_20260927/word_timeline.json` 和 `film/ai_mascot_mv_world_execute_20260926/audio/lyrics_synced.lrc`。它们都在 `.gitignore` 里，不会被提交。
