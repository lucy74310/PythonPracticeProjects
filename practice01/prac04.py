# 문제4.
# 다음과 같은 출력이 되도록 구구단을 작성하세요. (이중 for~in)

for dan in range(1, 10):
    for gob in range(1, 10):
        print(dan, 'x', gob, '=', dan * gob, end='\t')
    print()