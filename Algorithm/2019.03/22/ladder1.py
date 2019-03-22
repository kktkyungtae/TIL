
def ladder(v):
    stack = []
    visited = [False]*100
    visited[v] = True
    stack.append(v)

    while len(stack) > 0:
        for w in G[v]:
            if not visited[w]:
                visited[w] = True
                stack.append(v)
                v = w
                break
            else:
            v= stack.pop()

T = int(input())

for tc in range(T):
    lists = []
    lists.append(list(map(int,input().split())))


    for i in range(100):
        if lists[i][0] == 1:
            stack.append(i)
            visited[i] = True
            start = i

# 강사님 코드

def dfs(x,y):
    if x == 0: # 도착 했다면
        ans = y
        return
    visited[x][y] = True # 방문 처리
    # 도착 안했다면
    if y - 1>=0 and arr[x][y-1] and visited[x][y-1]: #왼쪽
        dfs(x,y-1)
    elif y + 1>=0 and arr[x][y+1] and visited[x][y+1]: #오른쪽
        dfs(x,y+1)
    else:
        dfs(x-1,y)


for tc in range(10):
    T = int(input())

    arr = [list(map(int, input().split())) for _ in range(100)]

    sx = sy = 0 # 시작점
    for i in range(100):
        if arr[99][i] == 2:
            sx, sy = 99, i
            break

    visited = [[False] * 100 for _ in range(100)]
    ans = 0 # 전역변수?
    dfs(sx,sy)


# 강사님 코드(return 하기)

def dfs(x,y):
    if x == 0: # 도착 했다면
        return y # 리턴 y를 해주는 것
    visited[x][y] = True # 방문 처리
    # 도착 안했다면
    returns = 0
    if y - 1>=0 and arr[x][y-1] and not visited[x][y-1]: #왼쪽
        returns = dfs(x,y-1)
    elif y + 1>=0 and arr[x][y+1] and not visited[x][y+1]: #오른쪽
        returns = dfs(x,y+1)
    else: # 아래쪽
        returns = dfs(x-1,y)
    return returns


for tc in range(10):
    T = int(input())

    arr = [list(map(int, input().split())) for _ in range(100)]

    sx = sy = 0 # 시작점
    for i in range(100):
        if arr[99][i] == 2:
            sx, sy = 99, i
            break

    visited = [[False] * 100 for _ in range(100)]
    ans = 0 # 전역변수?
    dfs(sx,sy)


# 강사님 코드(지우면서 가기)

def dfs(x,y):
    if x == 0: # 도착 했다면
        return y # 리턴 y를 해주는 것
    arr[x][y] = 0 # 지나온 길을 0으로 지워주고////

    # 도착 안했다면
    returns = 0
    if y - 1>=0 and arr[x][y-1]  #왼쪽
        returns = dfs(x,y-1)
    elif y + 1>=0 and arr[x][y+1]  #오른쪽
        returns = dfs(x,y+1)
    else: # 아래쪽
        returns = dfs(x-1,y)

    arr[x][y] = 1 # 지나온 길을 복구해주기 위해 리턴 전에 해준다..
    return returns


for tc in range(10):
    T = int(input())

    arr = [list(map(int, input().split())) for _ in range(100)]

    sx = sy = 0 # 시작점
    for i in range(100):
        if arr[99][i] == 2:
            sx, sy = 99, i
            break

    visited = [[False] * 100 for _ in range(100)]
    ans = 0 # 전역변수?
    dfs(sx,sy)