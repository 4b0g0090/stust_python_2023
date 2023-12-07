class Student:
    def __init__(self,name,age,ID):
        self.name=name
        self.age=age
        self.ID=ID
    @property
    def Student_name(self):
        print(f'"{self.name}"was acceessed.')
        return self.name

    @Student_name.setter
    def Student_name(self, value):
        print(f'"{self.name}"is now"{value}".')
        self.name=value
        
    @Student_name.deleter
    def Student_name(self ):
        print(f'"{self.name}"was deleted')


    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("ID:",self.ID)    

if __name__=="__main__":
    Student1=Student("Jay",20,"s123")
    print(Student1.Student_name)
    
    Student1.Student_name = "peter"


    print(Student1.Student_name)
























    