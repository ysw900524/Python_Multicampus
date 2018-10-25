# 리스트 응용

solarsys = ['태양', '수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '해왕성', '지구']
print('태양계 :', solarsys)

    # 태양계 : ['태양', '수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '해왕성', '지구']


# 리스트에서 특정 요소의 위치 구하기(index)
planet = '지구'
pos = solarsys.index(planet)
print('%s 행성은 태양계에서 %d 번째에 위치하고 있습니다.' %(planet, pos))
pos = solarsys.index(planet, 5)
print('%s 행성은 태양계에서 %d번째에 위치하고 있습니다.' %(planet, pos))
    # index 값이 5인 위치부터 시작해서 '지구'라는 값이 어느 위치에 있는지를 찾아내게 된다.
    # 9번 자리에 있는 '지구'의 위치를 찾아내는 것이다.

    # 지구 행성은 태양계에서 3 번째에 위치하고 있습니다.
    # 지구 행성은 태양계에서 9번째에 위치하고 있습니다.


# 리스트에서 특정 위치의 요소를 변경하기
solarsys.pop(-1)
print('태양계 :', solarsys)

planet = '화성'
pos = solarsys.index(planet)
solarsys [pos] = 'Mars'
print('태양계 :', solarsys)

    # 태양계 : ['태양', '수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '해왕성']
    # 태양계 : ['태양', '수성', '금성', '지구', 'Mars', '목성', '토성', '천왕성', '해왕성']


# 리스트에서 특정 구간에 있는 요소 추출하기
solarsys = ['태양', '수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '해왕성']
rock_planets = solarsys[1:5]
gas_planets = solarsys[5: ]

print('암석형 행성: ', end=""); print(rock_planets);
print('가스형 행성: ', end=""); print(gas_planets);

    # 암석형 행성: ['수성', '금성', '지구', '화성']
    # 가스형 행성: ['목성', '토성', '천왕성', '해왕성']


# 리스트의 특정 위치에 요소 삽입하기(insert)
solarsys = ['태양', '수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '해왕성']
pos = solarsys.index('목성')
solarsys.insert(pos, '소행성')
print('태양계: ', solarsys)

    # 태양계:  ['태양', '수성', '금성', '지구', '화성', '소행성', '목성', '토성', '천왕성', '해왕성']
