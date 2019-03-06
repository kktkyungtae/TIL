
import sys
sys.stdin = open("5민석이의과제", "r")

# 1
# def my_sort(a):
#     for i in range(len(a)-1):
#         for j in range(len(a)-i-1):
#             if a[j] > a[j+1]:
#                 a[j], a[j+1] = a[j+1], a[j]
#     return a
#
# T = int(input())
# for t in range(1, T+1):
#     total, save = map(int, input().split())
#     nums = list(map(int, input().split()))
#
#     result = []
#     for i in range(1,total+1):
#         if i not in nums:
#             result.append(i)
#     result = my_sort(result)
#     print(f"#{t}", end=" ")
#     for i in result:
#         print(i, end=" ")
#     print()

# 2
T = int(input())
for t in range(1, T+1):
    total, save = map(int, input().split())
    nums = list(map(int, input().split()))
    result = [i for i in range(1, total+1)]

    # 과제 제출 한사람 0
    for i in range(save):
        result[nums[i]-1] = 0

    # 안한사람 출력
    print("#{}".format(t), end = " ")
    for i in range(total):
        if result[i]!= 0:
            print(result[i], end = " ")
    print()



