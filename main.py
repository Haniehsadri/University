from Member import Member
from Student import  Student
def login():
    studentid=1000
    in1=input("welcome to university select you status 1-student  2-instructor  3-esducation secretary ")
    name=input("enter your name : ")
    lastname=input("enter your last name: ")
    fathersname=input("enter your fathersname")


student=Student("hani","sadri","yousef","haniehsadri","haniehsadri",1234)
member = Member("hani", "ss", "hh", "ss", "gg")

members=[]
members.append(student)

members.append(member)
def search(members, username, password):

    for letter in members:
        if isinstance(letter,Student):
            print("welcome student")
            print(members.index(letter))
        elif letter.getUsername() == username and letter.getPassword() == password:
            return members.index(letter)

search(members,"ss","gg")

