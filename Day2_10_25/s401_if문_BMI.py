# BMI 판정 프로그램
weight = float(input("체중(kg)은?"))
height = float(input("키(cm)는?"))

# BMI 계산
height = height / 100   # m으로 고친다
bmi = weight / (height * height)

# BMI 값에 따라 결과로 분기 --- (*1)
result = ""
if bmi < 18.5:
    result = "마름"
elif (18.5 <= bmi) and (bmi < 25):
    result = "보통"
elif (25 <= bmi) and (bmi < 30):
    result = "가벼운 비만"
elif bmi >= 30:
    result = "심한 비만"
    # 주의!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # else :
    #   result = "심한 비만"
    # 마지막 elif 구문에 위의 수식을 넣어도 값이 나온다.
    # 주의!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # 파이썬의 경우에는 비교연산자를 25 <= bmi <30 : 같이 넣어도 작동한다.

# 결과 표시
print("BMI :", bmi)
print("판정 :", result)
