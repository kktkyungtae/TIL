# 부분집합 합 문제 구현하기
# 부분집합 중 원소의 합이 0이 되는 부분집합을 모두 출력하시오.

arr = [-1,3,-9,6,7,-6,1,5,4,-2]
n = len(arr)

for i in range(0,(1<<n)):
    numlist = []
    for j in range(0,n):
        if i & (1<<j):
            numlist.append(arr[j])
    if sum(numlist) == 0 and len(numlist) != 0:
        print(numlist)



##
