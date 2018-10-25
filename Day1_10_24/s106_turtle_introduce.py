# 거북이 소개

import turtle
import time
    # turtle과 time은 파이썬 내부에 속해 있는 모듈이다.

input ('엔터를 치면 거북이를 소개합니다. ^^')

turtle.shape('turtle')

print('앞으로 전진합니다.')
time.sleep(1)
turtle.forward(100)

print('한번 더 앞으로 전진합니다.')
time.sleep(1)
turtle.forward(100)

print('왼쪽으로 전진합니다.')
time.sleep(1)
turtle.left(90)
turtle.forward(100)

print('오른쪽으로 전진합니다.')
time.sleep(1)
turtle.right(90)
turtle.forward(100)

turtle.done()

# turtle의 경우 파이썬 내에 속해 있는 모듈이다. 그러므로 만약에 파이썬 내에서 turtle이란 단어를 쓰고 있다면,
# 파이썬의 모듈과 중복될 수 있으므로, 파일의 이름을 turtle로 저장해서는 안된다.
# 해결 방법은 모듈과 다른 이름으로 바꾸어주면 된다.
