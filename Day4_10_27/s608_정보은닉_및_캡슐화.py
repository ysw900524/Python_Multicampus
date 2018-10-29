class MyFavorite:
    __hobby = '야구'
    __drink = '맥주'

    def get_hobby(self):
        return self.__hobby

    def get_drink(self):
        return self.__drink

    def set_hobby(self, hobby):
        self.__hobby = hobby

    def set_drink(self, drink):
        self.__drink = drink


myInfo = MyFavorite()
my_hobby = myInfo.get_hobby()
my_drink = myInfo.get_drink()
print('예전엔 %s를 좋아하고, %s를 즐겨마셨어요.'%(my_hobby, my_drink))

    # 예전엔 야구를 좋아하고, 맥주를 즐겨마셨어요.

# myInfo.__hobby = '골프'
# myInfo.__drink = '소주'
myInfo.set_hobby('골프')
myInfo.set_drink('소주')
my_hobby = myInfo.get_hobby()
my_drink = myInfo.get_drink()
print('지금은 %s를 좋아하고, %s를 즐겨마십니다.'%(my_hobby, my_drink))

    # 지금은 야구를 좋아하고, 맥주를 즐겨마십니다.