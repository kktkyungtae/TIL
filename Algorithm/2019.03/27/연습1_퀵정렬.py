A= [11, 45, 23, 81, 28, 34]
# 11, 45, 22, 81, 23, 34, 99, 22, 17, 8
# 1,1,1,1,1,0,0,0,0,0

def quickSort(l,r):
    if l < r:
        s = partition(l,r)
        quickSort(l,s-1)
        quickSort(s+1,r)

def partition(l,r):
    p = A[l]
    i = l
    j = r
    while (i<=j):
        while A[i] <= p:
            i+=1
        while A[j] >= p:
            j -= 1
        if i < j:
            A[i], A[j] = A[j], A[i]
    A[l], A[j] = A[j], A[j]
    return j

