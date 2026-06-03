# Python 与数据科学

浙江工商大学 计算机科学与技术学院 — 大二下学期实验课程

**2025–2026 学年**

---

## 仓库结构

```
├── Lab1/   Python 入门练习
├── Lab2/   Python 基础语法实践
├── Lab3/   文件操作与数据读取
├── Lab4/   模块与面向对象编程
├── Lab5/   Python 科学计算实践
├── Lab6/   数据挖掘入门分类
├── Lab7/   蛋白质功能预测
├── Lab8/   文本分类预测
├── Lab9/   水果图像识别
├── Lab10/  正则表达式与网络爬虫
├── 课件/    课程幻灯片及 Jupyter Notebook
├── 期末/    期末大作业报告模板
└── study.md  Python 模块速查手册
```

每个 Lab 统一结构：

```
LabN/
├── code/           ← 源代码（.py）
├── data/           ← 实验数据文件
├── 实验要求.docx    ← 实验指导书
└── README.md       ← 知识点讲解（初学者视角）
```

## 使用说明

所有代码从仓库根目录运行：

```bash
python Lab1/code/1_5.py
python Lab6/code/Lab6.py
```

> ⚠️ 注意：Lab6 的训练数据（~1GB）和 Lab8 的文本数据（~50MB）未上传至 GitHub，运行前需从原始压缩包解压或向课程教师索取。

## 分支说明

| 分支 | 内容 |
|------|------|
| `python与数据分析` | 本课程全部实验代码与文档 |

其他课程的实验代码将以不同分支存放于本仓库。

## 模块速查

参见根目录 `study.md`，涵盖 os、random、time、datetime、csv、zipfile、hashlib、numpy、scipy、pandas、matplotlib 等常用模块的函数速查与代码示例。

