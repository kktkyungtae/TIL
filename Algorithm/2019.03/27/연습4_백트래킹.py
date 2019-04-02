# 부분집합 중 원소의 합이 10인 부분집합을 모두 구해라.

def backtrack(a,k,input):
    c=[False]*2 # True /False를 받아줄 배열
    ncands = 2 # 후보자 군은 2개/ True , False

    if k==input: # 자리수가 부분집합을 구하려는 input과 같으면
        process_solution(k) # 출력하는 함수로 출력한다.
    else: # 같지 않으면..
        k+=1 # 자리수를 하나 더하고
        make_candidates(k,input,c,ncands) # c 배열 t/f 넣어주는 함수
        for i in range(ncands):
            a[k] = c[i]
            backtrack(a,k,input)

def make_candidates(k,n,c,ncands): # c 배열에 t/f 를 넣어준다.
    c[0] = True
    c[1] = False
    # ncands = 2

def process_solution(k): # 결과를 출력하는 함수
    for i in range(0,k+1): # t/f 만 정해줬고, 어떤 수를 출력할지 안정해 줬으니
        if a[i] == True:  # T 인 것을 출력하기 위해서 선언
            print(i, end=' ')
    print()
a = [False]*11
backtrack(a,0,10)