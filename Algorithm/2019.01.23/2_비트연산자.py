# 입력 받은 수들의 집합의 합 중에서, 0이되는 집합의 수를 구하라.


arr = [-3,3,-9,6,7,-6,1,5,4,-2]
sum = cnt = 0

for i in range(1,1<<len(arr)):
    for j in range(len(arr)):
        if i &(1<<j):
            sum += arr[j]

    if sum == 0 :
        cnt +=1
        print("cnt: ", cnt, end=", 배열:  ")
        for j in range(len(arr)):
            if i & (1<<j):
                print(arr[j], end=" ")
        print()
    sum = 0