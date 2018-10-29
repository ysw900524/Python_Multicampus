# 클래스 초기화 함수, __init__() 재정의
class MyClass:
    def __init__(self, name):       # init 함수가 있을 때는 객체 생성과 동시에 인스턴스화를 진행하는 것.

        self.name = name

    def sayHello(self):
        hello = "Hello, " + self.name + "\t It's Good day!"
        print(hello)

# 객체 생성, 인스턴스화
# myClass = MyClass()
myClass = MyClass('채영')
myClass.sayHello()

    # Hello, 채영	 It's Good day!