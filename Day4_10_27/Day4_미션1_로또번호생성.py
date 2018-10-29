# 미션 1

# 로또 번호를 자동으로 생성해서 출력
    # 주문한 개수만큼 N개의 로또 번호 출력
# Hint : 랜덤 숫자 생성
#     import random
#     random.randint(num1, num2) # num1~num2까지의 정수 생성
#

    # Ex. dice.py
    # import random
    #
    # dice_num = random.randint(1, 6)
    # print('주사위:'. doce_num)

import random


# class Lotto:
#     nums = set()
#
#     def select(self, num):
#         while len(num) <= 7:
#             num.add(random.randint(1,45))
#             print(num)
#


# class Lotto:
#     nums = set()
#
#     def __init__(self, num):
#         while len(num) <= 7:
#             self.nums.add(random.randint(1,45))
#
#     def select(self):
#
#
# mylotto = Lotto()
# my_lotto = mylotto.select()
# print(my_lotto)


class Lotto:
    final = list()

    def select(self, n):
        for i in range(n):
            nums = set()
            while len(nums) <= 6:
                num = random.randint(1, 45)
                nums.add(num)
            self.final.append(nums)
        return self.final


try1 = Lotto()
x = try1.select(4)
print(x)

