## 데이터형 변환

#데이터형 확인
num_data = 350
str_data = '350'

print(type(num_data))
print(type(str_data))

    # <class 'int'>
    # <class 'str'>

# 에러 발생
sum = num_data + str_data

    # Traceback (most recent call last):
    #   File "C:/Users/student/PycharmProjects/Multicampus/Day2_10_25/s204_datatype.py", line 14, in <module>
    #     sum = num_data + str_data
    # TypeError: unsupported operand type(s) for +: 'int' and 'str'
        # 숫자형과 문자형의 데이터를 더해주라는 연산자를 넣었기 때문에 오류가 발생한다.


# 데이터형 변환
sum = int(str_data) + num_data
print('합계는? ', str(sum))

    # 합계는?  700