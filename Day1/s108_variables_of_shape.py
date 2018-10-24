# 사각형 그리기 응용

print("Hello git")

import turtle

size = input('사각형의 크기를 입력하세요.[100~300] ')
color = input('선의 색깔을 입력하세요.[red, blue, green] ')
thick = input('펜의 굵기를 입력하세요.[1~30] ')

angle = 90
thick = int(thick)
size = int(size)

turtle.color(color)
turtle.pensize(thick)

turtle.left(angle)
turtle.forward(size)

turtle.left(angle)
turtle.forward(size)

turtle.left(angle)
turtle.forward(size)

turtle.left(angle)
turtle.forward(size)

turtle.done()


# 위의 요소들을 살펴보면 left, forward 등과 같이 반복되는 단어들이 많은 것을 알 수 있다.
# 만약에 이러한 요소들의 명칭을 바꿔야 하는 경우, 하나씩 바꾸는 것은 비효율적이다.
# 고로, 영역 지정 후 마우스 오른쪽을 눌러 refactor 목록에서 한번에 이름을 바꿀 수 있다.
