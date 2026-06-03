from mc import Student

s1 = Student("A", 18, "M", [80,90,85])
s2 = Student("B", 19, "F", [77,82])
s3 = Student("C", 20, "M", [95])

print(s1.get_info())
print(s1.avg())
print(s2.get_info())
print(s2.avg())
print(s3.get_info())
print(s3.avg())