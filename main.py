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
                members[currentmember].addcourse(members, courses)

            if yesorno == 2:
                break
        while True:
            yesno = input("do you want to see courses informations? 1- yes 2- no ")
            if yesno == "1":

                for course in courses:
                    if len(course.studentsOfCourse) != 0:
                        print("course title:", course.getTitle(), "course id: ", course.getId()
                              , )
                courseid = input("enter the course Id : ")
                for c in courses:
                    if c.getId() == courseid:
                        currentcourse = courses.index(c)
                courses[currentcourse].studentinformation()
            if yesno == "2":
                break


def signin():
    studentid = 1000
    in1 = input(" select your status 1-student  2-instructor  3-esducation secretary ")
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


def changepassword(members, currentmember):
    while True:
        oldpassword = input("enter your password : ")
        if members[currentmember].getPassword() == oldpassword:
            newpassword = input("enter your new password:")
            confirmatiom = input("repeat your new password for confirmatio :")
            if newpassword == confirmatiom:
                members[currentmember].setPassword(newpassword)
                print(" your password changed")
                break

        else:
            print("the repeat of your password dos not match to you new password or your old password is not correct ")


while True:
    siginorup = input("welcome to university select to 1-signin or 2-signup:")
    if siginorup == "1":
      signin()
    if siginorup=="2":
        signup()
    yesorno=input("do you want to continue? 1- yes 2- no ")
    if yesorno=="1 ":
        break
