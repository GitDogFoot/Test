# 딕셔너리에 키-값 쌍 추가하기
# .setdefault() => 키만 추가하면 값으로 'None'가 삽입
D = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
D.setdefault('e', )
print(D)

# .update() => 키의 값 수정하기
D.update(a=5)
print(D)

# .update() => 키가 존재하지 않는 경우 키와 값이 같이 추가
D.update(f=60)
print(D)

# .update() => 여러 개의 쌍을 콤마로 구분해서 수정 가능
D.update(a=10, e=50)
print(D)

# .update() => 키가 숫자일 경우에는 중괄호 추가
d = {1: 'One', 2: 'Two'}
d.update({3: 'Three'})
print(d)

# .update() => 리스트와 튜플을 이용하여 키-값 쌍 추가하기. 튜플도 같은 방식
d.update([[2, 'TWO'], [4, 'FOUR']])
print(d)

# zip 객체 이용하기
d.update(zip([5, 6], ['Five', 'Six']))
print(d)

# .setdefault() 와 .update()의 차이
# .setdefault()는 키-값 쌍 추가만 할 수 있고 키의 값만 수정하는 것은 불가능
# .update()는 키-값 쌍 추가와 값만 수정하는 것 이 가능

# .pop() => 키-값 쌍 삭제하기
d.pop(6)
print(d)

# .pop('키', 기본값) => 키가 있을 때는 해당 키-값 쌍 삭제하지만 없을 때는 기본값 반환
print(d.pop(6, 0))  # == 0. 키 6이 없기 때문에.

# del 객체[키] => 키-값 쌍 삭제하기
del d[5]
print(d)

# .popitem() => 임의의 키-값 쌍 삭제하기. 파이썬 3.6에서는 맨 끝에 있는 쌍 삭제함
d.popitem()
print(d)

# .clear() => 모든 키-값 쌍 삭제하기
d.clear()
print(d)

# .get() => 키의 값 가져오기
# .get(키, 기본값) => 키의 값을 가져오고 없을 때는 기본값 반환
d = {'a': 10, 'b': 20, 'c': 30, 'd':40}
print(d.get('a'))
print(d.get('e', 0))

# .items() => 키-값 쌍을 모두 가져오기
# .keys() => 키만 가져오기
# .values() => 값만 가져오기
print(d.items())
print(d.keys())
print(d.values())

# .fromkeys() => 리스트와 튜플로 딕셔너리 만들기
keys = ['A', 'B', 'C', 'D']
d= dict.fromkeys(keys)
print(d)

# .fromkeys(키리스트, 값) => 키 리스트에서 키를 가져오고 값은 모두 같은 값 할당
d = dict.fromkeys(keys, 100)
print(d)

# .defaultdict() => 존재하지 않는 키에 접근할 때 기본값 반환
from collections import defaultdict
d = defaultdict(int)                    # d의 기본값 설정 int => 0
print(d['z'])
