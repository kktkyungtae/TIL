# -*- coding: utf-8 -*-
import sys
sys.stdin = open('1_input.txt','r')

T = int(input())

def get_goro(x,y,bw):
    # 오른쪽
    for i in range(x+1,len(ground_li)):
        if ground_li[i][y] == 0:
            break
        elif ground_li[i][y] == bw:
            if abs(i - x) == 1:
                ground_li[i][y] = bw
                break
    # 왼쪽
    for i in range(x-1,0,-1):
        if ground_li[i][y] == 0:
            break
        elif ground_li[i][y] == bw:
            if abs(x - i) == 1:
                ground_li[i][y] = bw
                break


def get_sero(x,y,bw):
    # 위
    for i in range(y+1,N+1):
        if ground_li[x][i] == 0:
            break
        elif ground_li[x][i] == bw:
            if abs(i - y) == 1:
                ground_li[x][i] = bw
                break
    # 아래
    for i in range(y-1,0,-1):
        if ground_li[x][i] == 0:
            break
        elif ground_li[x][i] == bw:
            if abs(y - i) == 1:
                ground_li[x][i] = bw
                break

def get_daegak(x,y,bw):
    # 위 - 오른쪽
    for i in range(x+1,N+1):
        for j in range(y+1,N+1):
            if ground_li[i][j] == 0:
                break
            elif ground_li[i][j] == bw:
                if abs(x - i) == 1 and abs(y - j) == 1:
                    ground_li[i][j] = bw
                    break

    # 위 - 왼쪽
    for i in range(x - 1, 0,-1):
        for j in range(y+1,N+1):
            if ground_li[i][j] == 0:
                break
            elif ground_li[i][j] == bw:
                if abs(x - i) == 1 and abs(j - y) == 1:
                    ground_li[i][j] = bw
                    break

    # 아래 - 오른쪽
    for i in range(x + 1, N + 1):
        for j in range(y - 1, 0, -1):
            if ground_li[i][j] == 0:
                break
            elif ground_li[i][j] == bw:
                if abs(i - x) == 1 and abs(y - j) == 1:
                    ground_li[i][j] = bw
                    break


    # 아래 - 왼쪽
    for i in range(x - 1,0,-1):
        for j in range(y - 1, 0, -1):
            if ground_li[i][j] == 0:
                break
            elif ground_li[i][j] == bw:
                if abs(x - i) == 1 and abs(y - j) == 1:
                    ground_li[i][j] = bw
                    break



for tc in range(T):
    N, M = map(int,input().split())
    ground_li = [[0]*(N+1) for _ in range(N+1)]
    ground_li[(N//2)+1][(N//2)] = 1
    ground_li[(N//2)][(N//2)] = 2
    ground_li[(N//2)+1][(N//2)+1] = 2
    ground_li[(N//2)][(N//2)+1] = 1

    for j in range(M):
        x,y,bw = map(int,input().split())
        ground_li[x][y] = bw
        get_daegak(x,y,bw)
        get_goro(x,y,bw)
        get_sero(x,y,bw)

    result_x,result_y = 0,0
    for i in range(len(ground_li)):
        for j in range(len(ground_li)):
            if ground_li[i][j] == 1:
                result_x+=1
            elif ground_li[i][j] == 2:
                result_y+=1


    print('#{} {} {}'.format(tc+1,result_x,result_y))