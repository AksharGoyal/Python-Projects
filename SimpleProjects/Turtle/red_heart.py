import turtle

colours = ['red','purple','blue','green','orange','yellow']
t = turtle.Pen()
turtle.Screen().title("RED HEART")
turtle.bgcolor('black')
t.pencolor('red')
t.width(2)
t.left(90)
startingX = t.pos()[0]
startingY = t.pos()[1]

for x in range(45):
    t.forward(5)
    t.left(5)

tracker = 0
while t.pos()[0] < startingX:
    t.forward(2)
    tracker += 1

t.left(2 * (360 - t.heading()))

while tracker > 0:
    t.forward(2)
    tracker -= 1

for x in range(45):
    t.left(5)
    t.forward(5)

turtle.Screen().exitonclick()