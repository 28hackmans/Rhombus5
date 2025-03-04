import turtle

screen = turtle.Screen()
screen.screensize(500,500)
screen.bgcolor("yellow")

t = turtle.Turtle()
t.speed(1)

t.goto(0,0)

t.fillcolor("brown")
t.begin_fill()
t.speed(0)
t.setheading(45)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.end_fill()



t.setheading(135)

t.fillcolor("cyan")
t.begin_fill()
t.speed(0)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.end_fill()


turtle.done()