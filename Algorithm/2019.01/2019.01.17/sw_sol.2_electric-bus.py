# [2019.01.17_문제2_Electric Bus]
# k = 충전 후 이동할 수 있는 정류장 수
# N = 종점 까지의 정류장 수
# M = 충전기가 있는 정류장 수

import sys
sys.stdin = open('2_elec-bus_input.text','r')

T = int(input())

for tc in range(1,T+1):
    KNM = list(map(int,input().split()))
    J = list(map(int,input().split()))
    K = KNM[0]
    N = KNM[1]
    M = KNM[2]
    kk = 0
    for i in range(1,len(J)):
        if J[i] - J[i+1] > K:
            return 0
        else :
            return K // N

print(f'#{tc}, {return}')

