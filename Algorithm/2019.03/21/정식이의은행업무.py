import sys
sys.stdin = open('js_input.txt','r')

def trans_2to10(num):
    value = 0
    for i in range(len(num)):
        value += int(num[len(num)-1-i])*(2**i)
    return value

def trans_3to10(num):
    value = 0
    for i in range(len(num)):
        value += int(num[len(num)-1-i])*(3**i)
    return value

T = int(input())

for tc in range(T):
    bin2_num = input()
    ter3_num = input()

    num2_10 = trans_2to10(bin2_num)
    num3_10 = trans_3to10(ter3_num)

    num2to10 = []
    for i in range(len(bin2_num)):
        for j in range(int(bin2_num[i])):
            temp_bin2 = bin2_num[:i] + str(int(bin2_num[i])-(j+1)) + bin2_num[i+1:]
