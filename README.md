# 稀疏体素卷积的活动域扩张与标签监督

本项目面向扫描覆盖与标注资格决定真实零/未知及冲突监督所涉及的数值资料。合成资料用于核对输入身份、数组布局及互操作语义，不代表实际设备或观测结论。

使用 Python 3.11，数值依赖版本在 requirements.txt 固定。可在独立虚拟环境安装后读取资料：

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python inspect_data.py
.venv/bin/python -m unittest discover -s tests -v
```

`inspect_data.py` 读取数据并显示数组形状、数值类型和对象名；它只检查资料，不执行数值产品。`tests` 检查合成输入之间的真实引用、形状和关键身份关系，不代表对应算子、训练或交付行为已经运行通过。

`data/small.json` 的 `objects` 保存领域对象，`tensors` 按名称保存嵌套实数数组；字段与原始数值是输入，没有预计算输出。`data/workload.json` 保存容量形状、种子及工作区范围，容量数字本身不表示数值实现已经提供。`docs/data-contract.md` 说明坐标、身份、数值含义和兼容范围。数值接口由产品实现提供，资料检查入口不承担训练或推理。

项目不需要网络数据或真实账户。更换输入时保持数据契约，数组引用和稳定身份应一同更新。若在已预装依赖的 Python 环境中工作，可以直接使用该解释器运行资料检查与测试，无需重复安装。
