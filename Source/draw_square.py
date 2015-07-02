import turtle

def draw_square(some_turtle):
    for i in range(0, 4):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_something():
    window = turtle.Screen()
    window.bgcolor("blue")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("red")
    brad.speed(100)
    for i in range(1, 37):
        draw_square(brad)
        brad.right(10);
    


##    angie = turtle.Turtle()
##    angie.shape("arrow")
##    angie.color("yellow")
##    angie.circle(100)
##    angie.speed(10)

##    chloe = turtle.Turtle();
##    chloe.shape("triangle")
##    chloe.color("green")
##    chloe.triangle()
    

    window.exitonclick()

draw_something()
