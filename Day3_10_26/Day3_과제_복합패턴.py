# 복합적인 패턴을 찾아서, 반복문을 적용하기
# 패턴 : 각도, 길이, 굵기, 색상
# HINT : 적용된 색상 값은 다음과 같다.
        #colors = ['red', 'green', 'blue', 'yellow', 'purple', 'cyan', 'magenta', 'violet']


import turtle as t

colors = ['red', 'green', 'blue', 'yellow', 'purple', 'cyan', 'magenta', 'violet']

# 첫번째 단계 : 단순하게 하나의 패턴을 찾아본다.
    # for i in range(8):
    #     t.forward(i)
    #     t.left(360/8)

# 두번째 단계 : 하나씩 조건들을 늘려간다.
    # for i in range(8):
    #     t.pensize(i)
    #     t.color(colors[i%8])
    #     t.forward(i)
    #     t.left(360/8)

# 세번째 단계 : 구체화
for i in range(45):
    t.pensize(i)
    t.color(colors[i%8])
    t.forward(i*5)
    t.left(360/8)

t.done()






# 실패의 흔적들
    # 점점 키워나가는 걸 왜 생각하지 못했을까...
#################################################################
    # import turtle as t
    #
    # side_cnt = 8
    # angle = 360/side_cnt
    # length = 80
    # width = 15
    # colors = ['red', 'green', 'blue', 'yellow', 'purple', 'cyan', 'magenta', 'violet']
    #
    # # t.color(colors[0])
    # t.forward(length)
    # t.right(angle)

    # for i in range(side_cnt):
    #     t.pensize(width - i)
    #     t.color(colors[i-1])
    #     t.forward(length)
    #     t.right(angle+(i*1))

    # t.pensize(width)
    # t.color(colors[0])
    # t.forward(length)
    # t.right(angle)
    # t.pensize(width)
    # t.color(colors[1])
    # t.forward(length)
    # t.right(angle)
    # t.pensize(width)
    # t.color(colors[2])
    # t.forward(length)
    # t.right(angle)
    # t.pensize(width)
    # t.color(colors[3])
    # t.forward(length)
    # t.right(angle)
    # t.pensize(width)
    # t.color(colors[4])
    # t.forward(length)
    # t.right(angle)
    # t.pensize(width)
    # t.color(colors[5])
    # t.forward(length)
    # t.right(angle)
    # t.pensize(width)
    # t.color(colors[6])
    # t.forward(length)
    # t.right(angle)
    # t.pensize(width)
    # t.color(colors[7])
    # t.forward(length)
    # t.right(angle)

    # print(range(side_cnt))
    # for i in range(side_cnt):
    #     t.pensize(width)
    #     t.color(colors[side_cnt-i])
    #     t.forward(length)
    #     t.right(angle)



    # for i in range(0, side_cnt):
    #     t.pensize(width-i/10)
    #     t.color(colors[i])
    #     t.forward(length-i/10)
    #     t.right(angle-i/10)

