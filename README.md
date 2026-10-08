# 表面打磨智能分析工具

一个面向机电制造方向的研究型项目，聚焦于基于机器视觉和数据分析的表面打磨质量评估与参数优化。

## 项目目标

- 自动识别打磨表面的缺陷
- 量化表面质量指标
- 建立“工艺参数 - 表面质量”的关系
- 为研究论文或毕设提供可演示的原型系统

## 技术路线

1. 生成模拟打磨表面数据
2. 进行图像预处理
3. 提取纹理与表面特征
4. 建立缺陷检测和质量评估模型
5. 推导打磨参数优化建议

## 目录结构

```text
surface-polishing-research/
├── README.md
├── requirements.txt
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── data_generation.py
│   ├── preprocessing.py
│   ├── feature_extraction.py
│   ├── defect_detection.py
│   ├── quality_assessment.py
│   └── parameter_optimization.py
├── data/
│   ├── raw/
│   ├── processed/
│   └── synthetic/
├── models/
├── notebooks/
├── reports/
└── tests/
```

## 安装依赖

```bash
pip install -r requirements.txt
```

## 使用方式

### 1. 生成合成数据

```bash
python src/data_generation.py
```

### 2. 运行缺陷检测示例

```bash
python src/defect_detection.py --input data/synthetic/surface_001.png
```

### 3. 质量评估

```bash
python src/quality_assessment.py --input data/synthetic/surface_001.png
```

### 4. 参数优化建议

```bash
python src/parameter_optimization.py --target-quality 8.5
```

## 研究价值

- 适用于机电制造、材料加工、质量控制等方向
- 无真实数据时可先使用模拟数据构建原型
- 具备论文写作、实验设计和演示展示的基础

## 说明

这是一个“可运行的研究原型”，旨在帮助你快速搭建一个可演示的表面打磨研究项目，后续可以进一步替换为真实采集数据和更高级的深度学习模型。
