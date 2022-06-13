#리스트를 리터럴로 생성할 때는 대괄호 사용.
list_0 = [1, 2, 3, 4, 5]
print(list_0)

# 변수 = list(range(n)) : 0부터 1씩 증가되는 n개의 정수가 담긴 리스트를 생성.
list_1 = list(range(10))
print(list_1)

# 변수 = list(range(n, m)) : n부터 m까지 1씩 증가하는 정수가 담긴 리스트를 생성.
list_2 = list(range(1, 10))
print(list_2)

# 변수 = list(range(n, m, o)) n부터 m까지 o씩 감소하는 정수가 담긴 리스트를 생성.
list_3 = list(range(0, 10, 2))
print(list_3)
