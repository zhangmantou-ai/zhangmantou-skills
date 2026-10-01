# 馒头 Excalicord 白板创作助手

版本：0.1.0 · 作者：斑马zhang · [所属仓库](https://github.com/zhangmantou-ai/zhangmantou-skills)

从素材或灵感出发，逐步确认方向、制作可编辑白板、确认口播稿，最后直接填入 Excalicord 提词器。

**创作者决定内容和表达，AI 负责整理与制作。** 编辑与录制都在 [Excalicord](https://excalicord.com/) 网页完成。

## 使用前提

- 一个支持读取 Skill 指令的 AI 助手。
- 文件生成能力。附带脚本使用 Python 3 标准库，无额外 Python 包。
- 自动导入和填入提词器需要助手具备浏览器操作能力，并获得相应访问权限。没有该能力仍可生成文件，但最后的网页操作需要人工完成。
- 不需要另装本地大模型或部署服务器。所用 AI 助手及 Excalicord 网页自身的联网要求依然存在；本项目不承诺完全离线运行。

## 安装到 Codex

从 [Skill 集合仓库](https://github.com/zhangmantou-ai/zhangmantou-skills) 点击 Code → Download ZIP 并解压。只复制其中的 `mantou-excalicord-creator` 子文件夹，放入：

```text
~/.codex/skills/mantou-excalicord-creator/
```

如设置了 `CODEX_HOME`，使用其 `skills/` 子目录。安装目录里应直接看到 `SKILL.md`，不要多嵌套同名文件夹。下一轮对话即可调用；若客户端尚未发现，重新打开会话。输入：

> 使用 $mantou-excalicord-creator，把这段素材做成适合白板口播的内容。先和我确定方向，再制作。我的素材是……

其他助手按其 Skill 安装方式加载 `SKILL.md` 及关联文件；不同宿主的工具能力与安装兼容性需要自行确认。

也可以直接对支持 skill-installer 的 Codex 说：

> 请安装 https://github.com/zhangmantou-ai/zhangmantou-skills/tree/main/mantou-excalicord-creator 这个 Skill。

已安装时，请先备份自己的修改，再更新。

## 创作流程

1. 确认主题、受众和观点。
2. 逐步确认文字/图文/图解、信息密度、风格、比例、时长和人像位置。
3. 确认分页提纲，再制作白板。
4. 在 Excalicord 导入、修改并确认白板。
5. 根据最终白板写逐页口播稿，交给创作者确认。
6. **口播稿确认后，直接填入 Excalicord 可编辑提词器，检查完整性。**

已有信息不重复询问；内容放不下就拆页，页数随内容决定。可以使用 3:4、16:9 等比例。白板交付为 `.excalidraw` 交换文件，但验收标准是它在 Excalicord 中实际能编辑、能分页。

## 试跑生成器

在本目录执行：

```sh
python3 scripts/build_scene.py examples/layout.json --output demo.excalidraw
python3 scripts/build_scene.py --self-test
```

`examples/sample.excalidraw` 为三页通用示例，`examples/narration.md` 是待创作者确认的配套口播示例。在 Excalicord 左上角菜单“打开”导入文件，替换现有画布前先保存原作品。

生成器接受已设计好的元素位置，不是自动布局引擎。AI 需要根据内容设计页面；精确换行和录制取景需在网页检查。

## 文件结构

- `SKILL.md`：核心指令与创作者确认环节。
- `agents/openai.yaml`：Codex 界面元数据。
- `scripts/build_scene.py`：场景生成器与基本自检。
- `references/`：场景格式与网页操作说明。
- `examples/`：可修改的通用示例，无私人截图与本地路径。
- `VALIDATION.md`：本版检查结果与限制。

## 分享和二次创作

本项目采用 MIT License，支持使用、修改和再分发，保留许可证及版权声明。你可以 Fork 仓库修改指令、布局、示例或脚本，也可以直接提交问题与改进建议。

本项目是独立的创作 Skill，不是 Excalicord 官方产品；不包含 Excalicord/Excalidraw 源码、字体或素材库资产。第三方服务、图形素材、品牌及用户内容的权利不由本许可证授予。

录制不自动启动。没有实际完成短试录与视频导出检查，就不宣称录制通过。

## 常见问题

**为什么文件叫 .excalidraw？** 它是白板交换格式，编辑和录制的入口仍是 Excalicord。以网页实际可编辑、可切页为准。

**只有一句灵感可以开始吗？** 可以。Skill 先协助确定观点和表达方向，再做分页，不要求填写复杂问卷。

**没有浏览器操作工具怎么办？** 可以生成文件和稿件，但需要手动导入白板、粘贴稿件；助手必须明确说明网页步骤未自动完成。

**没有 Python 怎么办？** 可以先做策划与口播稿；附带生成器需要 Python 3。助手有其他文件生成能力时可以替代，但仍须满足原生可编辑元素、分页和网页检查要求。

**稿件会直接填入吗？** 必须先由创作者确认最终稿，之后再填入可编辑提词器。不会自动开始录制或发布。

## 反馈与二次创作

欢迎在[仓库 Issues](https://github.com/zhangmantou-ai/zhangmantou-skills/issues) 提交问题，说明助手环境、浏览器、复现步骤及预期结果。截图和示例须去除私人信息。

可以 Fork 后修改指令、脚本和示例。提交 PR 时请说明修改目的、验证结果，以及是否改变创作者确认环节。不要提交凭据、私人素材或未获授权的人像截图。

## 项目状态

这是基于真实制作流程整理的首个公开版本，不保证所有 AI 宿主与浏览器均已适配。已完成和未完成的检查见 [VALIDATION.md](VALIDATION.md)。
