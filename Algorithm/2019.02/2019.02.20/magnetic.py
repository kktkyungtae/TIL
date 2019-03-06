import sys
sys.stdin = open('magnetic.txt','r')

for t in range(10):
    lists = []
    N = int(input())
    for i in range(N):
        lists.append(list(map(int, input().split())))

    lists_N = [-1] * N
    lists_S = [-1] * N

    for i in range(N):
        for j in range(N):
            if lists_N[j] == -1 and lists[i][j] == 1:
                lists_N[j] = i

    for i in range(N - 1, -1, -1):
        for j in range(N - 1, -1, -1):
            if lists_S[j] == -1 and lists[i][j] == 2:
                lists_S[j] = i

    result = 0
    for x in range(N):
        if lists_N[x] == -1 or lists_S[x] == -1:
            continue
        else:
            now = 1
            for y in range(lists_N[x], lists_S[x] + 1):
                if now == 1 and lists[y][x] == 2:
                    result += 1
                    now = 2
                elif lists[y][x] == 1:
                    now = 1

    print(f"#{t + 1} {result}")