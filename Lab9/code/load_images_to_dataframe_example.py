from pathlib import Path

import numpy as np
import pandas as pd
from PIL import Image

# 修改这里，指向训练集或测试集图片目录。
IMAGE_DIR = Path(__file__).resolve().parent / "train"
IMAGE_SIZE = 48

# 最多读取的图片数量
MAX_IMAGES = None # None 表示读取全部图片
# MAX_IMAGES = 2000 # 测试用，只读取前 2000 张图片



def list_image_paths(image_dir: Path) -> list[tuple[str, Path]]:
    items: list[tuple[str, Path]] = []
    for class_dir in sorted([path for path in image_dir.iterdir() if path.is_dir()]):
        label = class_dir.name
        for image_path in sorted([path for path in class_dir.iterdir() if path.is_file()]):
            if image_path.suffix.lower() not in {".jpg", ".jpeg", ".png", ".webp"}:
                continue
            items.append((label, image_path))
    if MAX_IMAGES is not None:
        items = items[:MAX_IMAGES]
    return items


def load_image_as_row(image_path: Path) -> np.ndarray:
    image = Image.open(image_path).convert("RGB")
    image = image.resize((IMAGE_SIZE, IMAGE_SIZE))
    return np.asarray(image, dtype=np.uint8).reshape(-1)


items = list_image_paths(IMAGE_DIR)
labels = []
pixel_rows = []

for label, image_path in items:
    labels.append(label)
    pixel_rows.append(load_image_as_row(image_path))

pixels = np.vstack(pixel_rows)
pixel_columns = [f"px_{index:04d}" for index in range(pixels.shape[1])]

df = pd.DataFrame(pixels, columns=pixel_columns)
df.insert(0, "label", labels)

print("Loaded images:", len(df))
print(df.shape)
print(df.head())
