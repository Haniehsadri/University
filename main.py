from Member import Member
from Student import Student
from Instructor import Instructor
from Educatinsecretary import Educationsecretary
from Course import Course

members = []
courses = []


def signup():
    username = input("enter your username: ")
    password = input("enter your password:")
    currentmember = search(members, username, password)

    if currentmember != -1 and isinstance(members[currentmember], Instructor):
        while True:
            yesorno = input("do you want to give score to your courses?1 yes 2- no")
            if yesorno == "1":
                members[currentmember].grade()
            if yesorno == "2":
                break
    if currentmember != -1 and isinstance(members[currentmember], Student):
        while True:
            yesorno = input("do you want to register course? 1- yes  2-no")
            if yesorno == "1":
                members[currentmember].courseRegister(courses)
            if yesorno == "2":
                break
        members[currentmember].transcription()
        for j in members[currentmember].studentcourses:
            print(j.getTitle())
    if currentmember != -1 and isinstance(members[currentmember], Educationsecretary):
        while True:
            yesorno = int(input("do you want to add course ? 1- yes  2- no "))
            if yesorno == 1:

                titleofcours = input("enter the title of course:")
                idofcours = input("enter the id of course")
                vacancy = input("enter the vacancy")
                course = Course(titleofcours, idofcours)
                course.setVacancy(vacancy)
                for i in members:
                    # print(isinstance(i, Instructor))
                    if isinstance(i, Instructor):
                        print(i.getLastname())
                instructorofcourse = input("enter the instructor of course lastname from the list : ")
                for letter in members:
                    if isinstance(letter, Instructor) and letter.getLastname() == instructorofcourse:
                        course.setInstructor(instructorofcourse)
                        letter.coursesofinstructor.append(course)
                        courses.append(course)
            if yesorno == 2 :
                break


def signin():
    studentid = 1000
    in1 = input("welcome to university select you status 1-student  2-instructor  3-esducation secretary ")
    name = input("enter your name : ")

    lastname = input("enter your last name: ")
    fathersname = input("enter your fathersname")
    username = input("enter your user name: ")
    password = input("enter your password:")
    if in1 == "1":
        studentid += 1
        print("your studentid is: " + str(studentid))
        student = Student(name, lastname, fathersname, username, password, studentid)
        members.append(student)

    if in1 == "2":
        instructor = Instructor(name, lastname, fathersname, username, password)
        members.append(instructor)

    if in1 == "3":
        educationsecretary = Educationsecretary(name, lastname, fathersname, username, password)
        members.append(educationsecretary)


def search(members, username, password):
    for letter in members:
        if letter.getUsername() == username and letter.getPassword() == password:
            return members.index(letter)
    return -1


signin()
signin()
signin()
print("signup")
signup()
signup()
signup()
signup()
