class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def introduce(self):
        return (f"my name is {self.name} and I am {self.age} years old. A student of L2E: Studying {self.course}")

    def change_course(self, value):
        self.course = value
        # return self.course


student1 = Student("wisdom", 12, "med-biochem")
student2 = Student("Nifemi", 21, "Medicine")
student3 = Student("Chika", 45, "Zoology")

# print(student1.introduce())
# print(student2.introduce())
# print(student3.introduce())

# print(student1.change_course("biochem"))
# # print(student1.introduce())


print(student1.course)
print(student1.name)
print(student1.age)
