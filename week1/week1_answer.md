# 답안지

- 코딩에는 정답이 없습니다!
- 하다가 궁금한 것이 있으면 저한테 찾아오세여

## 1-1

```python
# 의도한 답안
from random import randint

num1 = randint(1, 9)
num2 = randint(1, 9)
num3 = randint(1, 9)
num4 = randint(1, 9)
num5 = randint(1, 9)
num6 = randint(1, 9)

print(num1 + num2 + num3 + num4 + num5 + num6)

```

```python
# 꼼수
from random import randint

value = randint(1, 999999)

print(value)

```

## 1-2

```python
# while이나 for 반복문을 사용하는 것도 좋음
number = int(input(""))

print(number, "_ 1 =", number _ 1)
print(number, "_ 2 =", number _ 2)
print(number, "_ 3 =", number _ 3)
print(number, "_ 4 =", number _ 4)
print(number, "_ 5 =", number _ 5)
print(number, "_ 6 =", number _ 6)
print(number, "_ 7 =", number _ 7)
print(number, "_ 8 =", number _ 8)
print(number, "_ 9 =", number _ 9)
```

# 1-3

```python
# 원래 의도는 인터넷에서 random choice을 찾아보는 것이였음
# randint로 리스트 원소를 고른 것도 나쁘지 않음
import random

fruit_list = ["사과", "바나나", "포도", "오렌지", "키위"]

random_fruit = random.choice(fruit_list)

print(f"오늘의 과일은 {random_fruit}입니다")
```

# 1-4

```python
# 추가자료에 있던 replace()을 사용하면 그렇게 어렵지 않았음
# join 은... 정도는 잘 찾아서 했을것이라고 믿음
from random import randint

site_url = input("")

site_url.replace("https://", "")

site_url.replace(".com", "")

domain = site_url.join("")

print(domain)

sliced_domain = domain[:2]

len_of_word = len(sliced_domain)

random_num = randint(1, 999)

print(sliced_domain + str(len_of_word) + str(random_num) + "!")

```
