# 문제5.
# 선택정렬(제자리 정렬 알고리즘)을 적용하는 코드를 완성하세요.
# 문제에 주어진 배열 [ 5, 9, 3, 8, 60, 20, 1 ] 를 크기 순서대로 정렬하여 다음과 같은 출력이 되도록 완성하는 문제입니다.

# 1. 버블정렬
arr = [5, 9, 3, 8, 60, 20, 1]

exenum = len(arr) - 1

for i in range(0, exenum):
    for j in range(0, exenum-i):
        if arr[j] < arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
    print(arr)

print(arr)

# sortMore = True
# while sortMore:
#
#     for i, ele in enumerate(arr):
#         if i > 0:
#             if arr[i-1] < ele:
#                 arr[i] = arr[i-1]
#                 arr[i-1] = ele
#
#     sortMore = False
#     for i, ele in enumerate(arr):
#         if i > 0:
#             if arr[i-1] < ele:
#                 sortMore = True
#                 break

# print(arr)


# 2. 선택정렬
arr = [5, 9, 3, 8, 60, 20, 1]