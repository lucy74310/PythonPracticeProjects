# 문제1. 키보드로 정수 수치를 입력 받아 그것이 3의 배수인지 판단 하세요
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

    if number % 3 == 0:
        print(number, '는 3의 배수입니다.')
    else:
        print(number, '는 3의 배수가 아닙니다.')

