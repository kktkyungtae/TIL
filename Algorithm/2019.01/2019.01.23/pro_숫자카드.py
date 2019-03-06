T = int(input())

for tc in range(1,T+1):

    N=int(input())
    cards = input()
    cnt = [0] *10

    for i in range(N):
        cnt[int(cards[i])] +=1

    maxi = 0
    for i in range(10):
        if cnt[maxi] <= cnt[i]:
            maxi = i
    print("#%d %d %d %(tc,maxi, cnt[maxi)")
