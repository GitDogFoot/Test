import math

# class Point2D:
#   def __init__(self, x, y):
#     self.x = x
#     self.y = y
#
#
# p1 = Point2D(x=30, y=20)
# p2 = Point2D(x=60, y=50)
#
# print('p1: {} {}'.format(p1.x, p1.y))
# print('p2: {} {}'.format(p2.x, p2.y))
#
# a = p2.x - p1.x
# b = p2.y - p1.y
#
# c = math.sqrt((a * a) + (b * b))
# c = math.sqrt(math.pow(a, 2) + math.pow(b, 2))
# print(c)

# function abs(value) : 정수는 절댓값을 반환, 실수는 절댓값을 실수로 반환
# math.fabs(value) : 절댓값을 실수로 반환


# 37.2 연습문제: 사각형의 넓이 구하기
# class Rectangle:
#   def __init__(self, x1, y1, x2, y2):
#     self.x1 = x1
#     self.x2 = x2
#     self.y1 = y1
#     self.y2 = y2
#
#
# rect = Rectangle(x1=20, y1=20, x2=40, y2=30)
# width = abs(rect.x2 - rect.x1)
# height = abs(rect.y2 - rect.y1)
# area = width * height
# print(area)


# 37.3 심사문제: 두 점 사이의 거리 구하기
class Point2D:
  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y


length = 0.0
p = [Point2D(), Point2D(), Point2D(), Point2D()]
p[0].x, p[0].y, p[1].x, p[1].y, p[2].x, p[2].y, p[3].x, p[3].y = map(int, input().split())


for i in range(1, len(p)):
  length += math.sqrt(math.pow(abs(p[i].x - p[i-1].x), 2) + math.pow(abs(p[i].y - p[i-1].y), 2))

print(length)
