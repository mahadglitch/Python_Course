class Robot:
    def __init__(self, name, model, purpose, power_level):
        self.name = name
        self.model = model
        self.purpose = purpose
        self.power_level = power_level

    def introduce(self):
        print("Hello! I am a robot 🤖")
        print(f"My name is {self.name}.")
        print(f"My model is {self.model}.")
        print(f"My purpose is {self.purpose}.")
        print(f"My current power level is {self.power_level}%.")

    def work(self):
        print(f"{self.name} is now working efficiently!")


my_robot = Robot(
    name="NeoBot",
    model="NB-X1",
    purpose="Helping humans with daily tasks",
    power_level=85
)


my_robot.introduce()
my_robot.work()
