# 선택정렬의 재귀적 표현

# 반복
a = [1,54,2,48,4,14]

def SelctionSort(a):
    n = len(a)
    for i in range(0, n-1):
        min = i
        for j in range(i+1, n):
            if a[j] < a[min]:
                min = j
        temp = a[min]
        a[min] = a[i]
        a[i] = temp

# 재귀 : 샘코드
def SelSort(n):
    if n == (len(inp)-1):
        return
    minVal = inp[n]
    for i in range(n+1,len(inp)):
        if inp[i] < minVal:
            minVal = inp[i]
            mIdx = i
    temp = inp[n]
    inp[n] = inp[mIdx]

    SelSort(n+1)
    return
inp = list(map(int,input().split()))
SelSort(0)
print(inp)

# 동영 코드
def selsort(arr):
    if len(arr) == 1:
        return arr
    else:
        min_index = arr.index(min(arr))
        return [arr.pop(min_index)] + selsort(arr)