# Documentation Strings (docstring)

def my_function():
    """ 아무것도 하지 않지만, 문서만 기술한 함수

    본 함수는 docstring을 설명하기 위한 함수로 아무 행위도 하지 않는다.
    """
    pass
    # return 123
# print(my_function())
print(my_function.__doc__)
    # __doc__을 붙여야지 문서 내용을 출력한다.
    # my_function()을 출력하는 경우에는 none값이 나온다. return값이 없기 때문.


# 문서화를 위한 문자열 활용
def introduce_your_family(name, *family_names, **family_info):
    '''
    가족을 소개하는 함수입니다.
    :param name: 자기이름 입력하기
    :param family_names: 가족이름 입력하기
    :param family_info: 가족소개하기
    :return: 없습니다.
    '''
    pass
    # '''을 치면 자동으로 인자들에 대한 설명을 쓸 수 있는 문장이 초록색으로(옵션 지정된 색)생성된다.


# def introduceMyFamily(my_name, *family_names, **family_info):       # *하나는 튜플형으로 데이터를 묶어오고, **는 사전형으로 묶어온다.
#     '''
#     :param my_name:
#     :param family_names:
#     :param family_info:
#     :return:
#     '''
#     print('안녕하세요. 저는 %s 입니다.'%(my_name))
#     print('-'*35)
#     print('제 가족들의 이름은 아래와 같아요. ')
#     for name in family_names:
#         print('* %s' %(name), end='\t')
#     else:
#         print()
#     print('-'*35)
#     for key in family_info.keys():          # .keys()는 딕셔너리 형태에서 쓰이는 함수이다.
#         print('- %s : %s ' %(key, family_info[key]))
#
# introduceMyFamily('진수', '희영', '찬영', '준영', '채영',
#                   주소='롯데캐슬', 가훈='극기상진', 소망='세계일주')

    # 함수를 실행하는 경우에는 ''' ''' 사이의 내용은 출력되지 않는다.