# 세트형 집합 연산자
a = set('abracadabra')
b = set('alacazam')

print('집합 a =', a); print('집합 b =', b);
print('합집합, a | b =', a | b)
print('교집합, a & b =', a & b)
print('차집합, a - b =', a - b)
print('여집합, a ^ b =', a ^ b)


    # 집합 a = {'d', 'a', 'b', 'r', 'c'}
        # 순서가 d, a, b, r, c 등으로 나오는 이유는 set형은 순서가 중요하지 않기 때문이다.
    # 집합 b = {'l', 'a', 'z', 'm', 'c'}
    # 합집합, a | b = {'d', 'a', 'b', 'r', 'l', 'z', 'm', 'c'}
    # 교집합, a & b = {'a', 'c'}
    # 차집합, a - b = {'d', 'b', 'r'}
    # 여집합, a ^ b = {'d', 'l', 'b', 'r', 'z', 'm'}