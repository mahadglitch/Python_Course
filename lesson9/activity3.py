from abc import ABC , abstractmethod
class animal(ABC):
    def move(self):
        pass
class human(animal):
    def move(self):
        print("I Can Walk")   
class dog(animal):
    def move(self):
        print("I Can Bark")
h = human()
h.move()
d = dog()
d.move()                  