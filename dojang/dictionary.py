# 딕셔너리는 중괄호( {'키: 값'} ) 사용.
# 키가 중복될 경우 뒤에 있는 값만 적용.
# 값에는 모든 자료형 사용 가능. 딕셔너리 안에 딕셔너리 삽입 가능.
# 단, 키에는 리스트와 딕셔너리를 사용할 수 없음.

lux = dict(health=490, mana=480, melee=550, armor=18.72)                            # 변수 = dict(키1=값1, 키2=값2 ...)
gnar = dict(zip(['health', 'mana', 'melee', 'armor'], [510, 100, 175, 32]))         # 변수 = dict(zip['키1', '키2' ...], [값1, 값2 ...])
lulu = dict([('health', 550), ('mana', 350), ('melee', 550), ('armor', 29)])        # 변수 = dict([('키1', 값1), ('키2', 값2], ...)
fizz = dict({'health': 570, 'mana': 317.2, 'melee': 0, 'armor': 22.41})             # 변수 = dict({'키1': 값1, '키2': 값2, ...})

print(lux)
print(gnar)
print(lulu)
print(fizz)

# 딕셔너리 키에 접근하기
print(lulu['armor'])

# 딕셔너리 키에 값 할당하기
lux['health'] = 1935
lux['mana'] = 879.5

# 딕셔너리에 없는 키를 할당하면 키가 추가되고 값이 할당 됨.
lux['attack'] = 53.5

print(lux)

# 딕셔너리에 없는 키를 가져올 순 없음.

# 딕셔너리에 키가 있는지 확인하기
print('health' in lux)

# 딕셔너리에 키가 없는지 확인하기
print('movement speed' in lux)

# 딕셔너리에 키 개수 구하기(키의 개수 = 값의 개수)
print(len(fizz))
