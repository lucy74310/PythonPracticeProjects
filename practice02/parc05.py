# 문제5.
# 함수 sum 을 만드세요. 이 함수는 임의의 개수의 인수를 받아서 그 합을 계산합니다.


def sum(*nums):
    s = 0
    for n in nums:
        s += n
    return s


print(sum(1, 3, 5, 7, 9))
