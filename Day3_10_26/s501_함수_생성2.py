# 함수 생성 2

def add_num(num1, num2):
    result = num1 + num2
    return result

param1 = 40
param2 = 50
sum = add_num(param1, param2)
print('%d와 %d의 합은 %d입니다.'%(param1, param2, sum))


# 주의!!!!!!!!
    # 함수는 실행되고 난 뒤 결과값을 받는다.
    # 그러나 함수 안에 함수를 넣어 실행하는 경우에는 안의 함수가 실행된 이후
    # 바깥쪽(두번째 실행되는 함수) 함수의 경우에는 null값(none값)을 받게 되는 것이다.
    # 결과값을 출력하도록 만들기 위해서는 return 명령어를 사용해 값을 주어줘야 한다.