import turtle
colors = ['mistyrose', 'slategray', 'sienna', 'yellowgreen', 'powderblue', 'khaki']
t = turtle.Pen()
turtle.bgcolor('black')
for x in range(180):
    t.pencolor(colors[x % 6])
    t.width(x/100 + 1)
    t.forward(x)
    t.left(59)