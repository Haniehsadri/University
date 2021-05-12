from Member import Member
from Student import Student
from Instructor import Instructor

members = [Student("hh", "gg", "hh", "hh", "gg", "gg")]
print(members[0].Lastname)


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

# if in1 == 3:
# educationsecretary = Educationsecretary(name, lastname, fathersname, username, password)
# members.append(educationsecretary)


def search(members, username, password):
    for letter in members:
        if isinstance(letter, Student):
            print("welcome student")
            print(members.index(letter))
        elif letter.getUsername() == username and letter.getPassword() == password:
            print(members.index(letter))

login()
print(members[1].getLastname)