# 튜플형, Tuple

# 튜플형 선언 및 인덱싱

# 튜플 생성(튜플형, Tuple type)
girl_group = ('트와이스', '레드벨벳', '에이핑크', '걸스데이', '우주소녀')
    # 리스트는 ['트와이스', '레드벨벳', ...] 의 형태이지만, 소괄호로 묶은 () 경우에는 튜플형이 되는 것이다.

print('girl_group   \t: ', girl_group)
print('girl_group[:2]\t: ', girl_group[:2])
print('girl_group[-2:]\t: ', girl_group[-2:])

    # girl_group   	:  ('트와이스', '레드벨벳', '에이핑크', '걸스데이', '우주소녀')
    # girl_group[:2]	:  ('트와이스', '레드벨벳')
    # girl_group[-2:]	:  ('걸스데이', '우주소녀')



# 튜플형 변경
# 튜플값 변경 시도, TypeError 발생
girl_group[2] = '블랙핑크'
    # 튜플 형태에서는 리스트처럼 변경하는 것이 안된다.(immutable이기 때문)

    #TypeError: 'tuple' object does not support item assignment


girl_group = list(girl_group)
girl_group[2] = '블랙핑크'
girl_group = tuple(girl_group)
print('girl_group   \t: ', girl_group)

    # girl_group   	:  ('트와이스', '레드벨벳', '블랙핑크', '걸스데이', '우주소녀')
