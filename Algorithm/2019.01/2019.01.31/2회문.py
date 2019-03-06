
import sys
sys.stdin= open("2회문","r")

# 1
def isPalindrome(a):
    len_a = len(a)
    for i in range(len_a // 2):
        if a[i] != a[len_a - (i + 1)]:
            return False
    return True

T = int(input())
for t in range(1, T+1):
    a, b = map(int, input().split()) # 20 13
    c = a-b+1
    result = [[] for _ in range(a)]  # [[], [], [], [], [], [], [], [], []]
    answer=''
    # 2차원 배열 만들기
    for i in range(a):
        word = input()
        for j in range(a):
            result[i].append(word[j])

    # 가로, 세로 회전문 조회
    for i in range(a):
        for j in range(c):
            wid = ''
            hei = ''
            for k in range(j, j+b):
                wid += result[i][k]
                hei += result[k][i]
            if(isPalindrome(wid) == True):
                print(f"#{t} {wid}")
            if(isPalindrome(hei) == True):
                print(f"#{t} {hei}")


# 2
# def isPalindrome(a):
#     len_a = len(a)
#     for i in range(len_a // 2):
#         if a[i] != a[len_a - (i + 1)]:
#             return False
#     return True
#
# def getSentence(a, b, result):
#     c = a - b + 1 # ex) a=20, b=13이면 20까지 13글자를 조회해야함. 마지막 index 는 [i][7]~[i][19]까지니까 c= 20-13+1=8
#
#     # 가로, 세로 회전문 조회
#     for i in range(a):      # 세로 길f이
#         for j in range(c):  # 최대 j(13글자 조회니까 7까지만 가야함)
#             wid = ''
#             hei = ''
#             for k in range(j, j+b):
#                 wid += result[i][k]   # 0: i,0 ~ i,12,  1: 0,1 ~ 0, 13,  2: 0,2 ~ 0, 14 ..., 7: 0,7 ~ 0,19
#                 hei += result[k][i]   # 0: 0,0 ~ 12,0,  1: 1,0 ~ 13,0 , .... ,  7 : 7,0 ~ 19,0
#             if(isPalindrome(wid) == True):
#                 return wid
#             if(isPalindrome(hei) == True):
#                 return hei
#
# T = int(input())
# for t in range(1, T+1):
#     a, b = map(int, input().split())
#     result = [[] for _ in range(a)]
#
#     # 글자를 2차원 배열로 만들기
#     for i in range(a):
#         word = input()
#         for j in range(a):
#             result[i].append(word[j])
#     print(result)
#     answer = getSentence(a, b, result)
#
#     print(f"#{t} {answer}")



