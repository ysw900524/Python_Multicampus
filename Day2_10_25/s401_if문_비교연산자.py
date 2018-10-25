# IF 문

# 조건값 : 비교연산자

# condition = True
condition = False

if condition:
    print("조건을 충족함, condition met")

if not condition:
    print("조건 충족 못함, condition not met")

    # 조건 충족 못함, condition not met


# if - elif - else
num_a = 100
num_b = 200

if num_a > num_b :
    print('숫자 A가 더 큰 수입니다.')
    max = num_a
elif num_a < num_b :
    print('숫자 B가 더 큰 수입니다.')
    max = num_b
else :
    print('숫자A와 숫자B는 같습니다.')
    # if-elif-else는 하나의 블록처럼 붙어야만 한다. 파이썬 내부로 정한 규칙임.
    # 주의!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # 비교연산자를 사용해 if-elif-else 구문을 쓰는 경우에는 비교 대상을 먼저 확인한 이후에
    # 비교범위가 작은 것부터 큰 순으로 가야지만 온전한 결과값을 얻을 수 있다.
    # 예를 들어 90점 이상은 A, 80점 이상은 B, 60점 이상은 D, ... 순으로 등급을 매긴다고 했을 때,
    # 90점부터 확인해 나가야지, 먼저 50>=점수 같이 넓은 범위부터 확인하면 먼저 확인한 상황에서 종료가 되어버린다.
    # 고로, 좁은 범위부터 확장해 나가야 하는것.

print('숫자A와 숫자B 중 최대값은', max, '입니다')

    # 숫자 B가 더 큰 수입니다.
    # 숫자A와 숫자B 중 최대값은 200 입니다
