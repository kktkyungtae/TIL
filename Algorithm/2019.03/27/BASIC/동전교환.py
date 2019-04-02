coin = [6,4,1]
# sol = [0] * 100
# #완전 탐색을 할 수 밖에 없는데 어떻게 할것이냐
# def coinChange(k,n):
#     if n == 0: return 0
#         MIN = 0xffff
#     for val in coin:
#         if val > n: continue # 코인 값이 더 커지면 건너 뛰겠다.
#         ret = coinChange(n - val)
#         MIN = min(ret,MIN)
#     return MIN + 1
# coinChange(8) # 노드의 높이 k, 거스름돈 금액 n
# # 코인 값이 커지면 계속 찾게 된다.. 1원은 80번 들어가야 되니까 그래서 가지치기 해야되