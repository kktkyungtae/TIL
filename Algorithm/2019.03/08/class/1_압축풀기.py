import sys
sys.stdin = open('1_zip.txt','r')

T = int(input())
for tc in range(T):
    N = int(input())

    case = []
    for i in range(N):
        case.append(list(map(str,input().split())))
        print(case)
