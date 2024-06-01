# 답안지

- 코딩에는 정답이 없습니다!
- 하다가 궁금한 것이 있으면 저한테 찾아오세여

## 2-1

```python
# 숫자를 입력받아서 if문을 사용해서 판별하면 됨
num = int(input('정수를 입력하세요 : '))

if num > 0:
    print('이 숫자는 0보다 큽니다.')

elif num < 0:
    print('이 숫자는 0보다 작습니다.')

else:
    print('이 숫자는 0입니다.')

```

## 2-2

```python
# 정수를 입력받고 for 문을 활용하면 됨
number = int(input(''))

for i in range(1, number+1):
    print(i)
```

# 2-3

```python
# 리스트를 활용한 for문을 사용하면 됨
items = ['사과', '바나나', '체리']

for item in items:
    print(f'나는 {item}를 좋아해!')
```

# 2-4

```python
# 온도와 비가 오는지 안오는지 and 연산자를 활용하면 됨

temp = int(input('온도를 입력하세요 (예 : 24) : '))
rainy = int(input('비가 오나요? (y / n) : '))

if rainy == 'y':
    print('우산을 챙기세요!')
elif temp >= 20 and rainy == 'n':
    print('야외에서 운동하기 좋은 날입니다!')
elif temp < 20 and rainy == 'n':
    print('실내에서 책 읽기 좋은 날입니다!')
```

# 2-5

```python
# 팩토리얼을 구할려면 range 함수를 쓰면 되겟죠
num = int(input())

fact = 1
for i in range(1, num + 1):
    fact *= i

print(fact)
```

# 2-6

```python
# 짝수를 판별할려면 2로 나누었을때 나머지가 0이면 된다. 나머지를 구하는 연산자는 %이다

n = int(input())

for i in range(1, n+1):
    if i % 2 == 0:
        print(i)
        continue
```

# 2-7

```python
# 팩토리얼을 구할려면 range 함수를 쓰면 되겟죠
# 뭔가 똑같은거 같은데 하면 조용히 넘어가..ㅎㅎ...
num = int(input())

fact = 1
for i in range(1, num + 1):
    fact *= i

print(fact)
```

# 2-8

```python
n1 = int(input())
n2 = int(input())

bool1 = n1 % n2 == 0
bool2 = n2 % n1 == 0

if bool1 or bool2:
    print(True)
else:
    print(False)
```

# 2-9

```python
N = int(input())

boolean = True

for i in range(2, N):
    if N % i == 0:
        boolean = False

print(boolean)

```

# 2-10

```python
from random import randint

num = randint(1, 100)

while True:
    answer = int(input('숫자를 맞춰보세요 : '))
    if answer > num:
        print('다운')
    elif answer < num:
        print('업')
    else:
        print('정답입니다!')
        break

```
