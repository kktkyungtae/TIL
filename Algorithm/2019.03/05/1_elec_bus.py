# -*- coding: utf-8 -*-

import sys
sys.stdin = open('elec_bus.text', 'r')

T = int(input())

for test_case in range(T):
    k,n,m = map(int,input().split())
    char_station = list(map(int,input().split()))

    cur_station = 0
    charge_cnt = 0
    i = 0
    while cur_station + k < n:
        if cur_station + k < char_station[i]:
            charge_cnt = 0
            break
        elif cur_station + k == char_station[i]:
            cur_station = char_station[i]
            charge_cnt += 1
        else:
            if cur_station + k > char_station[i]:
                cur_station = char_station[i]
                charge_cnt += 1
        i+=1

    print('#{} {}'.format(test_case+1,charge_cnt))



