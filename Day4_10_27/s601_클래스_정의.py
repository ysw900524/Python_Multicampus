# 클래스 정의 : X(실패)
#
# class MyClass:
#     name = '희영'
#
#     def sayHello():
#         hello = "Hello, " + name + "\t It's Good day!"
#         return hello
#
# # 객체 생성, 인스턴스화
# myClass = MyClass()
# obj_name = myClass.name
# obj_method = myClass.sayHello()
#
# print('Object name  :', obj_name)
# print('Object method:', obj_method)

    # 오류 발생
    # Traceback (most recent call last):
    #   File "C:/Users/student/PycharmProjects/Multicampus/Day4_10_27/s601_클래스_정의.py", line 13, in <module>
    #     obj_method = myClass.sayHello()
    # TypeError: sayHello() takes 0 positional arguments but 1 was given


# 클래스 정의 : OK(성공)
class MyClass:
    name = '찬영'

    def sayHello(self):
        hello = "Hello, " + self.name + "\t It's Good day !"
        return hello
        # 클래스에서 함수 내 변수는 self가 들어간다.
        # self.name을 통해서 클래스 내의 name 변수값을 받아올 수 있게 된다.


# 객체 생성, 인스턴스화
myClass = MyClass()
obj_name = myClass.name
obj_method = myClass.sayHello()

print('Object name   :', obj_name)
print('Object method :', obj_method)

    # Object name   : 찬영
    # Object method : Hello, 찬영	 It's Good day !



## 참고
# 객체가 메모리에 올라가 있는 것은 클래스가 만든 구조에 따라 올라간다.
# 클래스가 만든 구조 속에 내용를 채워가는 과정을 인스턴스화라고 하는 것이다.(인스턴스화는 과정인 것)
# 그 과정을 통해 만들어진 결과물을 객체라고 하는 것이다.(객체는 결과물)



# 클래스 정의 : 심화
class MyClass:
    name = '찬영'
    gender = str()


    def sayHello(self):
        hello = "Hello, " + self.name + "\t It's Good day !"
        return hello
        # 클래스에서 함수 내 변수는 self가 들어간다.
        # self.name을 통해서 클래스 내의 name 변수값을 받아올 수 있게 된다.


# 객체 생성, 인스턴스화
myClass = MyClass()
obj_name = myClass.name
obj_method = myClass.sayHello()

print('Object name   :', obj_name)
print('Object method :', obj_method)