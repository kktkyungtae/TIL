def DFS(v):  # v는 시작점
    stack = []  # 스택
    visited = [False] * (V + 1)  # 정점의 갯수만큼 방문표시(1~V)
    # 시작점을 방문하고 스택에 어펜드
    visited[v] = True
    print(v, end='')
    stack.append(v)

    # 빈 스택이 아닐 동안 반복문 돈다
    while len(stack) > 0:
        # v는 현재 방문하고 있는 정점
        # v의 방문하지 않은 인접 정점을 하나를 찾는다.
        for w in G[v]:  # 하나씩들고 와서 확인한다.
            # 이런 스타일로 짜면 처음 시작점을 넣기 위해 스택에 넣고 지나온 길을 또 넣으니까 첫 정점이 두번 들어가는데 상관 없다 어짜피 다 빼니까
            if not visited[w]:
                visited[w] = True
                print(w, end='')
                stack.append(v)
                v = w
                break  # 하나만저장하고 빠져야되니까
                # if 문에 걸리지 않을 수도 있다..
                # 길이 없거나.. 다 방문 했거나
                # 그러면 되돌아 가야지
        else:  # for에도 else를 달 수가 있다!!! for문 다 돌고     else에 간다.. break로 빠지면 안가고!
            # 이거 싫으면 변수 하나 설정해놓고 브레이크로 빠졌는지 다 돌고 빠졌는지 해주면됨
            v = stack.pop()


V, E = map(int, input().split())  # V는 정점수 E : 간선수
G = [[] for _ in range(V + 1)]
for i in range(E):
    U, V = map(int, int().split())
    G[u].append(v)
    G[v].append(u)