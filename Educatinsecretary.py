from Member import Member
from Course import Course
from Instructor import Instructor


class Educationsecretary(Member):

    def __init__(self, Name, Lastename, Fathersname, Username, Password):
        super().__init__(Name, Lastename, Fathersname, Username, Password)

    def addcourse(title, members,courses):

        titleofcours = input("enter the title of course:")
        idofcours = input("enter the id of course")
        vacancy = input("enter the vacancy")
        course = Course(titleofcours, idofcours)
        course.setVacancy(vacancy)
        for i in members:

            if isinstance(i, Instructor):
                print(i.getLastname())
        instructorofcourse = input("enter the instructor of course lastname from the list : ")
        for letter in members:
            if isinstance(letter, Instructor) and letter.getLastname() == instructorofcourse:
                course.setInstructor(instructorofcourse)
                letter.coursesofinstructor.append(course)
                courses.append(course)
