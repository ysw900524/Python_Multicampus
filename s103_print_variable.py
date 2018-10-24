# 변수에 문자 담기

name = "홍길동"
greeting = "안녕"

print(name, greeting)
print(greeting, name)

text = name, '님, ', greeting, '하세요.'
print(text)


# 변수에 숫자 담기

coffee1_name = "카페라떼";
coffee1_val = 4000;
coffee2_name = "카푸치노";
coffee2_val = 4500;
coffee3_name = "마끼야또";
coffee3_val = 5000;

#Case1
# print('손님, ' + coffee1_name + coffee2_name + coffee3_name + '를 주문하셨습니다.')
# print('가격은 ' + coffee1_val + coffee2_val + coffee3_val + '원 입니다.')
    # Case1은 오류가 발생하는  case다. 왜냐하면 이름과 가격이 다른 형식의 자료이기 때문이다.
    # 또한, 전체 실행 시 Case1을 주석으로 만들지 않으면 오류 이후 작업들이 실행되지 않는다.
    # 이는 위에서부터 순차적으로 실행되는 프로그램의 특성 상 오류 발생시 그 위치에서 멈추기 때문이다.
    # 고로, 실제 작업 시에는 오류가 뜨는지 수시로 확인하고, 뜨는 경우 해결 이후 진행해야 좋다.

#Case2
print('손님, ' + coffee1_name + coffee2_name + coffee3_name + '를 주문하셨습니다.')
print('가격은 ' + str(coffee1_val + coffee2_val + coffee3_val) + '원 입니다.')
    # 이름과 가격의 요소들을 같은 문자 형태로 바꿔주자 오류가 사라졌다.

#Case3
coffee_val = coffee1_val + coffee2_val + coffee3_val
print('손님, \n%s, %s, %s를 주문하셨습니다.' %(coffee1_name, coffee2_name, coffee3_name))
    # \n은 줄바꿈, %s은 뒤의 요소들을 각각의 위치에 넣어주는 표현식.(s는 string의 문자를 의미)
print('가격은 %d입니다.' %coffee_val)
    # %d는 숫자 요소를 넣어주는 표현식(d는 dashboard라는 숫자를 의미)


