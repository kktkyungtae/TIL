input = '''
a b c d e f
| | | | | |
|-| | |-| |
| | |-| | |
| |-| | |-|
| | |-| | |
|-| | |-| |
| | | | | |
1 2 3 4 5 6
'''

ladder = [[j for j in i] for i in input.strip().split('\n')]
rows = len(ladder # 가로
cols = len(ladder[0])
#
# for i in range(0, cols, 2):
#     # 위치
#     p = i
#     for j in range(1, rows):
#         # 오른쪽에 - 가 있으면
#         if p + 1 < cols and ladder[j][p + 1] == '-':
#             p += 2
#         elif p - 1 >= 0 and ladder[j][p - 1] == '-':
#             p -= 2
#     print(ladder[0][i], '-', ladder[rows - 1][p])

print(rows)