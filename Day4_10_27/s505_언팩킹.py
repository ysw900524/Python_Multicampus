# unpacking

def add(a, b):
    return a + b

data = (10, 20)     #Tuple 형태
# print(add(data))
    # 오류 발생
    # Traceback (most recent call last):
    #   File "C:/Users/student/PycharmProjects/Multicampus/Day4_10_27/s505_언팩킹.py", line 7, in <module>
    #     print(add(data))
    # TypeError: add() missing 1 required positional argument: 'b'
    # => Tuple 형태로 묶여있기 때문에  data가 a인자로 들어가도 b 인자가 없기 때문에 오류가 발생한다.

print(add(*data))   # unpacking
    # 정상 실행된다,
    # 30 => 결과값
    # *를 붙여 data를 unpacking 해주었기 때문에 a,b에 10, 20이 들어간 것이다.

## 주의!!!!
# 선언시의 *와 호출시의 *의 역할이 다르다.
# 선언 시에는 packing으로 묶어주는 역할을 하고,
# 호출 시에는 unpacking으로 풀어주는 역할을 한다.





def introduce(name, greeting):
    return "{name}님, {greeting}".format(
        name = name,
        greeting = greeting
    )
            # {name}과 {greeting}은 사전형의 key값을 의미.

introduce_dict = {
    "name" : "김진수",
    "greeting" : "안녕하세요"
}   # {}는 사전형을 의미.
print(introduce(**introduce_dict))
    # 사전형 형태의 데이터를 unpacking 해서 인자값을 호출한 것이다.
    # 앞서 말했듯이 호출 시의 **은 선언 시와는 역할이 다르다.


    # 김진수님, 안녕하세요
