import turtle as t

t.pensize(5)
t.color('red')

side_cnt = 6
width = 60
angle = 360/side_cnt

# for i in range(side_cnt):
#     t.forward(width)
#     t.left(angle)
    # => 원을 하나 그려본다.

for j in range(side_cnt):
    for i in range(side_cnt):
        t.forward(width)
        t.left(angle)

    t.forward(width)
    t.right(angle)
    # => 하나씩 더해가면서 원이 구해지는 과정을 구한다.

# 주의!!!!!
# 숫자로 표현되는 부분은 변수로 지정해주는 것이 좋다!
# 변수 지정까지 해야만 100% 성공인 것.
# 코드를 호환 가능하면서 간단하게 만드는 것이 중요하다!