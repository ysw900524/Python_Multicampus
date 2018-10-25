# 튜플형 응용

width = 20
height = 30
area = width * height

print('너비 :', width)
print('높이 :', height)
print('넓이 :', area)

    # 너비 : 20
    # 높이 : 30
    # 넓이 : 600


data = (15, 50)
width, height = data
area = width * height
    # data 는 15, 50의 두가지 변수를 가지는 튜플 형태의 자료이다.
    # 이 경우, width와 height에 각각 따로 있는 값들을 할당하는 것이 가능하다.
    # width -> 15, height -> 50을 각각 배정
    # 이것을 unpacking이라고 한다.

print('너비 :', width)
print('높이 :', height)
print('넓이 :', area)

    # 너비 : 15
    # 높이 : 50
    # 넓이 : 750