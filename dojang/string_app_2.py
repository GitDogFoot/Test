# 문자열 서식 지정자와 포매팅(formating) 사용하기

# %s => 문자열
print('I am %s ' % 'TaeHun')

nation = 'Korea'
print('I live in %s' % nation)

# %d => 숫자(정수)
print('I am %d years old' % 33)

# %f => 숫자(소수)
height = 170.9
print('My height is %.1fcm' % height)

# %길이s => 길이만큼 문자 생성(오른쪽 정렬)
print('%10s' % 'Python')

# %-길이s => 길이만큼 문자 생성(왼쪽 정렬)
print('%-10s' % 'Python')

# 서식 지정자로 문자열 안에 값 여러 개 넣기
print('Today is %d %s' % (16, 'February'))

# .format => 포매팅(문자(열) 대체) 사용하기
print('Hello, {0}'.format('world'))
print('Today is the {0}th'.format(16))

# .format => 포매팅으로 여러 개의 값 넣기
print('Hello, {0} {2} {1}'.format('Python', 'Script', 3.8))

# .format => 같은 값을 여러 개 넣기
print('Hello {0} {1}, Hello {0} {1}'.format('Python', 'Script'))

# .format => 인덱스 지정하지 않을 경우엔 순서대로 들어감
print('Hello, {} {} {}'.format('Python', 3.8, 'Script'))

# .format('키'='값') => 인덱스 대신 이름 지정하기
print('Hello, {language} {version}'.format(language='Python', version=3.8))

# Python 3.6 이상에서 가능한 간단한 방법
language = 'Python'
version = 3.8
print(f'Hello, {language} {version}')

# .format 함수로 문자열 정렬하기
print('{0:<10}'.format('Python'), '<-|') # 0이라면 생략 가능('{:<10}')
print('|->', '{0:>10}'.format('Python')) # 0이라면 생략 가능('{:>10}')

# 숫자 자리수 맞추기
print('%03d' % 1)                   # == 001
print('{0:05d}'.format(35))         # == 00035
print('%08.2f' % 92)                # == 00009.20
print('{0:08.2f}'.format(150.37))   # == 00150.37

# 자릿수 맞추기와 정렬을 조합해서 사용하기
print('{0:0<10}'.format(15))
print('{0:0>10}'.format(15))
print('{0:0>10.2f}'.format(15))
print('{0: >10}'.format(15))
print('{0:<10}'.format(15))
print('{0:x>10}'.format(15))

# 천 단위로 콤마 넣기
print(format(1493500, ','))
print('{0:,}'.format(3721500))