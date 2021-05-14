from Member import Member
from Student import Student
from Instructor import Instructor
from Educatinsecretary import  Educationsecretary
from Course import Course

members = []
courses=[]


def login():

    studentid = 1000
    in1 = int(input("welcome to university select you status 1-student  2-instructor  3-esducation secretary "))
    name = input("enter your name : ")

    lastname = input("enter your last name: ")
    fathersname = input("enter your fathersname")
    username = input("enter your user name: ")
    password = input("enter your password:")
    if in1 == 1:
        studentid = studentid + 1
        print("your studentid is: " + str(studentid))
        student = Student(name, lastname, fathersname, username, password, studentid)
        members.append(student)



    if in1 == 2:
       instructor = Instructor(name, lastname, fathersname, username, password)
       members.append(instructor)

    if in1 == 3:
        educationsecretary = Educationsecretary(name, lastname, fathersname, username, password)
        members.append(educationsecretary)
        yesorno=int(input("do you want to add course ? 1- yes  2- no "))
        if yesorno==1:
            titleofcours=input("enter the title of course:")
            idofcours=input("enter the id of course")
            course=Course(titleofcours,idofcours)
            for i in members:
                if isinstance(i, Instructor):
                    print(i.printinformation())
            instructorofcourse=input("enter the instructor of course lastname from the list : ")
            for i in members:
                if isinstance(i,Instructor) and i.getLastname()==instructorofcourse:
                    course.setInstructor(instructorofcourse)

            vacancyofcourse=input("enter the vacancy of course: ")
            course.setVacancy(vacancyofcourse)





def search(members, username, password):
    for letter in members:
        if isinstance(letter, Student):
            print("welcome student")
            print(members.index(letter))
        elif letter.getUsername() == username and letter.getPassword() == password:
            print(members.index(letter))

login()
print(members[1].getFathersname())