# def select(list,k):
#     for i in range(0,k):
#         minIndex = i
#         for j in range(i+1, len(list)):
#             if list[minindex] > list[j]:
#                 minIndex = j
#         list[i], list[minIndex] = list[minIndex], list[i]
#     return list[k-1]
#
# print(select([4,8,5,2,44,5,5],3))
#
#
# a = [
#     [9,20,2,18,11],
#     [19,1,25,3,21],
#     [8,24,10,17,7],
#     [15,4,16,5,6],
#     [12,13,22,24,14]
# ]
#
# for x in a:
#     print(x[0])

def selectSort(a):
    for i in range(0,len(a)):
        min = i
        for j in range(i+1, len(a)):
            if a[min] > a[j]:
                min = j
        a[i], a[min] = a[min], a[i]
    return a

a1 = [9,20,2,18,11,321,32,42]

print(selectSort(a1))




