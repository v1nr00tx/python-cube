from vpython import *

scene.title = "Meu cubo 3D"
scene.background = color.black

cubo = box(pos=vector(0,0,0),
           size=vector(2,2,2),
           color=color.green,
           opacity=0.8)

while True:
    rate(30)