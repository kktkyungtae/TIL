import sys
sys.stdin = open('02_input.txt','r')

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