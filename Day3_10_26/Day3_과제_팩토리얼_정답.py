# 숫자값 N을 입력받아, 1~N까지의 Sum과 Factorial 구하기

# 입력값에 대한 Validation 체크.  cf. 숫자값이 아닌경우 재입력

# 첫단계 : 입력 요소 정하기
# key_in = input("숫자값을 입력하세요,[1~100]")
# check_num =True


# 두번째 : 루프문 생성
while True:
    key_in = input("숫자값을 입력하세요,[1~100]")
    is_number =True
    chk_number = list('0123456789')

    for char in list(key_in):
        print(char)
        is_number = is_number * (char in chk_number)

        if not is_number:
            break

    if is_number:
        key_in = int(key_in)
        print("입력한 값은 %d 입니다." %key_in)
        break
    else:
        print("입력한 값은 숫자가 아닙니다.")
        continue

# Sum과 Factorial 결과값을 list 에 저장 후, 한꺼번에 출력
Sum = []
Factorial = []
sum, gop = 0, 1

for key_in in range(key_in+1):
    sum += key_in          # sum = sum + num
    gop *= key_in          # gop = gop * num
    if gop == 0:
        gop = 1

    #print(num, sum, gop)
    Sum.append(sum)
    Factorial.append(gop)

print(Sum)
print(Factorial)

print('%d까지의 합은 %d입니다.'%(key_in, Sum[-1]))
for key_in in range(len(Factorial)):
    print('%d! = %d' %(key_in, Factorial[key_in]))