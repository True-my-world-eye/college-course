student_scores={"Alice":85,"Bob":90,"Charlie":78,"David":92,"Eve":88}

for name, score in student_scores.items():
    print(f"{name}: {score}")

max_student = max(student_scores, key=student_scores.get)
print(f"成绩最高者：{max_student},成绩：{student_scores[max_student]}")