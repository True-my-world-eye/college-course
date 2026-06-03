class Person:
    def __init__(self,name,age,sex):
        self.__name=name
        self.__age=age
        self.__sex=sex
    def get_info(self):
        return self.__name,self.__age,self.__sex
    
class Student(Person):
    def __init__(self, name, age, sex,scores):
        super().__init__(name, age, sex)
        self.scores=scores
    def avg(self):
        return sum(self.scores)/len(self.scores)
    def get_info(self):
        info=super().get_info()
        return info,self.scores