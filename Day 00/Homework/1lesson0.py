
from turtle import *

#we want to paint a house
#step 1:draw a square
speed(5)
width(7)
begin_fill()
color("red")
forward(150)
left(90)
forward(150)
left(90)
forward(150)
left(90)
forward(150)
left(90)
end_fill()
#finish of square

#drawing a door

forward(100)
left(90)
begin_fill()
color("black")
forward(50)
left(90)
forward(40)
left(90)
forward(50)
end_fill()
#end of door

#lets start to make a roof
penup()
goto(150,150)

pendown()
begin_fill()
color("blue")
right(150)
forward(148)

left(120)
forward(145)
end_fill()

#lets start to make the windows
width(6)

color("black")
penup()
goto(100,100)
pendown()

left(120)
forward(50)
left(90)
forward(40)
left(90)
forward(47)
left(90)
forward(40)

penup()
goto(155,155)
pendown()
color("blue")
right(90)
right(90)

left(90)
forward(150)
color("red")
left(90)

forward(15)
left(90)
color("black")
forward(50)
right(90)
forward(40)
right(90)
forward(50)
right(90)
forward(40)
#end house


exitonclick()