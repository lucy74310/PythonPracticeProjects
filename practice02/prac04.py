# 문제4
# 반복문을 이용하여 369게임에서 박수를 쳐야 하는 경우의 수를 순서대로 화면에
# 출력해보세요. 1부터 99까지만 실행하세요.

for n in range(1, 100):
    s = str(n)
    c = s.count('3') + s.count('6') + s.count('9')
    clap = str()
    if c > 0:
        for c2 in range(0, c):
            clap += "짝"
        print(s, clap)
