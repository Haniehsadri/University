from Member import  Member
from Course import Course
class Student(Member):
    def __init__(self, Name, Lastename, Fathersname, Username, Password,Studentid):
        super().__init__(Name, Lastename, Fathersname, Username, Password)
        self.Studentid=Studentid

    def getStudentid(self):
        return self.Studentid

    def setLastname(self, Studentid):
        self.Studentid=Studentid




    def courseRegister(self,coursename,instructor):
        studentcourses = []
        cours=Course(coursename,instructor)
        studentcourses.append(cours)






