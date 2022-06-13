# 가장 기본적인 요소 출력하기
a = [58, 39, 12, 92, 100]

for i in a:
    print(i)

# 인덱스와 요소를 같이 출력하기
for index, value in enumerate(a):
    print("a[", index, "] =", value)

print("--------------")

# 인덱스를 특정 숫자부터 출력하기
for index, value in enumerate(a, start=2):
    # enumerate(a, 2)로 줄여서 사용 가능
    print("a[",index,"] =", value)

# min(), max() => 가장 작은 값과 가장 큰 값 출력하기
print(min(a))
print(max(a))

# sum() => 요소의 합계 출력하기
print(sum(a))

# list comprehension 컴프리헨션 = 리스트 표현식
a = [i for i in range(2, 11) if i % 2 == 0]
print(a)

# 리스트에 map 사용하기. 요소의 실수값을 정수로 변환하기.
a = [1.5, 2.2, 3.6, 4.9, 5.1]
a = list(map(int, a))
print(a)

# map을 사용하여 언패킹하기
x = input().split()
m = map(int, x)
a, b = m
print(a)
print(b)