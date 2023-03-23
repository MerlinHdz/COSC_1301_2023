import turtle

# two sideways squares connected together
def square():
    for i in range(4):
        turtle.forward(100)
        turtle.right(90)


def fig1():
    turtle.setheading(45)
    square()
    turtle.setheading(-135)
    square()


# Isosceles triangle with triangle inside
def fig2():
    turtle.forward(200)
    turtle.left(120)
    turtle.forward(200)
    turtle.left(120)
    turtle.forward(200)

    turtle.setheading(45)
    turtle.forward(140)
    turtle.setheading(-45)
    turtle.forward(140)



fig2()

turtle.done()