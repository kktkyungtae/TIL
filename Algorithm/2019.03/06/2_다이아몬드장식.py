T = int(input())

word = map(str,input().split())

if word == 1:
    for i in range(5):
        print('.#')

else:
    print('..#..')