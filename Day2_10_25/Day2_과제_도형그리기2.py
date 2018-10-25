# 반복문 (for 혹은 while)을 사용하여 그려보기
    # 1단계 : 먼저 정육각형을 그려보기
    # 2단계 : 정육각형을 회전이동하면서 반복하여 그려보기


import turtle
import math
import time

width = 50
num_shape = 6

input('엔터를 치면 거북이가 그림 그려요.')

# turtle.forward(width)
# turtle.right(60)
# turtle.forward(width)
# turtle.right(60)
# turtle.forward(width)
# turtle.right(60)
# turtle.forward(width)
# turtle.right(60)
# turtle.forward(width)
# turtle.right(60)
# turtle.forward(width)


# for _ in range(1, 3):
#     for _ in range(1, 3):
#         for _ in range(1, 4):
#             turtle.forward(width)
#             turtle.right(60)
#             time.sleep(1)
#             turtle.forward(width)
#             turtle.right(60)
#             turtle.forward(width)
#             turtle.right(60)
#             turtle.forward(width)
#             turtle.right(60)
#             turtle.forward(width)
#             turtle.right(60)
#             turtle.forward(width)
#             turtle.right(180)
#         turtle.forward(width)
#         turtle.left(60)
#     turtle.forward(width)
#     turtle.left(60)
#
# turtle.done()


import turtle

for xxx in range(6):
    turtle.right(60)
    turtle.forward(100)
    for yyy in range(6):
        turtle.left(60)
        turtle.forward(100)

turtle.done()
