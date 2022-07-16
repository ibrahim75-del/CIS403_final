import turtle
import time
from turtle import *
from random import *
import turtle
import time
window = turtle.Screen()
window.setup(1.0, 1.0)

def splashPage():
    turtle.bgcolor("black")
    turtle.pencolor("white")
    turtle.write("Project 4", align="center", font=("Cooper Black", 20, "bold"))
    turtle.penup()
    turtle.right(90)
    turtle.forward(40)
    turtle.write("TURTLE RACE", align="center",font=("Cooper Black", 20, "bold"))
                 
    turtle.penup()
    turtle.forward(40)
    turtle.write("Ibrahim Diakite", align="center", font=("Cooper Black", 20, "bold"))
    turtle.ht()


splashPage()

time.sleep(1.5)
turtle.clear()

#SCREEN SETUP
setup(800, 500)
title("Turtle Race")
bgcolor("white")
speed(0)

# HEADING
penup()
goto(-100, 205)
color("black")
write("The Best Shall WIN! Let's GO! ", align="center", font=("Poppins", 20, "bold"))

#DIRT
goto(-350, 200)
pendown()
color("dimgrey")
begin_fill()
for i in range(2):
  forward(700)
  right(90)
  forward(400)
  right(90)
end_fill()

# FINISH LINE
gap_size = 20
shape("square")
penup()

#BLACK SQUARES ROW 1
color("lightgrey")
for i in range(10):
  goto(250, (170 - (i * gap_size * 2)))
  stamp()

#BLACK SQUARES ROW 2
for i in range(10):
  goto(250 + gap_size, ((210 - gap_size) - (i * gap_size * 2)))
  stamp()

#YELLOW SQUARES ROW 1
color("black")
for i in range(10):
  goto(250, (190 - (i * gap_size * 2)))
  stamp()

#YELLOW SQUARES ROW 2
for i in range(10):
  goto(251 + gap_size, ((190 - gap_size) - (i * gap_size * 2)))
  stamp()

#TURTLE  = blue 
blue_turtle = Turtle()
blue_turtle.color("blue")
blue_turtle.shape("turtle")
blue_turtle.shapesize(2)
blue_turtle.penup()
blue_turtle.goto(-300, -50)
blue_turtle.pendown()

#TURTLE  - GREEN 
green_turtle = Turtle()
green_turtle.color("chartreuse")
green_turtle.shape("turtle")
green_turtle.shapesize(2)
green_turtle.penup()
green_turtle.goto(-300, 50)
green_turtle.pendown()


#TURTLE  - PINK
pink_turtle = Turtle()
pink_turtle.color("hotpink")
pink_turtle.shape("turtle")
pink_turtle.shapesize(2)
pink_turtle.penup()
pink_turtle.goto(-300, -150)
pink_turtle.pendown()

#TURTLE  - RED
red_turtle = Turtle()
red_turtle.color("red")
red_turtle.shape("turtle")
red_turtle.shapesize(2)
red_turtle.penup()
red_turtle.goto(-300, 150)
red_turtle.pendown()

#PAUSE FOR 1 SECOND BEFORE RACING 
time.sleep(1)

#MOVE THE TURTLES
while red_turtle.xcor() <= 230 and green_turtle.xcor() <= 230 and pink_turtle.xcor() <= 230 and blue_turtle.xcor() <= 230:
  red_turtle.forward(randint(1, 10))
  green_turtle.forward(randint(1, 10))
  pink_turtle.forward(randint(1, 10))
  blue_turtle.forward(randint(1, 10))

# CELEBRATE THE WINNER
# RED TURTLE WINS 
if red_turtle.xcor() > green_turtle.xcor() and red_turtle.xcor() > pink_turtle.xcor() and red_turtle.xcor() > blue_turtle.xcor():
  print("Red Turtle Wins!") 
  for i in range(72):
    red_turtle.right(5)
    red_turtle.shapesize(3.5)
    red_turtle.write("Red Turtle Wins!" , align="center", font=("Cooper Black", 30, "bold"))
    
# GREEN TURTLE WINS
elif green_turtle.xcor() > red_turtle.xcor() and green_turtle.xcor() > pink_turtle.xcor() and green_turtle.xcor() > blue_turtle.xcor():
  print("Green Turtle Wins!")
  for i in range(72):
    green_turtle.right(5)
    green_turtle.shapesize(3.5)
    green_turtle.write("Green Turtle Wins!" , align="center", font=("Cooper Black", 30, "bold"))
# BLUE TURTLE WINS
elif blue_turtle.xcor() > red_turtle.xcor() and blue_turtle.xcor() > green_turtle.xcor() and blue_turtle.xcor() > pink_turtle.xcor():
  print("Blue Turtle Wins!")
  for i in range(72):
    blue_turtle.right(5)
    blue_turtle.shapesize(3.5)
    blue_turtle.write("Blue Turtle Wins!" , align="center", font=("Cooper Black", 30, "bold"))

# PINK TURTLE WINS
else:
  print("Pink Turtle Wins!")
  for i in range(72):
    pink_turtle.right(5)
    pink_turtle.shapesize(3.5)
    pink_turtle.write("Pink Turtle Wins!" , align="center", font=("Cooper Black", 30, "bold"))

