# 문제6.
# 키보드에서 정수로 된 돈의 액수를 입력 받아
# 오만 원권, 만원 권, 오천 원권, 천원 권, 500원짜리 동전,
# 100원짜리 동전, 50원짜리 동전, 10원짜리 동전, 1원짜리 동전
# 각 몇 개로 변환 되는지 작성하시오.
import sys

number = input('금액 :')

if 'exit' == number:
    sys.exit(0)

try:
    number = int(number)
except ValueError:
    print('{}는 정수가 아닙니다'.format(number))
    sys.exit(0)

오만 = divmod(number, 50000)
print('50000원 :', 오만[0], '개')

만 = divmod(오만[1], 10000)
print('10000원 :', 만[0], '개')

오천 = divmod(만[1], 5000)
print('5000원 :', 오천[0], '개')

천 = divmod(오천[1], 1000)
print('1000원 :', 천[0], '개')

오백 = divmod(천[1], 500)
print('500원 :', 오백[0], '개')

백 = divmod(오백[1], 100)
print('100원 :', 백[0], '개')

오십 = divmod(백[1], 50)
print('50원 :', 오십[0], '개')

십 = divmod(오십[1], 10)
print('10원 :', 십[0], '개')

오 = divmod(십[1], 5)
print('5원 :', 오[0], '개')

일 = divmod(오[1], 1)
print('1원 :', 일[0], '개')


