# Keyword Argument

#키워드 인자 활용하기
def introduceMyCar(brand, seats=4, type='세단'):
    print('나의 차는 {b} {s}인승 {t}이다.'.format(
        b = brand,
        s = seats,
        t = type
    ))
    # print('나의 차는', brand, '의', seats, '인승', type, '입니다.')

# 위치 인자 값 1개
introduceMyCar('아우디')

    # 나의 차는 아우디 4인승 세단이다.


# 키워드 인자 값 1개
introduceMyCar(brand='렉서스')

    # 나의 차는 렉서스 4인승 세단이다.


# 위치 인자 값 1개, 키워드 인자 값 1개, 혼용으로 사용 가능
introduceMyCar('제규어', seats=2)
    #introduceMyCar(seats=2,'제규어')
        # 키워드를 주지 않은 경우 순서가 맞지 않으면 오류가 발생한다.

    # 나의 차는 제규어 2인승 세단이다.


# 키워드 인자 값 2개
introduceMyCar(brand='머큐리', type='머슬카')

    # 나의 차는 머큐리 4인승 머슬카이다.


# 순서 바뀐 키워드 인자 값 2개, 순서가 바뀐 경우는 반드시 키워드 인자값 사용
introduceMyCar(type='미니벤', brand='카니발')

    # 나의 차는 카니발 4인승 미니벤이다.


# 순서를 지킨 위치 인자 값 3개, 순서가 같다면 모두 위치 인지 값 사용 가능
introduceMyCar('카니발', 9, '미니벤')

    # 나의 차는 카니발 9인승 미니벤이다.


# 순서 바뀐 키워드 인자 값 3개, 순서가 바뀐 경우는 반드시 키워드 인자값 사용
introduceMyCar('쉐보레', type='SUV', seats=7)

    # 나의 차는 쉐보레 7인승 SUV이다.
