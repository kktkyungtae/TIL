# 1~9 사이의 정수 a를 입력받아 a + aa + aaa + aaaa 의 값을 계산하는 프로그램을 작성하십시오.

a = int(input("1~9 사이의 정수 하나를 입력하시오 : "))
b = [1,11,111,1111]
c = 0
for i in b:
    c+=a*i

print(c)