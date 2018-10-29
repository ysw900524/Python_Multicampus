# 함수 호출 2
def exchangeUSDtoKRW(dollar):
    won = dollar * 1065
    return won

usd = 2000
krw = exchangeUSDtoKRW(usd)
print('환전한 금액은 %d원 입니다.'%krw)

    # 환전한 금액은 2130000원 입니다.



# 에러 발생
krw = exchangeUSDtoKRW()
print('환전한 금액은 %d원 입니다.'%krw)

    # Traceback (most recent call last):
#     #   File "C:/Users/student/PycharmProjects/Multicampus/Day3_10_26/s501_함수_호출2.py", line 12, in <module>
#     #     krw = exchangeUSDtoKRW()
#     # TypeError: exchangeUSDtoKRW() missing 1 required positional argument: 'dollar'