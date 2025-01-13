#Underwater Scene - ALL

#Initialize
import turtle
yareli = turtle.Turtle()
yareli.speed(10)
 #Turtle for Yareli

diego=turtle.Turtle() 
diego.speed(10)
diego.pensize(8)
#Turtle for Diego

Matti=turtle.Turtle()
Matti.speed(10)
#Turtle for Matti

#Functions
#Code for Yareli
yareli.dot(3000, "#4dd2ff")
def draw_seastar(size, color, x, y):
    yareli.begin_fill()
    yareli.pensize(10)
    yareli.pencolor(color)
    yareli.color(color)
    yareli.up()
    yareli.goto(x, y)
    yareli.pd()
    for i in range(5):
        yareli.forward(size)
        yareli.right(144)
    yareli.end_fill()

def draw_allSeastars(): #Yareli
    draw_seastar(100, "#ffaa00", 110, 90) 
    draw_seastar(70, "#ff0000", -50, -200)
    draw_seastar(30, "black", -300, 350) 

def draw_seaweed(size,color,x,y): #Code for Diego - one seaweed
    diego.penup()
    diego.goto(x,y) # allows for the locations to be a variable
    diego.pendown()
    diego.color(color)# allows for the color to be a variable 
    for i in range(3):
        diego.circle(size,180) #size makes the size a variable 
        diego.circle(-size,180)
    
def draw_all_seaweed(): #Code for Diego - multiple seaweed
    draw_seaweed(20,"green",-300,-400)
    draw_seaweed(40,"light green",-100,-400)
#sets the seaweed into place

#Code for Matti - Fish
def draw_Fish(size,color,x,y):
    Matti.penup()
    Matti.goto(x,y)
    Matti.dot(size,color)
    Matti.color(color)
    Matti.begin_fill()
    Matti.pendown()
    Matti.setheading(0)
    Matti.forward(size/1.2)
    Matti.right(90)
    Matti.forward(size/2)
    Matti.right(120)
    Matti.forward(size)
    Matti.right(120)
    Matti.forward(size)
    Matti.right(120)
    Matti.forward(size * 1.1)
    Matti.end_fill()
def drawAllFish(): #Draw multiple fish - Matti
    draw_Fish(100,"red",100,200)
    draw_Fish(60,"green",250,-200)

    
#Main
draw_allSeastars() #Yareli
drawAllFish() #Matti
draw_all_seaweed() #Diego
