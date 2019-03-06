a = int(input())

def abc(x):
    if x % 3 == 0 or x % 2 == 0 or x % 5 == 0 or x % 7 == 0:
        print('소수가 아닙니다.')
    elif x % 1 == 0 and x % x == 0:
        print('소수입니다.')

print(abc(a))