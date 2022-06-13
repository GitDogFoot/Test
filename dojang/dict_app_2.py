# 반복문으로 키 출력하기
d = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
for i in d:
    print(i, end=' ')

print()

# 반복문으로 키-값 쌍 출력하기

for key, value in d.items():
    print(key, value)
