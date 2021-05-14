from Member import Member
from Course import Course


class Educationsecretary(Member):

    def __init__(self, Name, Lastename, Fathersname, Username, Password):
        super().__init__(Name, Lastename, Fathersname, Username, Password)

    def addcours(title, id, instructor, vacancy, courses):
        course = Course(title, id)
        course.setInstructor(instructor)
        course.setVacancy(vacancy)
        courses.append(course)
