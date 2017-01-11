import turtle

def draw_square():
    fly = ("fly.gif")
    window = turtle.Screen()
    #window.bgcolor("grey")
    window.setup(450, 300)
    window.bgpic("turtle.gif")
    window.register_shape(fly)

    brad = turtle.Turtle()
    brad.penup()
    brad.setposition(100, 100)
    brad.pendown()
    brad.shape(fly)
    brad.color("dark green")
    brad.pensize(4)
    brad.speed(1.5)


    count = 0

    while count < 4:
        
        brad.forward(100)
        brad.right(90)
        count = count +1  

    window.exitonclick()
    

draw_square()
