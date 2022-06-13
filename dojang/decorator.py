# 데코레이터 : 이미 작성된 코드에 새로운 기능을 추가하여 함수 기능을 확장시키는 개념
# 파이썬에서 함수는 일급 객체 취급. 클로저 사용. 함수 내 함수를 정의할 수 있음.

# def outer_function(msg):
#     def inner_function():
#         return "난 내부 함수인데 {} 메세지를 받았어".format(msg)
#     return inner_function

# c= outer_function("배고프다는")
# print(dir(c))
# print(len(c.__closure__))
# print(dir(c.__closure__[0]))
# print(c.__closure__[0].cell_contents)

import time

def time_checker(func):
    def inner_function(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print("함수 {} 동작 시간: {}".format(func.__name__, end_time-start_time))
        return result
    return inner_function

@time_checker
def test1():
    for _ in range(5):
        time.sleep(0.1)

@time_checker
def test2():
    for _ in range(3):
        time.sleep(0.1)

test1()
test2()

def login_required(func):
    def inner_function(*args, **kwargs):
        if not kwargs.get("in_login"):
            print("로그인이 안되서 수행할 수 없습니다")
            return "로그인이 필요한 페이지입니다."
        return func(*args, **kwargs)
    return inner_function

@login_required
def login():
    print("안녕")

def add_tag(new_args):
    def decorator(func):
        def wrapper(name):
            print(name)
            return "<{}>{}</{}>".format(new_args, func(name), new_args)
        return wrapper
    return decorator

@add_tag("html")
def test(msg):
    return "데코레이터 " + msg

print(test("왜 이렇게 쉽냐"))