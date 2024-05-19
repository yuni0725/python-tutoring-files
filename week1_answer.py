#1-1 

from random import randint

num1 = randint(1, 9)
num2 = randint(1, 9)
num3 = randint(1, 9)
num4 = randint(1, 9)
num5 = randint(1, 9)
num6 = randint(1, 9)

print(num1 + num2 + num3 + num4 + num5 + num6)

# ======================

from random import randint

value = randint(1, 999999)

print(value)

# 1-2

number = int(input(""))

print(number, "* 1 =", number * 1)
print(number, "* 2 =", number * 2)
print(number, "* 3 =", number * 3)
print(number, "* 4 =", number * 4)
print(number, "* 5 =", number * 5)
print(number, "* 6 =", number * 6)
print(number, "* 7 =", number * 7)
print(number, "* 8 =", number * 8)
print(number, "* 9 =", number * 9)

# 1-3

import random

fruit_list = ["사과", "바나나", "포도", "오렌지", "키위"]

random_fruit = random.choice(fruit_list)

print(f"오늘의 과일은 {random_fruit}입니다")

# 1-4
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


