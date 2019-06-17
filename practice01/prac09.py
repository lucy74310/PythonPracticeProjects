# 문제9.
# 주어진 if 문을 dict를 사용해서 수정하세요.

price = dict(오뎅=0, 순대=0, 만두=0)

# print(price)
menu = input('메뉴: ').strip()


if menu == '오뎅':
    price['오뎅'] = 300
elif menu == '순대':
    price['순대'] = 400
elif menu == '만두':
    price['만두'] = 500
else:
    price[menu] = 0


print('가격: {0}'.format(price[menu]))

