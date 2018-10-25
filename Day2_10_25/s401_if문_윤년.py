# 윤년 판정
year = int(input("서기 몇 년? "))

# 판정식
is_leap = False
if year % 400 == 0 :
    is_leap = True
elif year % 100 == 0 :
    is_leap = False
elif year % 4 == 0 :
    is_leap = True
else :
    is_leap = False


is_leap