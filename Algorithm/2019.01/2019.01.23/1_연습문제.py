a = [[1,1,1,1,1],[1,0,0,0,1],[1,0,0,0,1],[1,0,0,0,1],[1,1,1,1,1]]
result = 0

for i in range(1,4):
    for j in range(1,4):
        sum1 = a[i][j] - a[i][j-1]
        sum2 = a[i][j] - a[i-1][j]
        sum3 = a[i][j] - a[i][j+1]
        sum4 = a[i][j] - a[i-1][j]
        result = [sum1,sum2,sum3,sum4]

    def sum_t(a):
        for k in result:
        if k > 0:
            return k
        else:
            return -k

print(f'{}')

# review
def calAbs(y,x):
    if y - x > 0 : return y - x
    else:
        return x - y


dx = [-1,0,1,0]
dy = [0,1,0,-1]

sum = 0
for x in range(len(arr)):
    for y in range(len(arr[0])):

