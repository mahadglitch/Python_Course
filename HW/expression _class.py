class Expression:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def solve(self):
        result = (self.a + self.b) * self.c
        return result

    def display(self):
        print("Expression: (a + b) * c")
        print(f"a = {self.a}, b = {self.b}, c = {self.c}")
        print("Result =", self.solve())


exp = Expression(123, 234, 23)


exp.display()
