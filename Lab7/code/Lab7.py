# -*- coding: utf-8 -*-
"""
蛋白质功能预测实验 - 完整可运行代码
特征：氨基酸组分 + 二肽组分 + k-space特征
模型：XGBoost（分类效果最优）
输出：preds.txt（200行 0/1）
"""

import numpy as np
import pandas as pd
from collections import Counter
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score
from xgboost import XGBClassifier

# ===================== 1. 配置路径 =====================
TRAIN_PATH = "Lab7/data/ProSeqs_Train.txt"
TEST_PATH = "Lab7/data/ProSeqs_Test.txt"
SAVE_PATH = "Lab7/output/preds.txt"

# 20种标准氨基酸
AA20 = ['A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I',
         'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V']

# ===================== 2. 序列读取函数 =====================
def load_train_data(path):
    df = pd.read_csv(path)
    seqs = df['sequence'].values
    labels = df['label'].values
    return seqs, labels

def load_test_data(path):
    df = pd.read_csv(path)
    seqs = df['sequence'].values
    return seqs

# ===================== 3. 特征提取核心函数 =====================
def clean_seq(s):
    return ''.join([c if c in AA20 else 'X' for c in s])

def get_aa_composition(seq):
    """氨基酸组分（21维：20标准+X）"""
    cnt = Counter(seq)
    total = len(seq)
    feat = []
    for aa in AA20 + ['X']:
        feat.append(cnt.get(aa, 0) / total if total > 0 else 0)
    return np.array(feat)

def get_dipeptide(seq):
    """二肽组分（441维）"""
    dipeps = [seq[i:i+2] for i in range(len(seq)-1)]
    cnt = Counter(dipeps)
    total = len(dipeps)
    feat = []
    for a in AA20 + ['X']:
        for b in AA20 + ['X']:
            key = a + b
            feat.append(cnt.get(key, 0) / total if total > 0 else 0)
    return np.array(feat)

def get_kspace(seq, k=2):
    """k-space组分（k=2，共2*21维）"""
    feat = []
    for i in range(k):
        sub = seq[i::k]
        feat.extend(get_aa_composition(sub))
    return np.array(feat)

def extract_features(seq_list):
    """统一提取所有特征并拼接"""
    features = []
    for s in seq_list:
        s = clean_seq(s)
        f1 = get_aa_composition(s)
        f2 = get_dipeptide(s)
        f3 = get_kspace(s, k=2)
        f = np.concatenate([f1, f2, f3])
        features.append(f)
    return np.array(features)

# ===================== 4. 主流程 =====================
if __name__ == "__main__":
    # 读取数据
    print("正在读取训练集...")
    train_seqs, y_train = load_train_data(TRAIN_PATH)
    print("正在读取测试集...")
    test_seqs = load_test_data(TEST_PATH)

    # 特征提取
    print("正在提取特征（氨基酸+二肽+k-space）...")
    X_train = extract_features(train_seqs)
    X_test = extract_features(test_seqs)

    # 标准化
    print("正在标准化...")
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # 训练最优模型 XGBoost
    print("正在训练模型...")
    model = XGBClassifier(
        n_estimators=200,
        max_depth=6,
        learning_rate=0.1,
        subsample=0.8,
        colsample_bytree=0.8,
        random_state=42,
        eval_metric="logloss"
    )
    model.fit(X_train, y_train)

    # 预测
    print("正在预测测试集...")
    y_pred = model.predict(X_test)

    # 保存结果（只输出0/1，每行一个）
    print(f"正在保存到 {SAVE_PATH} ...")
    with open(SAVE_PATH, 'w') as f:
        for label in y_pred:
            f.write(f"{label}\n")

    # 训练集内部验证（查看F1）
    y_train_pred = model.predict(X_train)   
    y_train_np = np.asarray(y_train)
    y_train_pred_np = np.asarray(y_train_pred)
    f1 = f1_score(y_train_np, y_train_pred_np)
    print(f"训练集 F1 Score: {f1:.4f}")
    print("✅ 全部完成！preds.txt 已生成")