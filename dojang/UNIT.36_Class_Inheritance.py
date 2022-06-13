# class Person:
#   def greeting(self):
#     print('Hello')

# class Student(Person):
#   def study(self):
#     print('to Study')

# james = Student()
# james.greeting()
# james.study()
# print(issubclass(Student, Person))


# class PersonList():
#   def __init__(self):
#     self.person_list = []
#
#   def append_person(self, person):
#     self.person_list.append(person)

# 1. 상속 관계와 포함 관계 이해하기

class Person:
  def __init__(self):
    print('Person __init__')
    self.hello = 'Hello'


class Student(Person):
  def __init__(self):
    print('Student __init__')
    super().__init__()
    self.school = 'Python Coding Dojang'


james = Student()
print(james.school)
print(james.hello)
