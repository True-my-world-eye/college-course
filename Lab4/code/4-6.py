class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def get_name(self):
        print(self.name)
        return 
    
    def do_homework(self):
        print("There is no homework from the parent")

class Student(Human):
    def __init__(self, name, age,homework):
        super().__init__(name, age)
        self.homework=homework
    
    def do_homework(self):
        super().do_homework()
        print("作业为："+self.homework)

if __name__ == "__main__":
    stu = Student("John", 20, "Python实验")
    print(stu.name, stu.age, stu.homework)
    stu.get_name()
    stu.do_homework()