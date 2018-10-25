# 중복 제거 및 정렬
beast = ["lion", "tiger", "wolf", "tiger", "lion", "bear", "lion" ]
print('beast =', beast)

unique_beast = list(set(beast))
print('unique_beast =', unique_beast)
sorted_beast = sorted(unique_beast)
print('sorted_beast =', sorted_beast)

    # beast = ['lion', 'tiger', 'wolf', 'tiger', 'lion', 'bear', 'lion']
    # unique_beast = ['tiger', 'wolf', 'lion', 'bear']
    # sorted_beast = ['bear', 'lion', 'tiger', 'wolf']
    