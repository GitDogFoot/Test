# 세트 만들기
fruits = {'strawberry', 'grape', 'orange', 'pineapple', 'cherry'}
a = set('apple')
b= set(range(5))
c = set()
print(fruits, a, b, c)

# 특정 값 확인
print('grape' in fruits)
print('cherry' not in fruits)

# 세트 안에 세트를 넣으려면 frozenset()을 사용해야 함

# |, set.union(세트1, 세트2) = 합집합(or)
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a | b)
print(set.union(a, b))

# &, set.intersction(세트1, 세트2) = 교집합(and)
print(a&b)
print(set.intersection(a, b))

# -, set.difference(세트1, 세트2) = 차집합
print(a - b)
print(set.difference(a, b))

# ^, set.symmetric_difference(세트1, 세트2) = 대칭차집합
print(a^b)
print(set.symmetric_difference(a, b))

# 집합 연산 후 할당 연산자 사용하기(|=, &=, -=, ^=)
# 또는 .update(), .intersection_update(), .difference_update(), symmetric_difference()

# 부분집합과 상위집합 확인하기
# 현재세트 <= 다른세트 또는 현재세트.issubset(다른세트) == 현재세트가 다른 세트의 부분집합인지 확인
a = {1, 2, 3, 4}
print(a <= {1, 2, 3, 4})            # True
print(a.issubset({1, 2, 3, 4, 5}))  # True
print(a < {1, 2, 3, 4})             # False

# 현재세트 >= 다른세트 또는 현재세트.issuperset(다른세트) == 현재세트가 다른 세트의 상위집합인지 확인
a = {1, 2, 3, 4}
print(a >= {1, 2, 3, 4})            # True
print(a.issuperset({1, 2, 3, 4}))   # True

# 현재세트.isdisjoint(다른세트) == 세트가 겹치지 않는지 확인하기
a = {1, 2, 3, 4}
print(a.isdisjoint({5, 6, 7, 8}))

# .add() => 세트에 요소 추가하기
a = {1, 2, 3, 4}
a.add(5)
print(a)

# .remove() => 세트에 특정 요소 삭제하기. 해당 요소가 없을 경우 에러 발생.
a.remove(4)
print(a)

# .discard() => 세트에 특정 요소 삭제하기. 해당 요소가 없어도 에러 발생하지 않음.
a.discard(5)
print(a)

# .pop() => 세트에서 임의의 요소 반환과 동시에 삭제하기. 요소가 없을 경우 에러 발생.
a.pop()
print(a)

# .clear => 세트의 모든 요소를 삭제하기
a.clear()
print(a)