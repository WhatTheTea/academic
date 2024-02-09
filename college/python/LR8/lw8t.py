import turtle as t

try:
    shapes = int(input("Кількість фігур: "))
except:
    print("error")
    exit()

screen= t.Screen()
t.bgcolor("green")
t.color("yellow")      
t.tracer(True)
angles=6
size=40
angle=360/angles
for k in range(shapes):
   for p in range(angles):
      t.forward(size)
      t.right(angle)
   t.right(360/shapes)
input()                      
