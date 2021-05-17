class Course:
    Vacancy = 0;

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
        print(self.getId(), self.getTitle()
              , self.getInstructor(), self.getVacancy())

    def addstudent(self,student):
        self.studentsOfCourse.append(student)