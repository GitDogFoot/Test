# class Person:
#   def __init__(self, name, age, address):
#     self.hello = '안녕하세요'
#     self.name = name
#     self.age = age
#     self.address = address
#
#   def greeting(self):
#     print('{0} 저는 {1}입니다.'.format(self.hello, self.name))
#
#
# maria = Person('마리아', 20, '서울시 서초구 반포동')
# maria.greeting()

# 1. 위치 인수 사용하는 방법
# class Person:
#   def __init__(self, *args):
#     self.name = args[0]
#     self.age = args[1]
#     self.address = args[2]
#
# maria = Person(*['마리아', 20, '서울시 서초구 반포동'])

# 2. 키워드 인수 사용하는 방법
# class Person:
#   def __init__(self, **kwargs):
#     self.name = kwargs['name']
#     self.age = kwargs['age']
#     self.address = kwargs['address']
#
# maria1 = Person(name='마리아', age=20, address='서울시 서초구 반포동')
# maria2 = Person(**{'name': '마리아', 'age': 20, 'address': '서울시 서초구 반포동'})


# 인스턴스는 생성한 뒤에도 속성을 추가할 수 있다. __init__메소드가 아닌 다른 메소드에서도 속성을 추가할 수 있다. 단, 이때는 메소드를 호출해야 속성이 생성된다.
# __slots__ = ['attribute name'] 특정 속성만 허용하는 방법


# 34.3 비공개 속성 사용하기
# 메소드 이름에도 '__'을 붙이면 비공개 메소드가 된다.
# class Person:
#   def __init__(self, name, age, address, wallet):
#     self.hello = 'Hello'
#     self.name = name
#     self.age = age
#     self.address = address
#     self.__wallet = wallet
#
#   def pay(self, amount):
#     self.__wallet -= amount
#     print('이제 {0}원 남았네요.'.format(self.__wallet))
#
#
# maria = Person('마리아', 20, '서울시 서초구 반포동', 10000)
# maria.pay(3000)


#.34.5 연습문제
# class Knight:
#   def __init__(self, health, mana, armor):
#     self.health = health
#     self.mana = mana
#     self.armor = armor
#
#   def slash(self):
#     print('베기')

# x = Knight(health=542.4, mana=210.3, armor=38)
# print(x.health, x.mana, x.armor)
# x.slash()

# 34.6 심사문제(딩동댕)
class Annie:
  def __init__(self, health, mana, AP):
    self.health = health
    self.mana = mana
    self.AP = AP

  def tibber(self):
    print('티버: 피해량 {0}'.format(self.AP*0.65+400))


health, mana, AP = map(float, input().split())
x = Annie(health, mana, AP)
x.tibber()


