class Student:
    def __init__(self, school_name, department_name,  student_name, student_id, address, credits, gpa):
        self.school_name = school_name
        self.department_name = department_name
        self.student_name = student_name
        self.student_id = student_id
        self.address = address
        self.credits = credits
        self.gpa = gpa

    #學校名稱 SET AND GET
    def getSchoolName(self):
        return self.school_name

    def setSchoolName(self, new_school_name):
        self.school_name = new_school_name

    #科系 SET AND GET
    def getDepartmentName(self):
        return self.department_name

    def setDepartmentName(self, new_department_name):
        self.department_name = new_department_name
    #姓名 SET AND GET
    def getStudentName(self):
        return self.student_name

    def setStudentName(self, new_student_name):
        self.student_name = new_student_name

    #學號 SET AND GET
    def getStudentID(self):
        return self.student_id

    def setStudentID(self, new_student_id):
        self.student_id = new_student_id
    #地址 SET AND GET
    def getAddress(self):
        return self.address

    def setAddress(self, new_address):
        self.address = new_address

    #學分 SET AND GET
    def getCredits(self):
        return self.credits

    def setCredits(self, new_credits):
        self.credits = new_credits

    #成績GPA SET AND GET
    def getGPA(self):
        return self.gpa
    def setGPA(self, new_gpa):
        self.gpa = new_gpa
#建立一個STUDENT1
student1 = Student("STUST", "engineer",  "Jay", "4B0G0090", "南台街", 110, 4.0)
#更改GPA
student1.setGPA(6)
student1.setCredits(20)
#輸出
print("School:",student1.getSchoolName())
print("department_name:",student1.getDepartmentName())
print("name:",student1.getSchoolName())
print("StudentID:",student1.getStudentID())
print("adress:",student1.getAddress())
print("credits:",student1.getCredits())
print("GPA:",student1.getGPA())




