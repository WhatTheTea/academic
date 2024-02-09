import turtle as t

screen = t.Screen()
t.degrees()

def drawtriangle():
    for i in range(3):
        t.right(60)
        t.forward(100)
        t.right(60)

def spacing():
    t.up()
    t.fd(150)
    t.down()

drawtriangle()
spacing()
t.color("#DDCC00")
drawtriangle()
spacing()
t.fillcolor("red")
t.begin_fill()
drawtriangle()
t.end_fill()
input()