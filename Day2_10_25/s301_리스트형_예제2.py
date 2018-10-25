# 리스트형 추가/삭제
sistar_members = ['효린', '소유']
print('씨스타 \t:', sistar_members)

sistar_members.append('다솜')
print('append \t:', sistar_members)
sistar_members.insert(1, '보라')
print('insert \t:', sistar_members)

sistar_members.remove('소유')
print('remove \t:', sistar_members)

pickup = sistar_members.pop(0)
print('pop  \t:', sistar_members, end=' --> ')      #end-' --->' 요소를 넣어줌으로써, default가 \n으로 되어있어 줄이 바뀌는 결과값을 끝에 붙이는 것으로 변환시킨 것이다.
print(pickup)

    # 씨스타 	: ['효린', '소유']
    # append 	: ['효린', '소유', '다솜']
    # insert 	: ['효린', '보라', '소유', '다솜']
    # remove 	: ['효린', '보라', '다솜']
    # pop  	: ['보라', '다솜'] --> 효린
