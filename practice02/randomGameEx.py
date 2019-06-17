import random


min, max = 1, 100
i = 0
while True:
    n = random.randrange(max) + min
    i += 1
    if n == int(input('수 입력: ')):
        print(i, '번 만에 맞추셨습니다!')
        break

    print(n)
    # if 'y' != input('다시 하시겠습니까?(y/n) >> '):
    #     break


