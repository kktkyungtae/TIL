# -*- coding: utf-8 -*-

import sys
sys.stdin = open('2_dungchi.txt','r')

M = int(input())
m_list = []
for ms in range(M):
    dungchi_ms = list(map(int,input().split()))
    m_list.append(dungchi_ms)

for m in m_list:
    print(m[0])