# 문제10
# 숫자를 입력 받아서 아래와 같은 실행결과가 나타나도록 코드를 완성하세요.
import sys

while True:

    number = input('숫자를 입력하세요: ')

    if 'exit' == number:
        sys.exit(0)

    try:
        number = int(number)
    except ValueError:
        print('정수가 아닙니다.')
        continue

    s = 0
    mod = number % 2
    for i in range(1, number + 1):
        if i % 2 == mod:
            s += i

    print('결과 값 :', s)

