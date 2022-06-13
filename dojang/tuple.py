#튜플을 리터럴로 생성할 때는 소괄호 혹은 무괄호 사용.
tuple_1 = (49, 238, 3, 28, 160)
tuple_1 = 49, 238, 3, 28, 160
print(tuple_1)

# 변수 = tuple(range(n)) : 0부터 1씩 증가되는 n개의 정수가 담긴 튜플을 생성.
tuple_2 = tuple(range(10))
print(tuple_2)

# 변수 = list(range(n, m)) : n부터 m까지 1씩 증가하는 정수가 담긴 튜플을 생성.
tuple_3 = tuple(range(10, 20))
print(tuple_3)

# 변수 = list(range(n, m, o)) n부터 m까지 o씩 감소하는 정수가 담긴 튜플을 생성.
tuple_4 = tuple(range(10, 0, -2))
print(tuple_4)
