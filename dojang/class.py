# Class

# class FishCakeMaker:
#     def __init__(self, **kwargs):
#         self._size = 10
#         self._flavor = "팥"
#         self._price = 100
#         if "size" in kwargs:
#             self._size = kwargs.get("size")
#         if "flavor" in kwargs:
#             self._flavor = kwargs.get("flavor")
#         if "price" in kwargs:
#             self._price = kwargs.get("price")
        
#     def show(self):
#         print("붕어빵 종류 {}".format(self._flavor))
#         print("붕어빵 크기 {}".format(self._size))
#         print("붕어빵 가격 {}".format(self._price))
#         print("*" * 50)
    
# fish1 = FishCakeMaker()
# fish2 = FishCakeMaker(size=20, price=300)
# fish3 = FishCakeMaker(size=15, price=500, flavor="슈크림")

# fish1.show()
# fish2.show()
# fish3.show()

class Person():
    def greeting(self):
        print('안녕하세요')

class Student(Person):
    def greeting(self):
        super().greeting()
        print('저는 파이썬 코딩 도장 학생입니다.')

james = Student()
james.greeting()
