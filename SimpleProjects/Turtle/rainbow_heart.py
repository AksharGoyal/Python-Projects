import turtle

colours = ['purple','blue','green','orange','yellow','red']
t = turtle.Pen()
turtle.Screen().title("RAINBOW HEART")
turtle.bgcolor('black')
t.width(4)
t.left(90)
t.setposition(0, 75)
t.hideturtle()
startingX = t.pos()[0]
startingY = t.pos()[1]
colourCounter = 0

for x in range(45):
    t.pencolor(colours[colourCounter % 6])
    colourCounter += 1
    t.forward(11)
    t.left(5)

tracker = 0
while t.pos()[0] < startingX:
    t.pencolor(colours[colourCounter % 6])
    colourCounter += 1    
    t.forward(10)
    tracker += 1

t.left(2 * (360 - t.heading()))

while tracker > 0:
    t.pencolor(colours[colourCounter % 6])
    colourCounter += 1    
    t.forward(10)
    tracker -= 1

for x in range(45):
    t.pencolor(colours[colourCounter % 6])
    colourCounter += 1    
    t.left(5)
    t.forward(11)

turtle.Screen().exitonclick()