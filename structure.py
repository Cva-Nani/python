from turtle import *

hideturtle()
speed(100)
bgcolor('black')
colormode(255)
colors = [(78,253,84),
          (32,210,244),
          (255,7,58)]

counter = 1
for i in range(500):
    color(colors[i%3])
    forward(counter)
    left(121)
    counter += 2
done()
