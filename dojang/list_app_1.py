# .append() => 리스트 끝에 요소 하나 추가하기
a = [10, 20, 30]
a.append(40)
print("a = ", a)
# 어떤 값이든(중복 허용) 리스트 맨 끝자리에 추가 됨

# 리스트 안에 리스트 추가하기
b = [10, 20, 30]
b.append([50, 60])
print("b = ", b)

# .extend() => 리스트 안에 여러 개의 요소 추가하기
c = [10, 20, 30]
c.extend([50, 60])
print("c = ", c)

# 리스트 자체를 추가할 수 있음
d = [70, 80, 90, 100]
c.extend(d)
print("c = ", c)

# .insert() => 리스트 특정 인덱스에 요소 추가하기
a.insert(2, 25) # 2번 인덱스에 25를 추가. 기존 2번 인덱스는 뒤로 밀려남
print("a = ", a)

# .insert() => 리스트 안에 리스트 추가 가능
c.insert(3, [40, 45])
print("c = ", c)

# 슬라이스를 이용한 리스트 추가
a[4:4] = [10, 35, 38]
print("a = ", a)

# .pop() => 리스트에서 특정 인덱스의 요소를 삭제하기
a.pop() # 값을 넣지 않을 경우 가장 끝자리 요소를 반환함과 동시에 삭제
print("a = ", a)

a.pop(6) # a = [10, 20, 25, 30, 32, 35]
print("a = ", a)

# .pop() 대신 del 사용 가능
del a[5] # a = [10, 20, 25, 30, 32]
print("a = ", a)

# .remove() => 리스트에서 특정 값을 찾아서 삭제하기
a.remove(10) # a[0]과 a[4] 중에서 앞에 있는 값을 삭제함. a = [20, 25, 30, 10]
print("a = ", a)

# 리스트에서 특정 값의 인덱스 구하기
n = a.index(25) # n == 1
print(n)

# 리스트에서 특정 값의 개수 구하기
a.append(25)
n = a.count(25) # n == 2
print(n)

# .reverse() => 리스트의 순서를 뒤집기
a.reverse()
print("a = ", a)

# .sort() or sort(reverse=False), .sort(reverse=True) => 값의 오름차순 혹은 내림차순으로 정렬하기
a.sort()
print("a = ", a)

# .clear() => 리스트의 모든 요소를 삭제하기
a.clear() # == del a[:]
print("a = ", a)

# 슬라이스로 리스트를 수정할 때 리스트 자체를 추가하면 .extend()와 같은 결과
b[len(b):] = [70, 80]
print("b = ", b)