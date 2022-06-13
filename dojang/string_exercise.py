string = list(input().split())
count = int(0)

for i in string:
    i = i.strip(',.')
    if i == 'the':
        count += 1
        continue
    else:
      pass

print(count)
    
m = list(map(int, input().split(';')))
m.sort(reverse=True)
for i in m:
    print('{0:>9,}'.format(i))