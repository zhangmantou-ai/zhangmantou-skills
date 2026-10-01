# 文件制作与检查

## 为什么使用 .excalidraw

这是可编辑场景的交换格式；使用入口仍然是 Excalicord。2026-10-01 的实际网页检查中，含六个原生 `frame` 的文件被识别为六张幻灯片，点击页码能切换，标题可原生编辑。网页将来可能变化，导入后仍须现场确认。

`group` 不是原生元素类型；相关元素共享 `groupIds`。各页的元素通过 `frameId` 指向本页画框。生成器为不同页分组加命名空间，避免跨页意外编组。

## 布局 JSON

```json
{
  "title": "示例",
  "width": 1080,
  "height": 1440,
  "background": "#fffdf8",
  "pages": [{
    "title": "01 一页一个重点",
    "elements": [
      {"type":"text","x":72,"y":120,"text":"一个重点","fontSize":60},
      {"type":"rectangle","x":72,"y":300,"width":400,"height":160,"fill":"#edf3fc","group":"idea"},
      {"type":"text","x":100,"y":345,"text":"可编辑图形","fontSize":36,"group":"idea"},
      {"type":"arrow","x":280,"y":490,"points":[[0,0],[0,140]]}
    ]
  }]
}
```

支持 `text`、`rectangle`、`ellipse`、`diamond`、`line`、`arrow`。颜色用 `color` 和 `fill`，分组用 `group`；箭头用相对 `points`。字号、坐标由创作者确认后的布局决定。输入内容必须是可信的布局数据，不是可执行代码。

文字支持显式换行。默认宽度采用保守字符估计；`text.width` 可覆盖估计，但必须实际检查，不能仅靠加宽或缩小通过校验。生成器不提供精确字体测量或自动布局。不同系统字体会改变换行，网页视觉检查必不可少。

```sh
python3 scripts/build_scene.py examples/layout.json --output sample.excalidraw
python3 scripts/build_scene.py --self-test
```

无第三方 Python 依赖。输出 2 版场景 JSON，所有页横向排列，每页含背景矩形和原生画框。背景设为锁定，避免误移动；内容保持可编辑。

## 检查重点

- 画框数量等于页数；全部采用确认的比例；原生元素 ID 唯一，frame 引用有效。
- 文本、形状以及线条所有端点都在本页内；长文字显式换行或重新布局。
- 页面标题、正文、箭头关系清晰；人像区不盖住文字。
- 导入后核对文字实际尺寸及换行，而不是仅看 JSON 边界校验。
- 该工具不生成 `.excalicord` 私有项目格式，也不保证其他 Excalicord 分支版本自动识别分页。

使用外部素材库时，仅引入许可允许的素材并记录来源。当前示例完全使用原生基础图形，没有第三方素材。
