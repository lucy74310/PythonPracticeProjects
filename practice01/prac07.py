# 문제 7.
# 키보드에서 5개의 정수를 입력 받아
# 리스트에 저장하고
# 평균을 구하는 프로그램을 작성하시오

inputData = list()

i = 0
while i < 5:
    n = input('>')
    try:
        n = int(n)
    except ValueError:
        print('{} 는(은) 정수가 아닙니다'.format(n))
        continue
    i += 1
    inputData.append(n)

print()
print('평균:', sum(inputData) / i)





