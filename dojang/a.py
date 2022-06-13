# 리스트가 비어있는지 확인하기
# if not seq:               리스트가 비어 있으면 True
# if seq:                   리스트에 내용이 있으면 True

# 리스트가 비어 있을 경우 인덱스를 -1로 지정하면 에러가 발생한다.

# 리스트의 요소 출력하기
a = [1,2,[3,4,5],6,7]

# for i in a:
#     print(i)

for index, value in enumerate(a, 1):
    print(index, value)

# while 반복문으로 요소 출력하기
a = [38, 21, 45, 81, 92]
i = 0
while i < len(a):
    print(a[i])
    i += 1
