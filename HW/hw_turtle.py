import turtle

screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.title("Fun with Shapes - Turtle Graphics")

t = turtle.Turtle()
t.speed(3)
t.width(3)

# TRIANGLE 
t.penup()
t.goto(-200, 0)
t.pendown()

t.color("black", "red")
t.begin_fill()
for _ in range(3):
    t.forward(100)
    t.left(120)
t.end_fill()

# RECTANGLE 
t.penup()
t.goto(0, 0)
t.pendown()

t.color("black", "green")
t.begin_fill()
for _ in range(2):
    t.forward(140)
    t.left(90)
    t.forward(80)
    t.left(90)
t.end_fill()

# HEXAGON 
t.penup()
t.goto(200, 0)
t.pendown()

t.color("black", "yellow")
t.begin_fill()
for _ in range(6):
    t.forward(80)
    t.left(60)
t.end_fill()


t.hideturtle()
screen.exitonclick()
