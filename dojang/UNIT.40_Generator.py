def upper_generator(x):
  for i in x:
    yield i.upper()


fruits = ['apple', 'pear', 'grape', 'pineapple', 'orange']
for i in upper_generator(fruits):
  print(i, end=' ')

# 제너레이터 표현식
# 리스트는 '[]'를 사용해서 만들고 제너레이터는 '()'을 사용해서 만든다.
# 리스트는 처음부터 리스트의 요소를 만들지만 제너레이터 표현식은 필요할 때 요소를 만듬으로써 메모리를 절약할 수 있다.
