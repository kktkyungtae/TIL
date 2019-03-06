import sys
sys.stdin = open('3_input.txt','r')

rect_list = []
for i in range(4):
    s = list(map(int,input().split()))
    rect_list.append(s)

mat = [[0] * 10 for i in range(10)]
for q in range(4):
    for i in range(rect_list[q][1], rect_list[q][3]):  # y
        for j in range(rect_list[q][0], rect_list[q][2]):  # x
            if mat[i][j] == 0:
                mat[i][j] = 1

cnt = 0
for i in range(10):
    for j in range(10):
        if mat[i][j] == 1:
            cnt += 1

print(cnt)