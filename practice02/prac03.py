# 문제3.
# 1)다음 문자열을 모든 소문자를 대문자로 변환하고,
# 문자 ',', '.','\n'를 없앤 후에 중복
# 없이 각 단어를 순서대로 출력하세요.
s = """We encourage everyone to contribute to Python. If you still have questions after reviewing the material
in this guide, then the Python Mentors group is available to help guide new contributors through the process."""
# print(s)

# print('--- . 제거---')
s = s.replace('.', '')
# print(s)

# print('--- ,제거 ---')
s = s.replace(',', '')
# print(s)

# print('--- \\n 제거 ---')
s = s.replace('\n', '')
# print(s)

wordList = s.upper().split(' ')
# 중복제거
wordSet = set(wordList)
# 정렬위해 list로
wordList = list(wordSet)
wordList.sort(key=str)

print('1)')

for wrd in wordList:
    print(wrd)

# 2)각 단어의 빈도수도 함께 출력해 보세요
print('\n2)')

wordList2 = s.upper().split(' ')
wordList2.sort(key=str)
d = dict()
for wrd in wordList2:
    if d.get(wrd) is None:
        d[wrd] = 0
    d[wrd] = d[wrd] + 1

keys = d.keys()
for k in keys:
    print('{}:{}'.format(k, d[k]))

