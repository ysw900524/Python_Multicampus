# 상속, Inheritance

# 부모클래스, Animal
class Animal:
    tribe = '동물'
    def __init__(self, name):
        self.name = name

    def getInfo(self):
        print("나는", self.tribe, self.name, '입니다.')

# Animal의 자식클래스, Carnivore 클래스
class Carnivore(Animal):
    def __init__(self, name):
        self.name = name
        self.tribe = '육식동물'

    def favoriteFood(self):
        print('나는 고기를 좋아합니다.')

# Animal의 자식클래스, Herbivore 클래스
class Herbivore(Animal):
    def __init__(self, name):   # 호랑이 => name / init 함수의 name 변수를 의미함을 알아야 함.
        self.name = name
        self.tribe = '초식동물'

    def favoriteFood(self):
        print('나는 풀을 좋아합니다.')


print('-'*50, "\n[Carnivore 객체 생성]")
tiger = Carnivore('호랑이')    # 호랑이 => name / init 함수의 name 변수를 의미함을 알아야 함.
tiger.getInfo()
tiger.favoriteFood()

print('-'*50, '\n[Herbivore 객체 생성]')
rabit = Herbivore('토끼')
rabit.getInfo()
rabit.favoriteFood()


    # --------------------------------------------------
    # [Carnivore 객체 생성]
    # 나는 육식동물 호랑이 입니다.
    # 나는 고기를 좋아합니다.
    # --------------------------------------------------
    # [Herbivore 객체 생성]
    # 나는 초식동물 토끼 입니다.
    # 나는 풀을 좋아합니다.