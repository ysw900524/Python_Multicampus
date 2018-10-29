# Scope of variable & global variable

# 지역변수와 전역변수
param = 10
strdata = '전역변수'

def func1():
    strdata = '지역변수'
    print('func1.strdata = %s, id = %d' %(strdata, id(strdata)))

def func2():
    param = 20
    print('func2.param = %d, id = %d' %(param, id(param)))

def func3():
    global param    #global 이라는 명령어로 전역변수로 변환시켜 준다.
    param = 30
    print('func3.param = %d, id = %d' %(param, id(param)))


func1()
print('main1.strdata = %s, id = %d' %(strdata, id(strdata)))

    # func1.strdata = 지역변수, id = 41210112
    # main1.strdata = 전역변수, id = 31481656

func2()
print('main2.param = %d, id = %d' %(param, id(param)))

    # func2.param = 20, id = 8791457445296
    # main2.param = 10, id = 8791457444976

func3()
print('main3.param = %d, id = %d' %(param, id(param)))

    # unc3.param = 30, id = 8791457445616
    # main3.param = 30, id = 8791457445616