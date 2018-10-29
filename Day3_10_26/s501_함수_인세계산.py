# 인세를 계산하는 함수
def calc_royalty(price, sales, per):
    rate = per / 100
    royalty = int(price * sales * rate)
    return royalty

# 사용자가 정보를 입력한다.
i = input("책의 정가는? ")
price = int(i)

i = input("발행 부수는? ")
sales = int(i)

i = input("인세율(퍼센트)은? ")
per = float(i)

# 결과 표시
v = calc_royalty(price, sales, per)
print("인세는 ", v, "원입니다.")


    # 책의 정가는? 27000
    # 발행 부수는? 1000
    # 인세율(퍼센트)은? 30
    # 인세는  8100000 원입니다.
