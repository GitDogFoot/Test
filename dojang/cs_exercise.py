mylist = [1,2,3,4,5,6,7,8,9,10,'python']
for n, i in enumerate(mylist):
    if type(i) == int and i % 2 == 0:
        mylist[n] = '짝수'
    elif type(i) == int and i % 2 != 0:
        mylist[n] = '홀수'
    else:
        mylist[n] = '숫자 아님'
print(mylist)

yourlist = [1,2,3,4,5,6,7,8,9,10,'python']
yourlist = ['짝수' if type(x) == int and x % 2 == 0 else '홀수' if type(x) == int and x % 2 != 0 else '숫자 아님' for x in yourlist]
print(yourlist)

greetings = ["안녕", "니하오", "곤니찌와", "올라", "싸와디캅", "헬로", "봉주르"]
i = 0
while i <= 6:
    print("%d번째 인사말 : " %i, greetings[i])
    i += 1

total = 0
for i in range(1, 1001, 2):
    total += i
print(total)

for i in 'python':
    if i != 'y':
        print(i.upper())
    else:
        print(i)

dic = {'a':1, 'b':2, 'c':3, 'd':4}
for k in dic:
	print("{",k,":",dic[k],"}")

my_dir1 = ['a.txt', 'b.doc', 'c.jpg', 'd.div']
my_dir2 = ['e.aux', 'f.kor', 'g.txt', 'h.bat']
my_dir3 = ['i.py', 'b.doc', 'c.jpg', 'd.div']

D = ['my_dir1', 'my_dir2', 'my_dir3']

# for d in D:
#     print(D)
#     for f in d:
#         print("D:\\{}\\{}".format(D, f))

for d in D:
    print(d)
    for f in eval(d):
        print(f)

x = list(range(1, 101))

for i in x:
    if i % 2 == 0 and i % 3 == 0:
        if i % 4 != 0:
            print(i, end=' ')

lists = list(range(1, 1000))
itli = iter(lists)
total = 0
while True:
    total += itli.__next__()
print(total)


