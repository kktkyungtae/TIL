# -*- coding: utf-8 -*-

import sys
sys.stdin = open('1회전.txt','r')

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int,input().split())
    lists = list(map(int,input().split()))

    # 원형 큐 생성
    queue = [0]*N
    front = rear = 0

    for i in range(len(lists)):
        queue[i] = lists[i]
        rear = (rear + 1) % len(queue)

    for j in range(M):
        front = (front + 1) % len(queue)
        a = queue[front]
        # enQueue
        rear = (rear + 1) % len(queue)
        queue[rear] = a

    print(f'#{test_case} {queue[front]}')




