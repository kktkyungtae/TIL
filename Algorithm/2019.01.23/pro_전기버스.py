T = int(input())
for tc in range(1, T+1):
    K,N,M= list(map(int, input().split()))
    c = list(map(int, input().split())) 
    stations = [0] * (N+1)
    
    for i in range(M):
        stations[c[i]] = 1

    cnt = cur = 0 # cur:버스위치
    while(True):
        pre = cur # 이전위치는 내위치, 내위치 저장 왜냐면 다시 돌아오면 0 이니까
        cur += K
        if cur >= N:
            break
        if stations[cur] == 1:
            cnt += 1
        else:
            for i in range(1, K+1):
                if stations[cur-i] == 1:
                    cur-=i
                    cnt+=1
                    break
            if cur == pre:
                cnt = 0
                break
    print("#%d" % tc, cnt)