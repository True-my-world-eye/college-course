# Lab9 水果图像识别实验 — 知识文档

## 1. 实验目标概览
- 学会用 Pillow 读取和处理图像
- 理解图像作为"数据"的本质——图像就是数字矩阵
- 掌握 PCA 降维
- 用 SVM 进行多分类

---

## 2. 核心知识点

### 2.1 图像 = 数字矩阵

一张 48×48 的彩色图片可以看作一个三维数组：

- 形状：(48, 48, 3)
- 48 行、48 列、3 个颜色通道（RGB）
- 每个像素的值范围：0~255

```python
from PIL import Image
import numpy as np

img = Image.open("xxx.webp").convert("RGB")
img = img.resize((48, 48))
arr = np.asarray(img, dtype=np.float32)
# arr.shape = (48, 48, 3)

# 展平为一维向量（48*48*3 = 6912 维）
flat = arr.reshape(-1)  # shape = (6912,)
```

### 2.2 读取目录中的图片

训练集：按类别分目录存放
```
train/
├── apple/     # 所有苹果图片
├── banana/    # 所有香蕉图片
└── ...
```

测试集：所有图片在一个目录下，按文件名编号

```python
from pathlib import Path

def list_image_paths(image_dir, is_train=True):
    items = []
    if is_train:
        for class_dir in sorted(image_dir.iterdir()):
            label = class_dir.name
            for img_path in sorted(class_dir.iterdir()):
                items.append((label, img_path))
    else:
        for img_path in sorted(image_dir.iterdir()):
            items.append((None, img_path))
    return items
```

### 2.3 PCA 降维

一张 48×48 的图片展平后有 6912 维。维度过高会导致：
1. 计算慢
2. 容易过拟合
3. 需要更多数据

**PCA（主成分分析）**：找到数据中最重要的方向，把高维数据投影到低维空间。

```python
from sklearn.decomposition import PCA

pca = PCA(n_components=256)  # 降到256维
X_train_pca = pca.fit_transform(X_train)
X_test_pca = pca.transform(X_test)   # 测试集用训练集的 PCA
```

### 2.4 标签编码

类别名称（如"apple"、"banana"）不能直接输入模型，需要转成数字：

```python
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
y_train_enc = le.fit_transform(y_train)
# "apple" → 0, "banana" → 1, ...

# 预测后还原
y_pred = le.inverse_transform(y_pred_enc)
# 0 → "apple", 1 → "banana", ...
```

### 2.5 SVM 支持向量机

SVM 试图找到一个"超平面"将不同类别的数据分开。

```python
from sklearn.svm import SVC

model = SVC(
    kernel="rbf",       # 核函数（rbf 最常用）
    C=10,               # 正则化强度（越大越容错小）
    gamma="scale",      # 核函数的影响范围
    random_state=42
)
```

### 2.6 保存和加载模型

```python
import joblib

# 保存
joblib.dump(model, "Lab9/svm_model.pkl")
joblib.dump(le, "Lab9/label_encoder.pkl")
joblib.dump(pca, "Lab9/pca.pkl")

# 加载
model = joblib.load("Lab9/svm_model.pkl")
```

---

## 3. 初学者常见问题

- **归一化**：像素值 0~255 → 除以 255 变成 0~1，有助于模型收敛
- **文件名顺序**：`sorted()` 按字符串排序，即 `000000.webp` < `000001.webp`，这样和测试集顺序一致
- **降维参数**：`n_components` 越小越快但可能丢失信息，越大信息保留越多但越慢
- **验证集**：训练时可从训练集分出一部分做验证，测试集不要碰

## 4. 拓展思路

除 SVM 外，可尝试：
- **KNN**：邻近算法，简单但效果不错
- **随机森林**：多棵树投票
- **小型 CNN**：用 PyTorch 搭建卷积神经网络
