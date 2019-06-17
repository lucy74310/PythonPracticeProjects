# 문제2.
# range() 함수와 유사한 frange() 함수를 작성해 보세요. frange() 함수는 실수 리스트를 반환합니다.


# val ~ base 또는 base ~ val step 간격으로 증가하는 실수 리스트
def frange(val, base=0.0, step=0.1):
    if val < base:
        start = val
        stop = base
    else:
        start = base
        stop = val

    f = start
    r = [f]

    while f < stop:
        f += step
        f = round(f, 1)
        r.append(f)

    return r


print(frange(2))
print(frange(1.0, 2.0))
print(frange(1.0, 3.0, 0.5))
print(frange(6, 3.0, 0.2))
