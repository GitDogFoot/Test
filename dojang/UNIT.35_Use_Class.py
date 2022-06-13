# class Person:
#   bag = []
#
#   def put_bag(self, stuff):
#     self.bag.append(stuff)
#
# james = Person()
# james.put_bag('책')
#
# maria = Person()
# maria.put_bag('열쇠')
#
# print(james.bag)
# print(maria.bag)


# 35.2 정적 메소드 사용하기
class Calc:
  @staticmethod
  def add(a, b):
    print(a + b)

  @staticmethod
  def mul(a, b):
    print(a * b)

Calc.add(10, 20)
Calc.mul(10, 20)


# 35.3 클래스 메소드 사용하기
class Person:
  count = 0

  def __init__(self):
    Person.count += 1

  @classmethod
  def print_count(cls):
    print('{0}명 생성됐습니다.'.format(cls.count))


james = Person()
maria = Person()

Person.print_count()


# 35.5 연습문제
class Date:
  @staticmethod
  def is_date_valid(date_string):
    year, month, day = map(int, date_string.split('-'))
    return month <= 12 and day <= 31


if Date.is_date_valid('2000-12-31'):
  print('올바른 날짜 형식입니다.')
else:
  print('잘못된 날짜 형식입니다.')


# 35.6 심사문제: 시간 클래스 만들기
class Time:
  def __init__(self, hour, minute, second):
    self.hour = hour
    self.minute = minute
    self.second = second

  @staticmethod
  def is_time_valid(time_string):
    hour, minute, second = map(int, time_string.split(':'))
    return hour <= 23 and minute <= 59 and second <= 59

  @classmethod
  def from_string(cls, time_string):
    hour, minute, second = map(int, time_string.split(':'))
    t = cls(hour, minute, second)
    return t


time_string = input()

if Time.is_time_valid(time_string):
  t = Time.from_string(time_string)
  print(t.hour, t.minute, t.second)
else:
  print('잘못된 시간 형식입니다.')
