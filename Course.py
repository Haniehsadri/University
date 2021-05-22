class Course:

    def __init__(self, Title, Id):
        self.Title = Title
        self.Id = Id
        self.studentsOfCourse = []
        self.gradesofcourse = []

    def getTitle(self):
        return self.Title

    def setTitle(self, Title):
        self.Title = Title

    def getInstructor(self):
        return self.Instructor

    def setInstructor(self, Instructor):
        self.Instructor = Instructor

    def getVacancy(self):
        return self.Vacancy

    def setVacancy(self, Vacancy):
        self.Vacancy = Vacancy

    def getId(self):
        return self.Id

    def setId(self, Id):
        self.Id = Id

    def printinformation(self):
        print("Id:", self.getId(), "Title :", self.getTitle()
              , "Instructor: ", self.getInstructor(), "vacancy:", self.getVacancy())

    def studentsinformation(self):
        if len(self.gradesofcourse) > 0:
            for s in self.gradesofcourse:
                print("name", s.student.getName(), "lastname:", s.student.getLastname(),
                      "studentId:", s.student.getStudentid(), "student grade: ", s.grade)
        else:
            print("the grades are not available ")
            for s in self.studentsOfCourse:
                print("name", s.student.getName(), "lastname:", s.student.getLastname(),
                      "studentId:", s.student.getStudentid())

    def addstudent(self, student):
        self.studentsOfCourse.append(student)

    def courseaverage(self):
        sum2=[]
        for grade in self.gradesofcourse:
            sum2.append(int (grade.grade))

        if len(sum2)!=0:
            average=sum (sum2)/len(sum2)