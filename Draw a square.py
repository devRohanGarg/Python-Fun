import turtle

def draw_square():

    windows = turtle.Screen()
    windows.bgcolor("#581845")

    brush = turtle.Turtle()
    brush.shape("turtle")
    brush.color("#FFFFFF", "#C70039")
    brush.speed('fastest')
    
    k=0;
    l=0;
    
    while(k < 360):
        l = 0
        while(l < 4):
            brush.forward(100)
            brush.right(90)
            l += 1
        brush.circle(100)
        brush.right(5)
        k += 5
    

    windows.exitonclick()

draw_square()
