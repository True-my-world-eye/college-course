import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# 读取训练集和测试集
train_path = "Lab8/data/ai_generated_train.parquet"
test_path = "Lab8/data/ai_generated_test.parquet"

# 读取训练数据：text（文章）、generated（标签：0.0/1.0）
train_df = pd.read_parquet(train_path)
print("训练集大小：", train_df.shape)

# 读取测试数据：只有 text
test_df = pd.read_parquet(test_path)
print("测试集大小：", test_df.shape)


# TF-IDF 文本特征提取
# 初始化 TF-IDF 向量器：过滤停用词，只保留重要词汇
tfidf = TfidfVectorizer(stop_words="english", max_features=5000)

# 训练集特征
X_train = tfidf.fit_transform(train_df["text"])
y_train = train_df["generated"]

# 测试集特征
X_test = tfidf.transform(test_df["text"])


# 训练模型：逻辑回归（文本分类很稳）
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)


# 预测测试集
y_pred = model.predict(X_test)


# 保存结果 pred.txt
with open("Lab8/output/pred.txt", "w") as f:
    for val in y_pred:
        f.write(f"{val:.1f}\n")

print("✅ 已生成 pred.txt")
print("预测结果统计：")
print("0.0 数量：", (y_pred == 0.0).sum())
print("1.0 数量：", (y_pred == 1.0).sum())