class Student:
    def __init__(self, name, id,major):
        self.name = name
        self.id = id
        self.major=major
        self.courses = []

    def add_course(self, course):
      
        if course not in self.courses:
            self.courses.append(course)
        
            print(f"{self.name,self.id,self.major} 選修課程：{course}")
        

    def drop(self, course):
        if course in self.courses:
            self.courses.remove(course)
            print(f"{self.name,self.id,self.major} 退選課程：{course}")

    def list(self):
        if self.courses:
            print(f"{self.name,self.id,self.major} 修課清單:")
            for course in self.courses:
                print(course)


student1 = Student("John", "S001","cise")
student2=Student("peter","S02","im")


student1.add_course("AI")
student1.add_course("python")

student1.list()

student2.add_course("AI")
student2.add_course("C++")

student2.list()

student1.drop("python")#退選
student1.list()