s = input('영어 대소문자로 이루어진 문장을 입력하세요.\n') # 문자열 입력

print('모두 대문자로 출력\n' + s.upper())               # 대문자로 모두 출력, s문장을 upper()함수로 대문자 변형

print('모두 소문자로 출력\n' + s.lower())               # 소문자로 모두 출력

new_s = str()                                         # 

for c in s:
    if c.islower():
        new_s += c.upper()
    else:
        new_s += c.lower()

print('대소문자 바꿔서 출력\n' + new_s)
print('대소문자 바꿔서 출력\n' + s.swapcase())

