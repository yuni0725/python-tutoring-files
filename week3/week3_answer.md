# 답안지

- 코딩에는 정답이 없습니다!
- 하다가 궁금한 것이 있으면 저한테 찾아오세여

## 3-1

```python
def reverse_string(text : str):
    text_list = list(text)
    text_list.reverse()

    text_reversed = ''.join(text_list)

    return text_reversed

text_inputed = input()

print(reverse_string(text_inputed))
```

## 3-2

```python
weight = int(input('체중 : '))
height = int(input('키 : ')) / 100

def cal_BMI(w, h):
    return w / (h**2)

def check_types(BMI):
    if BMI < 20:
        print('저체중')
    elif BMI >= 20 and BMI <= 24:
        print('정상')
    elif BMI >= 25 and BMI <= 29:
        print('과체중')
    else:
        print('비만')


check_types(cal_BMI(weight, height))
```

# 3-3

```python
def check_balance(balance):
    print(f'현재 계좌의 잔액은 {balance}원입니다.')

def withdraw_balance(balance):
    amount_of_money = int(input('인출하고 싶은 돈의 액수를 적어주세요 : '))
    if amount_of_money > balance:
        print('잔액이 부족합니다. 다시 시도해주세요.')
        return balance
    else:
        new_balance = balance - amount_of_money
        print(f'인출이 완료되었습니다. 현재 잔액은 {new_balance}입니다')
        return new_balance

def deposit_balance(balance):
    amount_of_money = int(input(f'입금하고 싶은 돈의 액수를 적어주세요 : '))
    new_balance = balance + amount_of_money
    print(f'입금이 완료되었습니다. 현재 잔액은 {new_balance}원입니다')

    return new_balance


balance = 0

while True:
    ans = input('은행 업무의 번호를 입력하세요. (잔액 확인 : 1, 인출하기 : 2, 입금하기 : 3, 종료하기 : 4) ')
    if ans == '1':
        check_balance(balance)

    elif ans == '2':
        balance = withdraw_balance(balance)

    elif ans == '3':
        balance = deposit_balance(balance)

    elif ans == '4':
        print('이용해주셔서 감사합니다')
        break

    else:
        print('잘못된 번호를 입력하셨습니다. 다른 번호를 입력해주세요.')
```
