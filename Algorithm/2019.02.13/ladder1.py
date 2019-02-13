# [제약 사항]
# 한 막대에서 출발한 가로선이 다른 막대를 가로질러서 연속하여 이어지는 경우는 없다.
#
# [입력]
# 입력 파일의 첫 번째 줄에는 테스트 케이스의 번호가 주어지며, 바로 다음 줄에 테스트 케이스가 주어진다.
# 총 10개의 테스트 케이스가 주어진다.
#
# [출력]
# #부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 도착하게 되는 출발점의 x좌표를 출력한다.


# import sys
# sys.stdin= open("ladder1.txt","r")
#
# T = int(input())
# x = [[j for j in i] for i in input().split('\n')]

# x = list(map(int, input().split()))

# # rows = len(x)
# # cols = len(x[0])
#
# for i in range(0, 101):
#     p = i
#     for j in range(1, 101):
#         if p+1 < 100 and x[j][p + 1] == 1:
#             p += 1
#         elif p -1>= 0 and x[j][p - 1] == 1:
#             p -=1
#
# print(f'#{T} {x[101 - 1][p]}')
#
# # for i in range(0, 100 + 1):
# #     for j in range(0, 100 + 1):

input = '''
10010
11100
10000
10000
axxxx
'''

ladder = [[j for j in i] for i in input.strip().split('\n')]
rows = len(ladder) # 가로
cols = len(ladder[0])
print(ladder)
for i in range(0, cols):
    # 위치
    p = i
    for j in range(1, rows):
        # 오른쪽에 - 가 있으면
        if p + 1 < cols and ladder[j][p + 1] == '1':
            p += 1
        elif p - 1 >= 0 and ladder[j][p - 1] == '1':
            p -= 1
    print(ladder[0][i], '-', ladder[rows - 1][p])