from Member import Member
from Grade import Grade


class Instructor(Member):


    def __init__(self, Name, Lastename, Fathersname, Username, Password):
        super().__init__(Name, Lastename, Fathersname, Username, Password)
        self.coursesofinstructor = []

    currentcourse=0
    def grade(self):
        for course in self.coursesofinstructor:
            print(course.getTitle(), course.getId())
        courseid = input("enter the course id :")
        for c in self.coursesofinstructor:
            if courseid == c.getId():
                currentcourse = self.coursesofinstructor.index(c)
        for student in self.coursesofinstructor[currentcourse].studentsOfCourse:
            print(student.getName(), student.getLastname(), student.getStudentid())
            grad = input("enter student's grad: ")
            grade = Grade(grad,self. coursesofinstructor[currentcourse],student)
            student.studentgrades.append(grade)
            self.coursesofinstructor[currentcourse].gradesofcourse.append(grade)





    def printinformation(self):
        print(self.getLastname())