a = [0, 0, 0, 0, 0]
b = a

print(a is b)

# 리스트의 a와 b는 같은 객체
# 리스트에 값을 수정해보면 a와 b 둘 다 적용

a[1] = 1
print("a = ", a)
print("b = ", b)

# a와 b를 다른 객체로 만드려면 .copy()를 사용

a = [0, 1, 2]
b = a.copy()
print("a = ", a)
print("b = ", b)

print(a is b) # copy()를 사용했으므로 다른 객체. False.
print(a == b) # == 연산자는 True.

a.append(3)
print("a = ", a)
print("b = ", b)
