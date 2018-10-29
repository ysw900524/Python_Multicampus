# Default Argument

def ordermenu(menu):
    print('손님, %s를 주문하였습니다.' %(menu))

ordermenu('카페모카')

    # 손님, 카페모카를 주문하였습니다.



#TypeError
#ordermenu()

    # Traceback (most recent call last):
    #   File "C:/Users/student/PycharmProjects/Multicampus/Day3_10_26/s502_디폴트.py", line 10, in <module>
    #     ordermenu()
    # TypeError: ordermenu() missing 1 required positional argument: 'menu'



# Default Argument
def orderCoffee(menu = '카페라떼'):
    print('손님, %s를 주문하였습니다.' %(menu))

orderCoffee()

    # 손님, 카페라떼를 주문하였습니다.