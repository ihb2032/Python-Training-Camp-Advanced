# Python训练营进阶部分

本项目包含一系列Python深度学习算法和计算机视觉实现的练习。你需要补全 `exercises` 目录下的 Python 文件中缺失的代码，并通过测试来验证实现的正确性。

## 练习内容

### 第1部分: 深度学习算法基础
1.  `exercises/iou.py`: 实现目标检测中的交并比 (IoU) 计算。
2.  `exercises/nms.py`: 实现目标检测中的非极大值抑制 (NMS) 算法 (包含 IoU 计算)。
3.  `exercises/conv.py`: 手写实现二维卷积操作。
4.  `exercises/leaky_relu.py`: 实现 LeakyReLU 激活函数。
5.  `exercises/maxpool.py`: 实现最大池化操作。
6.  `exercises/cross_entropy.py`: 实现交叉熵损失函数。
7.  `exercises/smooth_l1.py`: 实现 Smooth L1 损失函数。

### 第2部分: 计算机视觉基础
8.  `exercises/image_processing.py`: 使用 OpenCV 实现图像边缘检测等基本处理。
9.  `exercises/contour_detection.py`: 使用 OpenCV 实现图像轮廓检测。

## 使用方法

1.  **Fork 本仓库**: 将此仓库 Fork 到你自己的 GitHub 账户。
2.  **克隆仓库**: 将你 Fork 的仓库克隆到本地计算机：
    ```bash
    git clone https://github.com/YOUR_USERNAME/Python-Training-Camp-Advanced.git
    cd Python-Training-Camp-Advanced
    ```
    (将 `YOUR_USERNAME` 替换为你的 GitHub 用户名)
3.  **设置环境**: 参考下方的 "环境要求" 和 "运行方法" 安装必要的依赖。
4.  **完成练习**: 
    *   打开 `exercises/` 目录中的练习文件。
    *   仔细阅读文件顶部的说明和代码中的注释。
    *   在标记为 `# TODO:` 或包含 `pass` 的地方编写代码。
5.  **本地测试**: 使用 "运行方法" 中的命令在本地测试代码。
6.  **提交与评分**: 
    *   将修改后的代码 `git add`, `git commit`, 并 `git push` 到你 Fork 的仓库。
    *   推送代码后，GitHub Actions 会自动运行测试并计算分数。
    *   访问你 Fork 仓库的 "Actions" 页面查看结果。
    *   (若 Actions 未自动运行，请手动启用或触发)
    *   在 Actions 日志中查找 "Print test results score" 步骤查看分数，并在 "Summary" 页面下载构建产物获取详细报告。

## 建议学习顺序

建议按照练习文件名的隐含顺序或上述列表顺序学习，从基础算法到图像处理应用：
1.  先掌握目标检测的基础算法 (`iou.py`, `nms.py`)。
2.  学习深度学习的核心组件实现 (`conv.py`, `leaky_relu.py`, `maxpool.py`, `cross_entropy.py`, `smooth_l1.py`)。
3.  最后学习 OpenCV 图像处理 (`image_processing.py`, `contour_detection.py`)。

## 环境要求
*   Python 3.10
*   依赖库见 `requirements.txt` (主要包括 `numpy`, `opencv-python`, `pytest`)

## 目录结构

```
Python-Training-Camp-Advanced/
├── .github/workflows/     # GitHub Actions 工作流配置
│   └── test.yml
├── exercises/             # 学员练习目录 (需要填空的 .py 文件)
│   ├── contour_detection.py
│   ├── conv.py
│   ├── cross_entropy.py
│   ├── image_processing.py
│   ├── iou.py
│   ├── leaky_relu.py
│   ├── maxpool.py
│   ├── nms.py
│   └── smooth_l1.py
├── picture/               # 可能包含测试用的图片资源
├── tests/                 # Pytest 测试文件
│   ├── test_contour_detection.py
│   ├── test_conv.py
│   ├── # ... (其他测试文件)
│   └── test_smooth_l1.py
├── .gitignore             # Git 忽略文件配置
├── README.md              # 项目说明文件 (本文件)
├── requirements.txt       # Python 依赖库列表
├── score_calculator.py    # 用于计算分数的脚本
└── test_score.txt         # 分数计算结果（示例或运行时生成）
```

## 运行方法

1.  **安装依赖**:
    ```bash
    # 建议在虚拟环境中操作
    # python -m venv .venv
    # source .venv/bin/activate  # Linux/macOS
    # .venv\Scripts\activate  # Windows
    pip install -r requirements.txt
    ```
2.  **本地运行测试**:
    ```bash
    # 运行所有测试
    python -m pytest tests/ -v

    # 运行特定测试文件 (例如 iou.py)
    python -m pytest tests/test_iou.py -v
    ```
3.  **自动测试与评分 (GitHub Actions)**:
    *   将您的代码 `git push` 到您 Fork 的 GitHub 仓库。
    *   稍等片刻，进入 GitHub 仓库页面，点击 "Actions" 标签。
    *   找到最新的工作流运行实例，点击进入查看详情（若未触发自动测试，可能是因为一开始未启动Actions功能，手动启动测试即可）。
    *   您可以查看测试日志、`pytest` 的输出以及 `score_calculator.py` 生成的分数报告 (`test_score.txt` 会作为 artifact 上传)。

## 注意事项
- 每个练习文件中都有详细的注释说明和提示，请仔细阅读。
- 需要填写的代码部分主要是完成带有 `pass` 语句的函数体。

## 评分标准

当您推送代码后，GitHub Actions 会自动执行以下流程：
1.  运行 `pytest` 对您在 `exercises/` 目录下的代码进行测试。
2.  即使部分测试失败，流程也会继续 (`continue-on-error: true`)。
3.  运行 `score_calculator.py` 脚本，该脚本可能会根据 `pytest` 的测试结果（例如解析生成的 `test-results.xml` 文件）来计算一个分数。
4.  最终的分数会保存在 `test_score.txt` 文件中。
5.  您可以在 GitHub Actions 的运行日志中看到分数报告的打印输出。
6.  `test_score.txt` 和 `test-results.xml` 文件会作为构建产物 (Artifacts) 上传，您可以在 Actions 运行详情页面下载它们以查看详细结果。

最终评价基于 `score_calculator.py` 计算出的分数。 