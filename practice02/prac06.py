# 문제6
# 숨겨진 카드의 수를 맞추는 게임입니다.
# 1-100까지의 임의의 수를 가진 카드를 한 장 숨기고
# 이 카드의 수를 맞추는 게임입니다.
# 화면과 같이 카드 속의 수가 57인 경우를 보면 수를 맞추는 사람이
# 40이라고 입력하면 "더 높게", 다시 75이라고 입력하면 "더 낮게" 라는 식으로
# 범위를 좁혀가며 수를 맞추고 있습니다.
# 게임을 반복하기 위해 y/n이라고 묻고 n인 경우 종료됩니다.

import random


def newgame(min, max):
    num = random.randrange(max)+min
    print('수를 결정하였습니다. 맞추어 보세요')
    return num


newGameStart = True
setMin, setMax = 1, 100

while True:
    if newGameStart:
        newGameStart = False
        n = newgame(setMin, setMax)
        c = 1
        printMinRange = setMin
        printMaxRange = setMax

    print('{}-{}'.format(printMinRange, printMaxRange))

    i = input('{}>>'.format(c))

    if i.isdecimal():
        c += 1
        i = int(i)
    else:
        print('정수를 입력해 주세요 ')
        continue

    if i < n:
        print('더 높게')
        printMinRange = i
    elif i > n:
        print('더 낮게')
        printMaxRange = i
    elif n == i:
        print('맞았습니다.')
        if 'y' == input('다시 하시겠습니까(y/n) >> '):
            newGameStart = True
            continue
        else:
            break
