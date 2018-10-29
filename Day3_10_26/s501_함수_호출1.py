# 함수 호출 1
def sayHello():
    print('Hi, Guys !!')

sayHello()

    # Hi, Guys !!
    # sayHello()함수만 실행했을 때의 결과값

print(sayHello())
    # 함수에 함수를 넣어서 활용하는 경우

    # Hi, Guys !!
    # None
    # sayHello() 함수의 결과값이 나온 이후, print 함수는 출력할 결과값을 찾기 못해 None값을 내보냈다.


# 주의!!!!!!!!
    # 함수는 실행되고 난 뒤 결과값을 받는다.
    # 그러나 함수 안에 함수를 넣어 실행하는 경우에는 안의 함수가 실행된 이후
    # 바깥쪽(두번째 실행되는 함수) 함수의 경우에는 null값(none값)을 받게 되는 것이다.
    # 결과값을 출력하도록 만들기 위해서는 return 명령어를 사용해 값을 주어줘야 한다.
    # 예시)
        #def sayHello():
        #   print('Hi, Guys !!')
        #   return 성공!

        # print(sayHello())
            # => Hi, Guys !!
            #    성공!
                # print함수의 결과값이 같이 출력된다.