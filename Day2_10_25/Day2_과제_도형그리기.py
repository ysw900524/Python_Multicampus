import turtle
import math
import time

width = 100
height = 100
slide = math.sqrt(width**2 + height**2)


input('엔터를 치면 거북이가 도형을 그립니다.')

turtle.shape('turtle')
turtle.pensize(5)
turtle.color('blue')

print('거북이 달리기 시작합니다.')
#time.sleep(1)
turtle.forward(width)

#time.sleep(1)
turtle.right(135)
turtle.forward(slide)

#time.sleep(1)
turtle.left(135)
turtle.forward(width)

#time.sleep(1)
turtle.left(135)
turtle.forward(slide)

#time.sleep(1)
turtle.left(135)
turtle.forward(height)

#time.sleep(1)
turtle.left(90)
turtle.forward(width)

#time.sleep(1)
turtle.left(90)
turtle.forward(width)

#time.sleep(1)
turtle.left(45)
turtle.forward(slide/2)

#time.sleep(1)
turtle.left(90)
turtle.forward(slide/2)


turtle.done()


# time.sleep(1)
# turtle.right(90)
# turtle.forward(width)
#
# time.sleep(1)
# turtle.


