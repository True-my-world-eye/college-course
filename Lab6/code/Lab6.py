import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

# 读取训练集与测试集
train = pd.read_csv("Lab6/data/data-train.csv")
test = pd.read_csv("Lab6/data/data-test.csv")

# 分离特征 X 和标签 y
X_train = train.drop("target", axis=1)
y_train = train["target"]
X_test = test

# 特征标准化
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 训练模型
model = RandomForestClassifier(n_estimators=50, random_state=42 , n_jobs=-1)
model.fit(X_train_scaled, y_train)

# 预测测试集
y_pred = model.predict(X_test_scaled)

# 保存结果
np.savetxt("Lab6/output/predictions.txt", y_pred, fmt="%d")

print("✅ 预测完成！已生成 predictions.txt（共160行）")
print("前10个预测结果：", y_pred[:10])
print("预测中0的数量：", (y_pred == 0).sum())
print("预测中1的数量：", (y_pred == 1).sum())