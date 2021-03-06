# str() 함수를 사용하지 않고, itoa()를 구현해 봅시다.
# - 양의 정수를 입력받아 문자열로 변환하는 함수
# - 입력 값 : 변환할 정수 값, 변환된 문자열을 저장할 문자배열
# 반환 값 : 없음
# 음수를 변환할 할때 필요한 고려사항은?

def itoa(x):
    sr =''
    while True:
        r = x % 10
        sr = sr + chr(r + ord('0'))
        x //= 10
        if x == 0: break

    s = ''
    for i in range(len(sr) - 1, -1, -1):
        s = s + sr[i]

    return s

print(itoa(1234))