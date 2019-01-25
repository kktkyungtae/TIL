#1부터 100사이의 숫자 중 3의 배수의 총합을 for 문을 이용해 출력하십시오.

ssum = []
for i in range(100):
    if i % 3 ==0:
        ssum.append(i)

print(f'1부터 100사이의 숫자 중 3의 배수의 총합: {sum(ssum)}')