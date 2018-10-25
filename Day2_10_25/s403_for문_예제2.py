# break vs. continue vs. pass

scope = list(range(1, 100))

for num in scope:

    if num <= 10:
        if num%2 == 0:
            pass
            print(num, 'is even number.')
        else:
            continue
            print(num, 'is odd number.')
    else:
        print(num, 'is bigger than ten')
        break
        print('after break')
    # pass는 아무 의미가 없다.
    # 그런데도 넣어주는 것은 조건문의 경우에 : 이후에 블록문구들이 와야만 하는 문법에 따라
    # 문법적 오류를 회피하기 위해 넣어주는 것이다.
    # continue는 다음 조건문을 연속해 이어가게 만드는 조건이다.
    # break는 계속해서 돌아가는 for, while 문에서 조건 만족시 멈추게 만드는 조건이다.
    # 보통 break는 while문에서 많이 쓰이며, for문의 경우에는 주어진 변수들의 값만큼만 돌지만, 중간에 조건 만족시
    # 멈추게 하고자 할 때는 for문에도 break가 쓰인다.


print('프로그램을 종료합니다.')


    # 2 is even number.
    # 4 is even number.
    # 6 is even number.
    # 8 is even number.
    # 10 is even number.
    # 11 is bigger than ten
    # 프로그램을 종료합니다.

