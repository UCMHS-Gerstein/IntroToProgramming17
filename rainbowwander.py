import turtle as t
import random
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
screensize = 150
x = 0

t.speed('high')
t.pensize(3)

while True:
  dist = random.randint(1, 5)
  c = colors[x % len(colors)]
  rot = random.randint(-10, 10)
  t.color(c)
  t.fd(dist)
  t.rt(rot)
  x += 1
  if t.xcor() > screensize:
    t.penup()
    t.setx(-screensize)
    t.pendown()
  elif t.xcor() < -screensize:
    t.penup()
    t.setx(screensize)
    t.pendown()
  if t.ycor() > screensize:
    t.penup()
    t.sety(-screensize)
    t.pendown()
  elif t.ycor() < -screensize:
    t.penup()
    t.sety(screensize)
    t.pendown()