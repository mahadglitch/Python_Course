class cat :
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def info(self):
        print(f"I am a cat , my name is {self.name} and my age is {self.age}")
    def make_sound(self):
        print("Cat here")
class dog :
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def info(self):
        print(f"I am a dog , my name is {self.name} and my age is {self.age}")
    def make_sound(self):
        print("Dog here")
cat1 = cat("Tom","3")
dog1 = dog("Bob","4")
for animal in (cat1,dog1):
    animal.info()
    animal.make_sound()                                