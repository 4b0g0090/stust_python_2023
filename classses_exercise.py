class Person:
    def __init__(self,name,age):
        self.name =name
        self.age=age

    def __str__(self):
        return f"name:{self.name} age:{self.age}"
    def myfunc(self):
        print("Hello my name is "+ self.name)

p1=Person("John",36)
p2=Person("Jennifer",25)


p1.age=50
#del p1

print(p1)
print(p2)
print(p1.myfunc(),p2.myfunc())


class student:
    pass
