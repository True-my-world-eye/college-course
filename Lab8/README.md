# Lab8 文本分类预测实验 — 知识文档

## 1. 实验目标概览
- 学会用 TF-IDF 将文本转为数值特征
- 用逻辑回归进行文本分类
- 处理 Parquet 格式数据
- 区分 AI 生成文本 vs 人类撰写文本

---

## 2. 核心知识点

### 2.1 Parquet 文件格式

Parquet 是一种高效的列式存储格式，比 CSV 更节省空间和读取更快。

```python
import pandas as pd
df = pd.read_parquet("Lab8/data/ai_generated_train.parquet")
```

### 2.2 TF-IDF 文本向量化

计算机无法直接理解"文字"，需要把文本转成数字向量。

**TF-IDF = 词频 × 逆文档频率**

- **词频（TF）**：某个词在文章中出现的次数
- **逆文档频率（IDF）**：包含了该词的文章数的倒数。常见词的 IDF 小（如"的"、"是"），稀有词的 IDF 大

```python
from sklearn.feature_extraction.text import TfidfVectorizer

tfidf = TfidfVectorizer(
    stop_words="english",   # 过滤英文停用词（the, a, an...）
    max_features=5000       # 只保留最重要的5000个词
)

# 训练集：拟合 + 转换
X_train = tfidf.fit_transform(train_df["text"])

# 测试集：只用转换（用训练集学到的词汇表）
X_test = tfidf.transform(test_df["text"])
```

**为什么测试集用 `transform` 而不是 `fit_transform`？** 和标准化一样，测试集不能"偷看"训练集的词汇表。

### 2.3 逻辑回归

虽然名字叫"回归"，但实际上是一个**分类**模型。

```python
from sklearn.linear_model import LogisticRegression

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
```

逻辑回归的本质：计算每个类别概率，取概率最大的类别。

### 2.4 评价指标：准确率

准确率 = 预测正确的样本数 / 总样本数

```python
from sklearn.metrics import accuracy_score
acc = accuracy_score(y_true, y_pred)
```

### 2.5 数据不平衡问题

如果训练集中 0 和 1 的比例不均衡（比如 90% 是 0），直接训练可能模型会"偷懒"——全都预测为 0。

解决思路：
- 使用 `class_weight='balanced'` 参数
- 对多数类降采样，少数类过采样
- 使用适合不平衡数据的评价指标

---

## 3. 初学者常见问题

- **TF-IDF 矩阵巨大**：5000 个特征 × 30000 篇文章 → 稀疏矩阵（大部分元素为 0）
- **`fit_transform` vs `transform`**：词汇表只能从训练集学习，测试集直接用
- **测试集不含标签**：这是正常的，测试集就是让你预测的
- **结果格式**：每行一个 `0.0` 或 `1.0`，共 20000 行
