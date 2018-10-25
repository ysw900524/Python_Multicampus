# 문자형

# 이스케이프 문자
text1 = "안녕하세요!\n하나금융\t임직원 여러분!"
    # \t는 tab 기능과 같은 역할의 명령어다.

text2 = '''
빅데이터를 위한 파이썬과정에서
만나뵙게 되어 반갑습니다.
끝까지 '화이팅' 하세요!!!
'''
    # '''(3따옴표)는 블록주석을 설정할 때도 사용하지만, 문자열을 한번에 나타낼 때도 사용한다.

print(text1)
print(text2)

    # 안녕하세요!
    # 하나금융	임직원 여러분!
    #
    # 빅데이터를 위한 파이썬과정에서
    # 만나뵙게 되어 반갑습니다.
    # 끝까지 '화이팅' 하세요!!!




# 문자형 함수1
test = '파이썬 프로그래밍 재미있다!'        # 문자열을 변수에 저장

result = test.startswith('파이썬')         # 문자열이 '파이썬'으로 시작하는지 확인
print(result)
result = test.endswith('!')               # 문자열이 '!'로 끝나는지 확인
print(result)
result = test.endswith('어려워요!')         # 문자열이 '어려워요!'로 끝나는지 확인
print(result)
result = test.replace('파이썬', 'Python')  # 문자열 중 '파이썬'을 'Python'으로 변경
print(result)

    # True
    # True
    # False
    # Python 프로그래밍 재미있다!



# 문자형 함수2
test = 'Python Programming is Interesting!'

result = test.upper()       # 문자열을 모두 대문자로 변경
print(result)
result = test.lower()       # 문자열을 모두 소문자로 변경
print(result)
result = '/'.join(test)     # 문자열의 각 문자 사이에 '/' 문자 집어 넣기
print(result)

    # PYTHON PROGRAMMING IS INTERESTING!
    # python programming is interesting!
    # P/y/t/h/o/n/ /P/r/o/g/r/a/m/m/i/n/g/ /i/s/ /I/n/t/e/r/e/s/t/i/n/g/!
