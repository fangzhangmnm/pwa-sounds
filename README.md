# PWA Sounds —— 家族音源库（跟人走的声音素材，不是 AI 模型）

> created 2026-10-07 by Claude Fable 5.1（user 2026-10-07：「音源不是ai」；2026-08-19：「音源库跟人不跟 app……说不定我会回去 fl studio，这个库跟的是我」）

放**录下来的声音素材**：乐器音色库（sf2 / sfz、鼓组）、音效素材（混响的脉冲响应、SFX、打击采样）。**普通文件 + 一份目录**，人和别的软件（FL Studio、MuseScore、任何 SoundFont 播放器）能直接用；家族 app 把它当货架，歌用到什么就 by value 拷进歌里。
AI 模型和推理运行时不在这里（它们在 `pwa-models`）；效果器算法是代码、随 app 发；私人录音在自己的 OneDrive / 本机。

## 布局

```
index.json                 # 目录：id / kind / name / file / format / bytes / sha256 / license{name,summary,file,sha256} / attribution / homepage / source / date / notes
<id>/<文件>                # 素材本体，原样（不切片、不改名）
<id>/LICENSE.txt           # 入库当时的许可证快照
tools/index.py             # 核对 / 补全目录里的字节事实（--write）
```

- `kind` 开放词表，现有：`instrument`（乐器音色库）/ `drumkit`（单独的鼓组）/ `ir`（卷积混响的脉冲响应）/ `sfx`（一次性音效）。
- `id` = `<名字>-<版本或日期>`；**一个 id 的字节永远不变**，新版本 = 新 id（app 和歌钉的是 sha256；这里只是运输）。
- **进库前许可证由仓主逐条核**（可再分发 + 署名义务写进 `attribution`）；`license.summary` 是给人看的摘要，原文看 `LICENSE.txt`。
- app 侧：出厂预填这个站的地址、设置里能改（反弃坑）；拿到文件先对 `index.json` 里钉的 sha256 再用；浏览只解析预设表、试听 / 选中时才子集化；**歌里带的是子集，不依赖这个站**。
- 托管：GitHub Pages（本仓 main 根目录直出，`.nojekyll`）；任何能放静态文件的地方都能镜像，把文件夹拷走即可。

## 现有素材

| id | kind | 内容 | 许可 | 出处 |
|---|---|---|---|---|
| `generaluser-gs-2.0.3` | instrument | GeneralUser GS 2.0.3，GM / GS 通用音色库，287 件含 13 套鼓组，32.3 MB | GeneralUser GS License v2.0（可商用、可进软件、可改包装；别直链作者下载） | https://github.com/mrbumpy409/GeneralUser-GS · https://www.schristiancollins.com/generaluser.php |
