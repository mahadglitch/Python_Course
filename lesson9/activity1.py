class person(object):
    def __init__(self,name,idnumber):
        self.name = name
        self.idnumber = idnumber
    def display(self):
        print(self.name)
        print(self.idnumber)
class employee(person):
    def __init__(self,name,idnumber,sallery,post):
        self.sallery = sallery
        self.post = post
        person.__init__(self,name,idnumber)
obj = employee("Mahad" , 4356 , 986348 , "intern")
obj.display()                     