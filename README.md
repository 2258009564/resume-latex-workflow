# Resume LaTeX Workflow

一个中文简历制作 skill：**分轮提问 → Markdown 大纲 → LaTeX/PDF → 岗位研究与润色 → 批注迭代**。适合从零制作简历，也支持已有简历的改写。默认单页宋体风格，常规/粗体层次清楚，宝蓝色用于章节与细线；正文可选择、源码可编辑。

## 使用

将本仓库中的 `resume-latex-workflow` 文件夹放到 `~/.codex/skills/`，随后在支持 skills 的 Codex 会话中调用：

```text
使用 $resume-latex-workflow，帮我做一份分布式存储研发实习简历。
先分轮问我问题，再生成 Markdown 大纲，按模板制作 LaTeX 和 PDF。
结合我的真实经历研究岗位要求并润色。
```

其他起手方式：

```text
使用 $resume-latex-workflow，按我已有简历直接生成，缺失项标待补充。
使用 $resume-latex-workflow，按这些 PDF 批注修改现有 resume.tex。
使用 $resume-latex-workflow，参考这份简历加强项目职责、句内重点和技能串联，不复制对方指标。
使用 $resume-latex-workflow，按我指定的能力写目标简历用于后续补全，正文不加待学习标签，完成状态留在说明。
```

安装后若当前客户端未刷新技能列表，可在新会话调用。其他支持文件型 skills 的工具可以读取 `SKILL.md`，但工具名称、编辑器和编译能力需由其环境提供。

## 工作流

1. **访谈**：按基本信息、个人介绍、教育、工作/实习、项目/校园、技能/证书分轮收集，每轮最多五问。已知信息不重复问，不清楚的内容最多追问两轮。
2. **大纲**：目标岗位用一级标题，模块用二级标题，每个字段单独列表项；默认不超过500字。完整正文单独保存，避免大纲字数限制挤掉项目证据。
3. **制作**：按随附模板生成 `resume.tex` 和 PDF，姓名与联系信息分组，照片在右，项目名称/语言突出，项目链接放标题后方偏左、起止年月在最右；强竞赛背景默认荣誉在项目前，赛事名称在左、奖项与级别在右；项目角色依授权靠右显示，模块顺序可按批注调整。
4. **研究润色**：按目标岗位和候选人资历查找招聘要求，优先官方来源，突出“做了什么、怎么做、结果如何”。不把职位要求或别人的成果写成候选人的经历。
5. **内容模式**：事实投递稿按已有经历写；明确的目标稿可以按用户授权的能力写成完整职责，完成状态留在说明。用户不要学习清单/标签时不强加，任何模式都不编造数字、测试结果和荣誉。
6. **检查和修改**：先查事实与内容一致性，再编译和查看实际渲染；按PDF批注修改同一源码。用户说“直接生成”时不再继续访谈。

竞赛名称会按年份、地区和赛项主动查证，向用户反馈原名、建议名称与来源，再修改确定项；赛事身份或组别有歧义时保留原文并询问，不静默替换为相似比赛。奖项条目末尾不加句号。

基本信息、教育、荣誉、项目、技能按候选人材料组织，不用虚构模块凑数量；用户明确不要个人介绍时不添加。无经历不虚构，未知项依用户选择省略或占位。照片、预留第二项目空间、奖项级别和技能熟练度均以用户资料为准。

## 参考改写与视觉重点

先查看参考 PDF，再分别借鉴架构描述、职责深度、句内强调与技能合并，不只换排版。每条职责突出少数关键机制，渲染后检查粗细差和小字清晰度；同色样采样避免反复猜蓝色。完整规则见 [参考改写规范](resume-latex-workflow/references/reference-adaptation.md) 与 [版式规范](resume-latex-workflow/references/layout.md)。

## 模板与运行环境

模板：[resume-template.tex](resume-latex-workflow/assets/resume-template.tex)。[空白模板 PDF](docs/template-preview.pdf)只演示版式，字段均为待补充。

![模板预览](docs/template-preview.png)

已有原生 LaTeX 编辑器/编译工具时优先使用。否则本地需要 XeLaTeX，以及模板使用的标准宏包（fontspec、xeCJK、geometry、xcolor、graphicx、titlesec、enumitem、hyperref）。中文优先宋体，强调保持宋体风格；SimSun 无原生粗体时采用受控字重扩展并实际看图，缺失时采用 Noto Serif CJK/FandolSong。英文优先 Times New Roman，缺失时采用 TeX Gyre。没有编译器时保留源码并报告 PDF 未生成，不自动安装 TeX。

```sh
xelatex -interaction=nonstopmode -halt-on-error resume.tex
```

可选预览检查脚本需要 Python 3 和 PyMuPDF。它报告字体是否嵌入、可选择文字、页面外文字及链接，并生成约216dpi预览：

```sh
python resume-latex-workflow/scripts/inspect_pdf.py resume.pdf --output preview
```

自动检查不能替代事实核对或逐页视觉检查。网页研究需要可用浏览工具；浏览不可用时保留现有事实，明确说明研究未完成，不能编造来源。

## 文件结构

```text
resume-latex-workflow/
  SKILL.md
  agents/openai.yaml
  assets/resume-template.tex
  references/layout.md
  references/research-writing.md
  references/reference-adaptation.md
  scripts/inspect_pdf.py
```

使用时产生的 `facts.md`、`resume-content.md`、真实头像和候选人文件应留在个人工作区，不提交到本公共仓库。验证记录见 [审核记录](docs/QUALITY.md)。

版式参数来自实际简历迭代，曾参考 [Auto-CV](https://github.com/flamingoTOM/Auto-CV) 的组织方式；随附模板用标准 article 独立实现，不需要第三方 resume.cls。代码与说明采用 MIT License。第三方工具、字体的许可由各自提供方决定。
