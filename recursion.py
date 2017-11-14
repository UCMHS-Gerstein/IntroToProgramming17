import turtle as t
import time

win = t.Screen()
# win.bgcolor('black')

def fr(length):
    t.fd(length)
    t.rt(90)
    if(length > 2):
        fr(length//2)

def branch(length, ratio, angle):
    t.fd(length)
    if length > 10:
        return_to = t.pos()
        return_angle = t.heading()
        t.rt(angle)
        branch(length * ratio, ratio, angle)
        t.pu()
        t.goto(return_to)
        t.setheading(return_angle)
        t.lt(angle)
        t.pd()
        branch(length * ratio, ratio, angle)

# for angle in range(10, 100, 5):
#     t.clear()
#     t.pu()
#     t.goto(0, -250)
#     t.pd()
#     t.setheading(90)
#     branch(length=250, ratio=.6, angle=angle)
    

t.pu()
t.goto(0, -250)
t.pd()
t.lt(90)
branch(length=80, ratio=.75, angle=30)

win.mainloop()