# 문제2. 키보드로 정수 수치를 입력 받아 짝수인지 홀수 인지 판별하는 코드를 작성하세요.
import sys

while True:
    number = input('수를 입력하세요 (종료를 원하시면 exit을 입력하세요) :')

    if 'exit' == number:
        sys.exit(0)

    try:
        number = int(number)
    except ValueError:
        print('{}는 정수가 아닙니다'.format(number))
        continue

    if number % 2 == 1:
        print('{}는 홀수 입니다.'.format(number))
    else:
        print('{}는 짝수 입니다.'.format(number))
