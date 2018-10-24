# Case 1
name = input('당신의 이름은 무엇입니까?')
print(name + '님. 반갑습니다.')

# Case 2
order = input('00카페입니다. \n무엇을 주문하시겠습니까? ')
count = input('몇 잔을 드릴까요? ')

print('%s %s잔을 주문하셨습니다. \n잠시만 기다려 주세요.' %(order, count))

# Case 3
price = 4500
cost = price * count

print('%s %s잔을 주문하셨습니다. \n결제하실 금액은 %s원입니다.' %(order, count, cost))
    # 이 경우 결과값이 222222222222222...와 같이 나오는데, 그 이유는 count 변수가 문자로 인식되기 때문이다.
    # 문자 요소를 4500번 반복해 나타내게 하는 식이 되어버리기 때문에 cost 요소에 대한 변환이 필요하다.
    # 아래 case4에서 바꾸어 보자,

# Case 4
price = 4500
cost = price * int(count)   # count 요소를 숫자 정수로 바꾸어준다.

print('%s %s잔을 주문하셨습니다. \n결제하실 금액은 %d원입니다.' %(order, count, cost))
    # cost의 경우에는 숫자값을 받아야 하므로 표현식을 %d로 해준다.
    # 제대로 값이 나오는 것을 확인할 수 있다.


