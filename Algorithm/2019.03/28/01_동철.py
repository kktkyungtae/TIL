import sys
sys.stdin = open('01_input.txt','r')
# n명, n개의 일이 있다.
# 각 사람과 일에 번호를 매겨놨는데,
# 사람이 일을 할때 능률은 각각 다르다.
# 일들을 하나씩 배분했을때 가장 높은 확률을 구하라

T = int(input())
for tc in range(T):
    N = int(input())
    work_p = []
    for i in range(N):
        work_p.append(list(map(int,input().split())))

    for i in range(N):
        for j in range(N):
            work_p[i][j] /= 100

