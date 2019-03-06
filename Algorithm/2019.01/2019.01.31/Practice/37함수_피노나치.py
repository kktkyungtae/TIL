
# def fib(n) :
#     if n == 1 or n == 2 :
#         return 1
#     return fib(n - 1) + fib(n - 2)
#
# print(fib(13))

d = int(input())

def fibo(d):
    a = 0
    b = 1
    c = a + b
    while c < d:
        print(c, end = " ")
        c = a + b
        a = b
        b = c

fibo(d)