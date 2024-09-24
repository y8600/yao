import turtle

def draw_sky():
 
    turtle.penup()
    turtle.goto(-400,200)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("sky blue")
    for _ in range(2):
        turtle.forward(800)
        turtle.right(90)
        turtle.forward(400)
        turtle.right(90)
    turtle.end_fill()

def draw_sun():
    turtle.penup()
    turtle.goto(0,100)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("yellow")
    turtle.circle(50)
    turtle.end_fill()

def draw_grass():
    turtle.penup()
    turtle.goto(-400, -200)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("green")
    for _ in range(2):
        turtle.forward(800)
        turtle.right(90)
        turtle.forward(200)
        turtle.right(90)
    turtle.end_fill()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        