class GradeManager:
    def __init__(self):
        self.student={}

    def add_student(self,student_id:str,name:str,grade:float):
        self.student[student_id]={"姓名":name,"成绩":grade}

    def remove_student(self, student_id: str):
        if student_id in self.student:
            del self.student[student_id]

    def get_grade(self,student_id:str)->float:
        return self.student.get(student_id, {}).get("成绩",None)
    
    def get_average(self)->float:
        if not self.student:
            return 0.0
        total_grade=sum(student["成绩"] for student in self.student.values())
        return total_grade/len(self.student)
    
    def get_top_student(self)->tuple:
        if not self.student:
            return None
        return max(self.student.items(), key=lambda item: item[1]["成绩"])

if __name__=="__main__":
    gm=GradeManager()
    gm.add_student("001", "张三", 95)
    gm.add_student("002", "李四", 88)
    print(gm.student)
    print("李四的成绩:", gm.get_grade("002"))
    print("最高分:", gm.get_top_student())
    print("平均分:", gm.get_average())
    gm.remove_student("002")
    print(gm.student)
    
    
