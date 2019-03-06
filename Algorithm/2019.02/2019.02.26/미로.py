import sys
sys.stdin = open('input.txt','r')

T = int(input())

for i in range(T):
    N = int(input())
    maze = [[1 for x in range(N+2)]]
