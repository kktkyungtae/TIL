# 부분집합 중 원소의 합이 10인 부분집합을 모두 구해라.

def backtrack(a,k,input):
    c = [0] * 2
    ncands = 2
    c[0] = True
    c[1] = False
    if k==input:
        process_solution(k)
    else:
        k+=1
        for i in range(ncands):
            a[k] = c[i]
            backtrack(a,k,input)

def process_solution(k):
    for i in range(0,k+1):
        if a[i] == True:
            print(i, end=' ')
    print()
a = [False]*11
backtrack(a,0,10)

def backtrack(arr,k,n,sum):
    if sum > 10:
        return
    if k == n:
        if sum == 10:
            for j in range(n):
                if chk[j]