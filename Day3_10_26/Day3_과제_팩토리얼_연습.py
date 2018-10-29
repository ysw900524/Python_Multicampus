while True:
    check_num = True

    num = input('숫자를 입력해 주세요!')

    num = list(num)
    print(num)

    for char in num:
        print(char, type(char), ' <- 요놈을 숫자인지 체크')


    if check_num:
        print("입력한값은 입니다.")
        break
    else:
        print("숫자가 아닙니다.")



#
#
# for i in range(len(num)):
#     if type(num[i]) == 'int':
#         print('합계 및 팩토리얼 구하기!!')
#         break
#     else:
#         print('입력한 값이 숫자가 아닙니다.')
#         continue
#
# sum = 0
# fac = 1
#
while num:
    for i in range(int(num)):
        sum += i + 1
        fac *= i + 1
        print("%d!=%d" % (i, fac))
    print(sum)
    break
#
#
#
#
#
# #
# # if 1 <= num <=100 :
#     print()






######################################################################################################
# num = input('tntwk')
#
# # int(num)
# # print(type(num[1]))
# # print(type(num))
# int(num[1])
# for i in range(len(num)):
#     if type(num[i]) == 'int':
#         print('합계 및 팩토리얼 구하기!!')
#         break
#     else:
#         print('입력한 값이 숫자가 아닙니다.')
#         continue
tf = 1
check = list()
check_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
while True:
    num = input('숫자를 입력해 주세요, [1~100] => ')
    num2 = list(num)
    print(num2)
    # print(check_list)
    for i in num2:
        tf *= i in check_list
        print(tf)
    if tf == '1':
        break
    else:
        continue


fac = 1
sum = 0

while num:
    for i in range(int(num)):
        sum += i + 1
        fac *= i + 1
        print("%d!=%d" % (i, fac))
    print(sum)
    break