class person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname , self.lastname)
class student(person):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)
        self.gyear = year
obj = student("Mahad" , "Kyser" , 2011)
obj.printname()
print(obj.gyear)        