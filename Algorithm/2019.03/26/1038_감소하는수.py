N = int(input())
arr = range(10)
res = []
if N > 1022:
    print(-1)
else:
    for i in range(1,1<<10):
        l = 0
        for j in range(9,-1,-1):
            if i & (1<<j):
                l = 1*10 + arr[j]
            res.append(l)
    res.sort()
    print(res[N])
