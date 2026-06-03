import base64
import pickle

# 加密函数：utf-8编码 → base64加密
def encrypt_content(content: str) -> str:
    """
    对字符串进行base64加密
    :param content: 原始字符串
    :return: 加密后的字符串
    """
    # 先转bytes，再base64加密，再转回字符串
    b_content = content.encode("utf-8")
    b_encrypt = base64.b64encode(b_content)
    return b_encrypt.decode("utf-8")

# 解密函数：base64解密 → utf-8解码
def decrypt_content(encrypt_str: str) -> str:
    """
    对base64加密字符串解密
    :param encrypt_str: 加密后的字符串
    :return: 原始字符串
    """
    b_encrypt = encrypt_str.encode("utf-8")
    b_decrypt = base64.b64decode(b_encrypt)
    return b_decrypt.decode("utf-8")

# 读取secret.txt并加密，保存至secret_encrypted.txt
with open("Lab3/data/secret.txt", "r", encoding="utf-8") as f:
    original_content = f.read()  
encrypt_str = encrypt_content(original_content)  # 加密
print(f"原始内容：\n{original_content}\n")
print(f"加密后的内容：\n{encrypt_str}\n")
with open("Lab3/data/secret_encrypted.txt", "w", encoding="utf-8") as f:
    f.write(encrypt_str)  
print("文件加密完成，加密结果保存至secret_encrypted.txt")

# 读取加密文件并解密还原
with open("Lab3/data/secret_encrypted.txt", "r", encoding="utf-8") as f:
    encrypt_content_read = f.read()
decrypt_str = decrypt_content(encrypt_content_read)  # 解密
print(f"解密后的原始内容：\n{decrypt_str}")

# pickle保存加密和解密函数至cipher.pkl（二进制模式）
cipher_functions = [encrypt_content, decrypt_content]
with open("Lab3/data/cipher.pkl", "wb") as f:
    pickle.dump(cipher_functions, f)
print("加密解密函数已保存至cipher.pkl")

# 测试：pickle载入函数并使用
with open("Lab3/data/cipher.pkl", "rb") as f:
    load_encrypt, load_decrypt = pickle.load(f)
test_str = "测试base64加密解密"
test_encrypt = load_encrypt(test_str)
test_decrypt = load_decrypt(test_encrypt)
print(f"\npickle测试：原始{test_str} → 加密{test_encrypt} → 解密{test_decrypt}")