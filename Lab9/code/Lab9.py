from pathlib import Path
import numpy as np
import pandas as pd
from PIL import Image
from sklearn.svm import SVC
from sklearn.preprocessing import LabelEncoder
from sklearn.decomposition import PCA
import joblib

# 配置
TRAIN_DIR = Path("Lab9/train")
TEST_DIR = Path("Lab9/test")
IMAGE_SIZE = 48
MAX_IMAGES = None  # 读取全部

# 读取图像函数
def list_image_paths(image_dir: Path, is_train=True):
    items = []
    if is_train:
        # 训练集：按子文件夹（类别）读取
        for class_dir in sorted([p for p in image_dir.iterdir() if p.is_dir()]):
            label = class_dir.name
            for img_path in sorted([p for p in class_dir.iterdir() if p.is_file()]):
                if img_path.suffix.lower() in {".webp", ".jpg", ".png"}:
                    items.append((label, img_path))
    else:
        # 测试集：直接读取所有文件，按文件名排序
        for img_path in sorted([p for p in image_dir.iterdir() if p.is_file()]):
            if img_path.suffix.lower() in {".webp", ".jpg", ".png"}:
                items.append((None, img_path))
    if MAX_IMAGES is not None:
        items = items[:MAX_IMAGES]
    return items

def load_image_as_array(img_path: Path):
    img = Image.open(img_path).convert("RGB")
    img = img.resize((IMAGE_SIZE, IMAGE_SIZE))
    return np.asarray(img, dtype=np.float32).reshape(-1) / 255.0  # 归一化

# 加载训练集
print("正在加载训练集...")
train_items = list_image_paths(TRAIN_DIR, is_train=True)
X_train, y_train = [], []
for label, path in train_items:
    X_train.append(load_image_as_array(path))
    y_train.append(label)
X_train = np.array(X_train)
print(f"训练集形状：{X_train.shape}")

# 标签编码
le = LabelEncoder()
y_train_enc = le.fit_transform(y_train)

# 特征降维（PCA，提高速度+降噪）
print("正在PCA降维...")
pca = PCA(n_components=256, random_state=42)
X_train_pca = pca.fit_transform(X_train)

# 训练SVM模型（高准确率）
print("正在训练SVM...")
model = SVC(kernel="rbf", C=10, gamma="scale", random_state=42)
model.fit(X_train_pca, y_train_enc)

# 保存模型与预处理器
joblib.dump(model, "Lab9/svm_model.pkl")
joblib.dump(le, "Lab9/label_encoder.pkl")
joblib.dump(pca, "Lab9/pca.pkl")
print("模型保存完成")

# 加载测试集并预测
print("正在加载测试集并预测...")
test_items = list_image_paths(TEST_DIR, is_train=False)
X_test = []
for _, path in test_items:
    X_test.append(load_image_as_array(path))
X_test = np.array(X_test)
X_test_pca = pca.transform(X_test)

# 预测
y_pred_enc = model.predict(X_test_pca)
y_pred = le.inverse_transform(y_pred_enc)

# 输出 preds.txt
with open("Lab9/output/preds.txt", "w", encoding="utf-8") as f:
    for label in y_pred:
        f.write(label + "\n")
print("已生成 preds.txt，共", len(y_pred), "行")