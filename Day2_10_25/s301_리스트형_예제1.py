## 데이터 구조 Data structure

# 리스트형 선언 및 인덱싱

    # R의 경우 리스트는 1부터 시작하는데,(R이 특이한 것이며 보통의 프로그램 언어들은 인덱스 번호가 0부터 시작된다.)
    # 파이썬은 index 번호가 0부터 시작된다.
    # 고로, 전체 변수길이가 7인 리스트에서 마지막 변수의 인덱스값은 7-1인 6이 되며, 첫번째 변수는 0의 인덱스 값을 가진다.

# 리스트형 선언 및 색인
bts_members = ['RM', '슈가', '진', '제이홉', '지민', '뷔', '정국']

# 변수의 타입 확인
print('멤버 :', bts_members)
print('타입 :', type(bts_members))
print('크기 :', len(bts_members))

    # 멤버 : ['RM', '슈가', '진', '제이홉', '지민', '뷔', '정국']
    # 타입 : <class 'list'>
    # 크기 : 7

print('리스트멤버 호출')
print(bts_members[0])
print(bts_members[1])
print(bts_members[2])
print(bts_members[3])

    # 리스트멤버 호출
    # RM
    # 슈가
    # 진
    # 제이홉

print('리스트멤버 호출(역순)')
print(bts_members[-1])
print(bts_members[-2])
print(bts_members[-3])
print(bts_members[-4])
    # 음수로 지정해주는 경우 역순으로, 즉 뒤에서부터 시작된 숫자를 의마하므로 주의!

    # 리스트멤버 호출(역순)
    # 정국
    # 뷔
    # 지민
    # 제이홉