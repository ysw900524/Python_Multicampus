books = list()  # 책 목록 선언

# 책 목록 만들기
books.append({'제목': '파이썬 프로그램 ', '출판연도':'2016','출판사':'A','쪽수':'200','추천유무':False})
books.append({'제목': '플랫폼 비지니스 ', '출판연도':'2013','출판사':'B','쪽수':'580','추천유무':True})
books.append({'제목': '빅데이터 마케팅 ', '출판연도':'2014','출판사':'A','쪽수':'296','추천유무':True})
books.append({'제목': '외식경영 전문가 ', '출판연도':'2010','출판사':'B','쪽수':'526','추천유무':False})
books.append({'제목': '십억만 벌어보자 ', '출판연도':'2013','출판사':'A','쪽수':'248','추천유무':True})


for book in books:   # 책 한 권씩 꺼내기 위한 루프 선언
    print(book['제목'], book['출판사'])  # 책 한 권 데이터 출력



#1) 내가 읽은 책 중 250 쪽이 넘는 책의 제목으로 이루어진 리스트형 변수 many_pages를 만든다.
many_pages=list()   # 책 리스트 선언

for book in books:
    if int(book['쪽수']) >=250:
        many_pages.append(book['제목'])

print(many_pages)



#2) 내가 읽은 책 중 추천하고 싶은 책의 제목으로 이루어진 리스트형 변수 recommends를 만든다.
recommends=list()   # 책 리스트 선언

for book in books:
    if book['추천유무']== True:
        recommends.append(book['제목'])

print(recommends)



#3) 내가 읽은 책의 전체 쪽수를 담는 숫자형 변수 all_pages를 만든다.
all_pages = 0   # 전체 쪽수 변수 선언

for book in books:
    page = int(book['쪽수'])
    all_pages += page
    print(page, ":", all_pages)

print(all_pages)



#4) 내가 읽은 책의 출판사를 위한 세트 형 변수 pub_company를 만든다.
pub_company =set()  # 출판사 변수 선언

for book in books:
    com = (book['출판사'])
    pub_company.add(com)

print(pub_company)




print('쪽수가 250쪽 넘는 책 리스트: ', many_pages)
print('내가 추천하는 책 리스트: ', recommends)
print('내가 읽은 책 전체 쪽수: ', all_pages)
print('내가 읽은 책의 출판사 목록: ', pub_company)





######################################################################################################
# 강사님 풀이 1

many_page = list()
recommend = list()
all_page = int()
pub_companies = set()


for book in books:
    if int(book['쪽수']) > 250:
        many_page.append(book['제목'])
    if book['추천유무']:
        recommend.append(book['제목'])
    all_page = all_page + int(book['쪽수'])
    pub_companies.add(book['출판사'])

print('쪽수가 250쪽 넘는 책 리스트: ', many_pages)
print('내가 추천하는 책 리스트: ', recommends)
print('내가 읽은 책 전체 쪽수: ', all_pages)
print('내가 읽은 책의 출판사 목록: ', pub_companies)


# 강사님 풀이 2

many_page = [book['제목'] for book in books if int(book['쪽수'])> 250]
recommend = [book['제목'] for book in books if book['추천유무']]
pub_companies = {book['출판사'] for book in books }
all_page = sum([int(book['쪽수']) for book in books])

print(' ### 도서 목록 출력 내용 ### \n', '-'*90)
print(' 1. 쪽수가 250 쪽 넘는 책 리스트 :', many_page)
print(' 2. 내가 추천하는 책 리스트      :', recommend)
print(' 3. 내가 읽은 책 전체 쪽수       :', all_pages)
print(' 4. 내가 읽은 책의 출판사 목록    :', sorted(pub_company))

##주의!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 2번째 풀이를 해석하는 것이 가장 중요하다!!!!!!
# 파이썬이 간단한 언어라는 증거가 바로 풀이 2번이다!!!
# 변수를 지정해 주고 그것을 활용할 줄 아는 능력을 얻는 것이 중요하다.
