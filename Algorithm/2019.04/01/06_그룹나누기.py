def make_set(x):
    joe[x] = x

def find_set(x):
    if x == joe[x]:
        return x
    else:
        return find_set(joe[x])

def union(x,y):
    temp = find_set(y)
    for j in range(len(joe)):
        if joe[j] == temp:
            joe[j] = find_set(x)
    # joe[find_set(y)] = find_set(x)

for tc in range(int(input())):
    N,M = map(int,input().split())
    team_request = list(map(int,input().split()))
    joe = [0] * N
    for i in range(N):
        make_set(i)
    for i in range(len(team_request)//2):
        union(team_request[2*i] -1,team_request[2*i+1])

print("#{} {}".format(tc+1,len(set(joe))))

