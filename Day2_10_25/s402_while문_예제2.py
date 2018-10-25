# while 문

# 루프 탈출
num, sum = 1, 0

while True :
    sum += num      # sum = sum + num
    if sum >100:
        break
    else:
        num += 1

print('num 값이 %d 일 때 while문 탈출 !!' % num)


    # num 값이 14 일 때 while문 탈출 !!