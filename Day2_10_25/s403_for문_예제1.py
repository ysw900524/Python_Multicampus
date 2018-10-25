# for 문

# range() 함수

result = list(range(10))
print('range(10)    :', result)

result = list(range(5, 10))
print('range(5, 10) :', result)

result = list(range(1, 10, 2))
print('range(1,10,2)):', result)
    # 1부터 10까지 2개 단위로 숫자 뽑아내는 것.

    # range(10)    : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # range(5, 10) : [5, 6, 7, 8, 9]
    # range(1,10,2)): [1, 3, 5, 7, 9]

scope = [1,2,3,4,5]

for x in scope:
    print(x)


scope = list('abcde')

for x in scope:
    print(x)