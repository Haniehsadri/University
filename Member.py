class Member:
    def __init__(self, Name, Lastename, Fathersname, Username, Password):
        self.Name = Name
        self.Lastname = Lastename
        self.Fathersname = Fathersname
        self.Username = Username
        self.Password = Password

    def getName(self):
        return self.Name


    def setName(self, Name):
        self.Name = Name


    def getLastname(self):
        return self.Lastname

    def setLastname(self, Lastname):
        self.Lastname = Lastname

    def getFathersname(self):
        return self.Fathersname

    def setFathersname(self, Fathersname):
        self.Fathersname = Fathersname

    def getUsername(self):
        return self.Username

    def setUsername(self, Username):
        self.Username = Username

    def getPassword(self):
        return self.Password

    def setUsername(self, Password):
        self.Password = Password



    def printinformation(self):
        print(self.getLastname())