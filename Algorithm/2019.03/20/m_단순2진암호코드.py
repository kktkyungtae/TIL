import sys
sys.stdin = open('input.txt','r')

pro_code = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9
}

T = int(input())
for tc in range(T):
    N, M = map(int,input().split())
    info = []
    for i in range(N):
        info.append(list(input()))


    code = ''
    for px in range(N):
        if '1' in info[px]:
            for py in range(M-1,-1,-1):
                if info[px][py] == '1':
                    code = ''.join(info[px][py-55:py+1])
                    break
            break

    result = []
    for i in range(0,len(code),7):
        result.append(pro_code.get(''.join(code[i:i + 7])))

    total = (result[0] + result[2] + result[4] + result[6]) * 3 + result[1] + result[3] + result[5] + result[7]

    if not total % 10:
        print("#{} {}".format(tc + 1, sum(result)))
    else:
        print("#{} 0".format(tc+1))


