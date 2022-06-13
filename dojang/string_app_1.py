# 문자열 바꾸기
str = 'Hello, world'
print(str)
str = str.replace('world', 'Python')
print(str)

# 문자 바꾸기
str_ = str.maketrans('aeiou', '12345')
print('apple'.translate(str_))

# .split() => 문자열 분리하여 리스트로 만들기
print('apple pear grape pineapple orange'.split())

# ' '.join() => 구분자 문자열과 문자열 리스트 연결하기
print(' '.join(['apple', 'pear', 'grape', 'pineapple', 'orange']))
print('-'.join(['apple', 'pear', 'grape', 'pineapple', 'orange']))

# .upper() => 문자열을 모두 대문자로 변환하기
print(str.upper()) # == HELLO, PYTHON

# .lower() => 문자열을 모두 소문자로 변환하기
print(str.lower()) # == hello, python

# .lstrip() => 문자열의 왼쪽 공백 삭제하기(왼쪽에 문자가 있으면 안됨)
str = '    Python    \"'
print(str.lstrip())

# .rstrip() => 문자열의 오른쪽 공백 삭제하기
str = '\"    Python    '
print(str.rstrip())

# .strip() => 문자열의 양쪽 공백 삭제하기
str = '    Python    '
print(str.strip())

# .lstrip('문자'), .rstrip('문자') => 왼쪽, 오른쪽의 특정 문자 삭제하기
str = '! Python !'
print(str.lstrip('!'))
print(str.rstrip('!'))

# .strip('문자') => 문자열의 양쪽에 특정 문자 삭제하기
str = '!Python!'
print(str.strip('!'))

# .punctuation => 구두점을 간단하게 삭제하기
import string       # string 모듈 불러오기
str = '!@ #Hello, Python$ %^ '
str = str.strip(string.punctuation)
print(str)

# + ' ' = 공백까지 삭제하기 === str.strip(string.punctuation).strip()
str = str.strip(string.punctuation + ' ')
print(str)

# .ljust(), .rjust() => 문자열을 왼쪽, 오른쪽으로 정렬하기
print(str.ljust(20), end='')
print('<- 7 Blank Spaces')
print('7 Blank Spaces ->', end='')
print(str.rjust(20))

# .center() => 문자열을 가운데 정렬하기
print('(', str.center(20), ')')

# .center() => 문자열을 제외한 남는 공간이 홀수라면, 왼쪽에 공백이 한 칸  더 들어감
print('(', str.center(21), ')')

# .zfill() => 문자열 왼쪽에 0 채우기(오른쪽에 0 채우기는 없나?)
print('35'.zfill(4))
print('3.5'.zfill(6))
print('Hello'.zfill(10))

# .find() => 문자열에서 특정 문자(열) 위치 찾기(처음으로 찾은 문자(열)의 인덱스만 반환)
print('apple pineapple'.find('pl')) # == 2

# .find() => 찾는 문자(열)이 없을 경우 -1을 반환
print('apple pineapple'.find('xy'))

# .rfind() => 문자열의 오른쪽에서부터 특정 문자(열) 위치 찾기(처음으로 찾은 문자(열)의 인덱스만 반환)
print('apple pineapple'.rfind('pl')) # == 12

# .index() => 문자열에서 특정 문자(열) 위치 찾기(처음으로 찾은 문자(열)의 인덱스만 반환)
print('apple pineapple'.index('pl')) # == 2

# .index() => 찾는 문자열이 없을 경우 에러 발생
# print('apple pineapple'.index('xy')) => syntax error

# .rindex() => 문자열의 오른쪽에서부터 특정 문자(열) 위치 찾기(처음으로 찾은 문자(열)의 인덱스만 반환)
print('apple pineapple'.rfind('pl')) # == 12

# .count() => 문자열에서 특정 문자(열)의 개수 세기
print('apple pineapple'.count('pl')) # == 2