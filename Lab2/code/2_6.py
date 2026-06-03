# 原始学生数据
students = [
    ('CHEN Xiaoming', '计算机学院', 20, 85.5),
    ('LI Siyu', '文学院', 19, 92.3),
    ('WANG Haoran', '计算机学院', 21, 86.9),
    ('ZHANG Yuxin', '医学院', 20, 85.5),
    ('LIU Zixuan', '文学院', 18, 94.0)
]

sorted_students = sorted(
    students,
    key=lambda x: (-x[3], x[1], x[2])  # 绩点降序 → 学院升序 → 年龄升序
)
result = [
    (name, college)
    for name, college, age, gpa in sorted_students
]

for item in result:
    print(item)