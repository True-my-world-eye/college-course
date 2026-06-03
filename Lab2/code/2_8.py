from functools import reduce

# 罗马字符与整数的映射
roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

def roman_to_int(s: str) -> int:
    # 用map将罗马字符转为数值列表
    values = list(map(lambda c: roman_map[c], s))
    # 用reduce实现加减规则：左小右大则减，否则加
    return reduce(
        lambda acc, i: acc + values[i] if values[i] >= values[i+1] else acc - values[i],
        range(len(values)-1),
        values[-1]  # 初始值为最后一个元素
    )

if __name__ == "__main__":
    print(roman_to_int("IV"))   # 4
    print(roman_to_int("IX"))   # 9
    print(roman_to_int("MCMXCIV")) # 1994
    print(roman_to_int("LVIII"))   # 58