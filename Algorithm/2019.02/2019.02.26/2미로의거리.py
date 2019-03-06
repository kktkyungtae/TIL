# -*- coding: utf-8 -*-

import sys
sys.stdin = open('2미로의거리.txt', 'r')

T = int(input())

for test_case in range(T):
    maze = []
    N = int(input())

    for n in range(N):
        black = input()
        maze.append([int(x) for x in black])

    visitied = [[False] * N for x in range(N)]
    start = ()
    end = ()

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 1:
                visitied[i][j] = True
            elif maze[i][j] == 2:
                start = (i, j, 0) # what is it?
            elif maze[i][j] == 3:
                end = (i, j, 0)

    dx = [1,-1,0,0]
    dy = [0,0,-1,1]
    result = 0





