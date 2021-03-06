# Arbitrary Argument

# 가변 인자 리스트 활용

def introduceMyFamily(my_name, *family_names, **family_info):       # *하나는 튜플형으로 데이터를 묶어오고, **는 사전형으로 묶어온다.
    print('안녕하세요. 저는 %s 입니다.'%(my_name))
    print('-'*35)
    print('제 가족들의 이름은 아래와 같아요. ')
    for name in family_names:
        print('* %s' %(name), end='\t')
    else:
        print()
    print('-'*35)
    for key in family_info.keys():          # .keys()는 딕셔너리 형태에서 쓰이는 함수이다.
        print('- %s : %s ' %(key, family_info[key]))

introduceMyFamily('진수', '희영', '찬영', '준영', '채영',
                  주소='롯데캐슬', 가훈='극기상진', 소망='세계일주')
                # 이번 경우에는 처리에 필요한 값이 명확하기 때문에 실행되지만, 파이썬은 애매한 경우에는 무조건 오류를 띄우기때문에
                # 너무 맹신해서는 안된다.
                # *하나는 튜플형으로 데이터를 묶어오고, **는 사전형으로 묶어온다.
                # 함수 자체는 순서대로 인자들을 받아오므로 첫번째 '진수'를 name이 가져가고, 나머지를 family_names가 가져간다.
                # 마지막으로 주소='롯데캐슬' 과 같이 key값과 value값이 묶인 형태는 사전형으로 인식해 **의 family_info가 가져가는 것이다.



    # 안녕하세요. 저는 진수 입니다.
    # -----------------------------------
    # 제 가족들의 이름은 아래와 같아요.
    # * 희영	* 찬영	* 준영	* 채영
    # -----------------------------------
    # - 주소 : 롯데캐슬
    # - 가훈 : 극기상진
    # - 소망 : 세계일주