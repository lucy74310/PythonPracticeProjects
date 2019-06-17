# 문제4.
# 구구단 중에 특정 곱셈을 만들고 그 답을 선택하는 프로그램을 작성하는 문제입니다.
# 답을 포함하여 9개의 정수가 아래와 같은 형태로 출력되고 사용자는 답을 골라 입력하게 됩니다.
# 프로그램은 정답 여부를 다시 출력합니다.
import random
min, max = 1, 81


while True:
    dan = random.randrange(9)+1
    gob = random.randrange(9)+1
    n = dan * gob
    numlist = [random.randrange(max)+min for i in range(1, 9)]
    numlist.append(n)
    random.shuffle(numlist)
    print()
    print('{} x {} = ?'.format(dan, gob))

    for i, num in enumerate(numlist):
        print(num, end='\t')
        if i % 3 == 2:
            print()

    print()
    while True:
        answer = input('answer :')
        if n == int(answer):
            print('정답')
            print()
            break
        else:
            print('오답')
            print()

    if "n" == input('다음 문제를 푸시겠습니까? (y/n)'):
        break
