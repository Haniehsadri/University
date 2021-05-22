from Member import Member
from Course import Course


class Student(Member):
    def __init__(self, Name, Lastename, Fathersname, Username, Password, Studentid):
        super().__init__(Name, Lastename, Fathersname, Username, Password)
        self.Studentid = Studentid
        self.studentcourses = []
        self.studentgrades = []

    def getStudentid(self):

        return self.Studentid

    def setLastname(self, Studentid):

        self.Studentid = Studentid

    def courseRegister(self, courses):

        for s in courses:
            s.printinformation()

        coursesid = input("entercoursesidfrom the list:")
        for c in courses:
            if c.getId() == coursesid:
                self.studentcourses.append(c)
                # c.studentsOfCourse.append(self)
                c.addstudent(self)
                c. setVacancy(int(c. getVacancy())- 1)

    def transcription(self):
        sum1 = []
        for grade in self.studentgrades:
            print(grade.course.getTitle(), grade.grade)
            sum1.append(int(grade.grade))

        if len(sum1) != 0:

            average = sum(sum1) / len(sum1)
            print(average)
