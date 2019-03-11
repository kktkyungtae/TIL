# import sys
# sys.stdin = open('6_input.txt','r')

T = int(input())

for test_case in range(T):
    lens = int(input())

    li = [[1]]
    for i in range(1,lens):
        li.append([1]*(i+1))

    for i in range(1,lens):
        for j in range(1,i):
            li[i][j] = li[i-1][j] + li[i-1][j-1]

    print('#{}'.format(test_case+1))
    # for i in range(len(li)):
    #     for j in range(len(li[i])):
    #         print(li([i][j]), end = ' ')
    for i in li:
        print(' '. join(str(x) for x in i))