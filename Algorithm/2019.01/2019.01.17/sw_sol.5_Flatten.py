import sys
sys.stdin = open('5_Flatten_input.text','r')

T = 10
for tc in range(1,T+1):
    q = int(input())
    w = list(map(int,input.split()))
    dump = 0
    maxx = 0

    for i in range(0, len(w)+1):
        if w[i] > maxx:
            maxx == w[i]
         

print(f'#{tc}, {maxx}')