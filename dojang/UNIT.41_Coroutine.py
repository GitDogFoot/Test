# def number_coroutine():
#   while True:
#     x = (yield)
#     print(x)
#
#
# co = number_coroutine()
# next(co)
#
# co.send(1)
# co.send(2)
# co.send(3)

import os
from django.utils import timezone
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Practice.settings")


def test():
  print('test')


if __name__ == '__main__':
  test()

print(timezone.localtime())
