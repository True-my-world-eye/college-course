# Lab7 蛋白质功能预测实验 — 知识文档

## 1. 实验目标概览
- 学会从生物序列数据中**手工设计特征**
- 理解氨基酸组分、二肽组分、k-space 特征
- 使用 XGBoost 进行分类

---

## 2. 核心知识点

### 2.1 数据理解

蛋白质由**氨基酸**组成，共有 20 种标准氨基酸（用字母 A~Y 表示）：

```python
AA20 = ['A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I',
        'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V']
```

训练数据文件每行格式：`序列ID 氨基酸序列 标签(0或1)`

```
P06787 MSSNLTEEQ... 1
```

任务是：给定一条蛋白质的氨基酸序列，预测它是否具有某种生物功能。

### 2.2 特征工程（核心！）

原始数据是**字符串**（如 "MSSNLTEEQ..."），不能直接给模型用，需要转成**固定长度的数值向量**。

#### (a) 氨基酸组分（20维 + 1维）

统计每种氨基酸在序列中出现的**比例**：

```python
from collections import Counter

def get_aa_composition(seq):
    cnt = Counter(seq)
    total = len(seq)
    feat = []
    for aa in AA20 + ['X']:   # X 代表非标准氨基酸
        feat.append(cnt.get(aa, 0) / total)
    return np.array(feat)
```

#### (b) 二肽组分（441维）

连续的两个氨基酸称为二肽，如 `"MS"`, `"SS"`, `"SN"`... 统计每种二肽的比例。

```python
def get_dipeptide(seq):
    dipeps = [seq[i:i+2] for i in range(len(seq)-1)]
    cnt = Counter(dipeps)
    total = len(dipeps)
    feat = []
    for a in AA20 + ['X']:
        for b in AA20 + ['X']:
            feat.append(cnt.get(a+b, 0) / total)
    return np.array(feat)
```

21 × 21 = 441 维。

#### (c) k-space 氨基酸组分

每隔 k 个位置取一个氨基酸，再计算组分：

```python
def get_kspace(seq, k=2):
    feat = []
    for i in range(k):
        sub = seq[i::k]           # 每隔 k 位取一个
        feat.extend(get_aa_composition(sub))
    return np.array(feat)
```

例如 k=2 时：取 `seq[0::2]`（奇数位）和 `seq[1::2]`（偶数位），各算一次组分。

### 2.3 XGBoost

XGBoost 是梯度提升树的一种高效实现，在表格数据上表现优异。

```python
from xgboost import XGBClassifier

model = XGBClassifier(
    n_estimators=200,        # 树的数量
    max_depth=6,             # 每棵树的深度
    learning_rate=0.1,       # 学习率
    subsample=0.8,           # 每棵树用80%的样本
    colsample_bytree=0.8,    # 每棵树用80%的特征
    random_state=42
)
```

### 2.4 评价指标：F1 Score

```python
from sklearn.metrics import f1_score
f1 = f1_score(y_true, y_pred)
```

F1 = 2 × (精确率 × 召回率) / (精确率 + 召回率)，综合衡量模型性能。

---

## 3. 初学者常见问题

- **特征维度爆炸**：氨基酸组分(21) + 二肽(441) + k-space(42) = 504 维，每增加一种特征维度就暴增
- **数据规模**：2000条训练，200条测试，每条序列长度几十到几百不等
- **非标准氨基酸**：如果序列中出现 AA20 以外的字符，统一替换为 'X'
- **路径问题**：代码中用 `Lab7/data/ProSeqs_Train.txt` 读取数据
