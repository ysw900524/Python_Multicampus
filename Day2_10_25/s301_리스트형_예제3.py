# 리스트 슬라이싱
rainbow = ['빨강', '주황', '노랑', '초록', '파랑', '남색', '보라']
print('\n무지개색깔 \t :', rainbow)

result = rainbow[2:5]
print('rainbow[2:5] :', result)
    # 주의! list를 슬라이싱 하는 경우에, 2:5에서 2번째부터 (5-1)번째까지를 자른다.
    # end-1의 index값까지 추출하니 주의할 것!!!

result = rainbow[:3]
print('rainbow[ :3] :', result)

result = rainbow[:]
print('rainbow[ : ] :', result)

result = rainbow[::2]
print('rainbow[::2] :', result)
    # ::의 경우에는 뒤의 숫자만큼 건너뛴 위치의 값들을 잘라낸다.
    # 빨강 다음 2번째 자리의 노랑 그다음 두번째 자리의 파랑 다음 2번째의 보라를 자르는 것.

result = rainbow[-3:]
print('rainbow[-3: ] :', result)

result = rainbow[::-1]
print('rainbow[::-1] :', result)
    # -를 붙이면 역순으로 1번째 자리의 값들을 모두 잘라내는 것.

    # 무지개색깔 	 : ['빨강', '주황', '노랑', '초록', '파랑', '남색', '보라']
    # rainbow[2:5] : ['노랑', '초록', '파랑']
    # rainbow[ :3] : ['빨강', '주황', '노랑']
    # rainbow[ : ] : ['빨강', '주황', '노랑', '초록', '파랑', '남색', '보라']
    # rainbow[::2] : ['빨강', '노랑', '파랑', '보라']
    # rainbow[-3: ] : ['파랑', '남색', '보라']
    # rainbow[::-1] : ['보라', '남색', '파랑', '초록', '노랑', '주황', '빨강']
