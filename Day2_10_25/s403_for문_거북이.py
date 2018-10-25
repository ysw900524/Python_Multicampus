# for 문 거북이

import turtle as t

num_circle = 30
radius = 180

t.bgcolor("green")      # 배경색
t.color("yellow")       # 선 색
t.speed(0.8)            # 속도

for _ in range(num_circle):
    t.circle(radius)    # radius 반지름
    t.left(360/num_circle)  # 360/30=12 => 12도만큼 왼쪽으로 옮긴 후 생성하게 된다.

t.done