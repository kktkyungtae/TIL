# 0과 1로 이루어진 1차 배열에서 7개 byte를 묶어서 10진수로 출력하기

ex_list = '0000000111100000011000000111100110000110000111100111100111111001100111'

for i in range(0,len(ex_list),7):
    summ = 0
    for j in range(6,-1,-1):
        if ex_list[i+j] == '1':
            k = i+j
            summ += 2**k
    print(summ)


# t=0
# for i in range(len(ex_list)):
#     t = t*2+int(ex_list[i])
#     if (i+1) % 7 == 0:
#         print(t,end =' ')
#         t=0