import turtle as t

screen = t.Screen()
t.tracer(False)
t.degrees()
t.bgcolor("blue")
t.color("#DDCC00")
t.fillcolor("#DDCC00")
def draw():
    for i in range(5):
        t.left(180-36)
        t.forward(50)
def spacing():
    t.up()
    t.left(30)
    t.fd(90)
    t.down()

for i in range(12):
    t.begin_fill()
    draw()
    t.end_fill()
    spacing()
    
input()