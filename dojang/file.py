# 파일 읽기
file = open('Hello.txt', mode='w')
file.write('Hello world')
file.close()

# 파일 쓰기
file = open('Hello.txt', mode='r')
c = file.read()
print(c)
file.close()

# 자동으로 파일 객체 닫기
with open('Hello.txt', mode='r') as file:
    s = file.read()
    print(s)

# 리스트에 들어있는 문자열을 파일에 쓰기
li = ['Hi\n', 'Good\n', 'Morning\n']
with open('Hello.txt', mode='w') as file:
    file.writelines(li)

# 파일의 내용을 한줄씩 리스트로 가져오기
with open('Hello.txt', mode='r') as file:
    text = file.readlines()
    print(text)

# 파일의 내용을 한줄씩 읽기
with open('Hello.txt', mode='r') as file:
    line = None
    while line != '':
        line = file.readline()
        print(line.strip('\n'))

    line = 'a'

# # for 반복문을 이용하여 파일의 내용을 한줄씩 읽기
with open('Hello.txt', mode='r') as file:
    for line in file:
        print(line.strip('\n'))

# 객체를 파일에 저장하기
import pickle

name = 'PTH'
age = 33
address = '경기도 의정부시 신곡동'
scores = {'korean': 90, 'math': 95, 'english': 92, 'science': 90}

with open('PTH.p', 'wb') as file:
    pickle.dump(name, file)
    pickle.dump(age, file)
    pickle.dump(address, file)
    pickle.dump(scores, file)

# 파일에서 파이썬 객체 읽기
with open('PTH.p', 'rb') as file:
    name = pickle.load(file)
    age = pickle.load(file)
    address = pickle.load(file)
    scores = pickle.load(file)
    print(name)
    print(age)
    print(address)
    print(scores)