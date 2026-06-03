# Lab6 数据挖掘入门分类实验 — 知识文档

## 1. 实验目标概览
- 理解机器学习分类的基本流程
- 学会用 scikit-learn 构建分类模型
- 掌握特征标准化（StandardScaler）
- 使用随机森林（Random Forest）进行分类

---

## 2. 核心知识点

### 2.1 机器学习分类流程

```
数据加载 → 特征/标签分离 → 特征标准化 → 训练模型 → 预测 → 保存结果
```

### 2.2 数据加载与分离

```python
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

train = pd.read_csv("Lab6/data/data-train.csv")
test = pd.read_csv("Lab6/data/data-test.csv")

# 特征和标签分离
X_train = train.drop("target", axis=1)  # 所有特征列
y_train = train["target"]               # 目标列
X_test = test                            # 测试集没有标签
```

### 2.3 特征标准化

为什么要做？不同特征的数值范围可能差别很大（比如有的特征在 0~1，有的在 0~10000），会影响模型效果。

```python
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)   # 拟合训练集并转换
X_test_scaled = scaler.transform(X_test)          # 用训练集的参数转换测试集
```

**注意：** 测试集用 `transform()` 而不是 `fit_transform()`——测试集不能"偷看"训练集的统计信息。

### 2.4 随机森林

随机森林 = 多棵决策树的集成，每棵树在不同的数据子集和特征子集上训练。

```python
model = RandomForestClassifier(
    n_estimators=50,     # 树的数量（越多越准，但越慢）
    random_state=42,     # 随机种子（保证结果可重复）
    n_jobs=-1            # 用所有CPU核训练
)
model.fit(X_train_scaled, y_train)    # 训练
y_pred = model.predict(X_test_scaled) # 预测
```

### 2.5 保存结果

比赛要求预测结果文件中每行一个 0 或 1：

```python
np.savetxt("Lab6/output/predictions.txt", y_pred, fmt="%d")
```

---

## 3. 初学者常见问题

- **`fit_transform` vs `transform`**：训练集用 `fit_transform`，测试集只用 `transform`
- **测试集不含标签**：这是正常的，因为测试集就是让你预测的
- **结果顺序必须一致**：预测的顺序要和测试数据的行顺序完全相同
- **数据量大**：`data-train.csv` 有 1000+ MB，训练可能需要一些时间
- **`random_state` 的作用**：设置后每次运行结果相同，方便调试

## 4. 拓展思路

除随机森林外，还可以尝试：
- **逻辑回归**（LogisticRegression）
- **XGBoost / LightGBM**
- **支持向量机**（SVC）
- **深度学习**（PyTorch / TensorFlow）
