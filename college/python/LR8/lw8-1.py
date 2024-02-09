import turtle
#
turtle.reset()
turtle.tracer(1)
turtle.width(2)
#
turtle.up()
x=0
y=-100
turtle.goto(x, y)
turtle.begin_fill()
turtle.color("#ffaa00")
turtle.down()
turtle.circle(100)
turtle.end_fill()
turtle.color("black")
turtle.circle(100) 
turtle.up()
#
x= -45
y=50
turtle.goto(x, y)
turtle.down()
turtle.color("#0000aa")
turtle.begin_fill()
turtle.circle(7)
turtle.up()
turtle.end_fill()
#
x=45
y=50
turtle.goto(x, y)

turtle.down()
turtle.color("#0000aa")
turtle.begin_fill()
turtle.circle(7)
turtle.up()
turtle.end_fill()
#
x= -55
y= -50
turtle.goto(x, y)
turtle.right(45)
turtle.width(3)
turtle.down()
turtle.color("#aa0000")
turtle.circle(80, 90)
turtle.up()
#
turtle.right(135)
x=0
y=50
turtle.goto(x, y)
turtle.width(2)
turtle.color("black")
turtle.down()
turtle.forward(100)
#
turtle.mainloop()