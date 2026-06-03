stu_grade = []
pass_count = 0  # 及格人数（成绩>=60）
total_count = 0  # 总人数

with open("Lab3/data/stu_grade.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        sno, sname, score = line.split(",")
        score = float(score)
        stu_grade.append((sno, sname, score))
        total_count += 1
        if score >= 60:
            pass_count += 1

# 按成绩降序排序
stu_grade_sorted = sorted(stu_grade, key=lambda x: -x[2])
# 计算及格率
pass_rate = round((pass_count / total_count) * 100, 2) if total_count > 0 else 0.0

# 将结果写入stu_grade_output.txt
with open("Lab3/data/stu_grade_output.txt", "w", encoding="utf-8") as f:
    f.write("学号\t姓名\t成绩\n")
    
    for sno, sname, score in stu_grade_sorted:
        f.write(f"{sno}\t{sname}\t{score:.1f}\n")
    # 及格率
    f.write(f"\n总人数：{total_count}\t及格人数：{pass_count}\t及格率：{pass_rate}%\n")

print("成绩排序完成，结果已保存至stu_grade_output.txt")
print(f"总人数：{total_count}，及格人数：{pass_count}，及格率：{pass_rate}%")