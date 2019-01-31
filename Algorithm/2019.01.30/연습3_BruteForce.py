#고지식한 방법을 이용하여 패턴을 찾아봅시다.
# 임의의 본문 문자열과 찾을 패턴 문자열을 만듭니다.
# 결과 값으로 찾은 위치 값을 결과로 출력합니다.

def BruteForce(t, p) :
    i = 0
    j = 0
    N = len(t)
    M = len(p)
    while j < M and i < N :
        if t[i] != p[j] :
            i = i - j
            j = -1
        i += 1
        j += 1
    if j == M : return i - M
    else: return i


T = "abcabcdefdadddddgdsasdfesdfkasdf"
P = "ddddd"
print(T[ BruteForce(T, P):] )