# 문제5.
# 주어진 리스트 데이터를 이용하여 3의 배수의 개수와 배수의 합을 구하여 출력형태와 같이 출력하세요.

data = list(range(1, 100))

count = 0
multiple3sum = 0
# multiple3list = []
for n in data:
    if n % 3 == 0:
        count += 1
        multiple3sum += n
        # multiple3list.append(n)


print('주어진 리스트에서 3의 배수의 갯수 =>', count)
print('주어진 리스트에서 3의 배수의 합 =>', multiple3sum)
# print(multiple3list)
