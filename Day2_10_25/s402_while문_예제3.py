# while 문
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
idx, sum = 0, 0

while idx < len(numbers):
    num = numbers[idx]
    sum += idx
    idx += 1
    # print('num = %d, sum = %d' %(num, sum))
    # => 만약 순차적으로 변화하는 값들을 확인하고 싶은 경우에는 수식 내에 print 함수를 활용해 넣어주면 된다.

print('numbers의 합계는 ', sum, '입니다.')


    # numbers의 합계는  45 입니다.
        # num = 0, sum = 0
        # num = 1, sum = 1
        # num = 2, sum = 3
        # num = 3, sum = 6
        # num = 4, sum = 10
        # num = 5, sum = 15
        # num = 6, sum = 21
        # num = 7, sum = 28
        # num = 8, sum = 36
        # num = 9, sum = 45
