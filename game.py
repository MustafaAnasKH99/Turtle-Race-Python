#Continue -- Code Club
import turtle
from random import randint

#Main pen
main_turtle = turtle.Turtle()
main_turtle.penup()
main_turtle.goto(-140, 140)

#Map main loop
for i in range(15):
    main_turtle.speed(100)
    main_turtle.write(i, align="center")
    main_turtle.right(90)
    main_turtle.forward(10)
    main_turtle.pendown()
    main_turtle.forward(150)
    main_turtle.penup()
    main_turtle.backward(160)
    main_turtle.left(90)
    main_turtle.forward(20)

# Turtle no. 1
batata = turtle.Turtle()
batata.color('red')
batata.shape('turtle')
batata.penup()
batata.goto(-160, 100)
batata.pendown()

# Turtle no. 2
makdoos = turtle.Turtle()
makdoos.color('yellow')
makdoos.shape('turtle')
makdoos.penup()
makdoos.goto(-160, 70)
makdoos.pendown()

# Turtle no. 3
borghol = turtle.Turtle()
borghol.color('green')
borghol.shape('turtle')
borghol.penup()
borghol.goto(-160, 40)
borghol.pendown()

# Turtle no. 4
banadoora = turtle.Turtle()
banadoora.color('blue')
banadoora.shape('turtle')
banadoora.penup()
banadoora.goto(-160, 10)
banadoora.pendown()

#Race main loop
for i in range(100):
    batata.forward(randint(1,5))
    banadoora.forward(randint(1,5))
    borghol.forward(randint(1,5))
    makdoos.forward(randint(1,5))