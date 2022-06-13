a = ['alpha', 'bravo', 'chalie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel', 'india']
b = [i for i in a if len(i) == 5]
print(b)

n, m = map(int, input().split())
x = list(range(n, m+1))
y = []

for i in x:
    if i == x[1] or i == x[-2]:
        continue
    else:
        y.append(2**i)

print(y)
