# 다음의 결과와 같이 가상의 두 사람이 가위 바위 보 중 하나를 내서 승패를 가르는 가위 바위 보 게임을 작성하십시오.
# 이 때 ["가위", "바위", "보"] 리스트를 활용합니다.
import random

Man = {'가위':1, '바위':2, '보':3}
Man1 = [random.choice(Man)]
Man2 = [random.choice(Man)]

print(f'{Man1[0]} {Man2[0]}')

    # if Man1[0] == '가위' and Man2[0] =='보':
    #     print("Result : Man1 Win!")
    # elif Man1[0] == '가위' and Man2[0] =='바위':
    #     print("Result : Man2 Win!")
    # elif Man1[0] == '가위' and Man2[0] =='가위':
    #     print("Result : Drow")
    # elif Man1[0] == '바위' and Man2[0] =='바위':
    #     print("Result : Drow")
    # elif Man1[0] == '바위' and Man2[0] =='가위':
    #     print("Result : Man2 Win!")
    # elif Man1[0] == '바위' and Man2[0] =='바위':
    #     print("Result : Drow")
    # elif Man1[0] == '보' and Man2[0] =='가위':
    #     print("Result : Man2 Win!")
    # elif Man1[0] == '보' and Man2[0] =='바위':
    #     print("Result : Man1 Win!")
    # elif Man1[0] == '보' and Man2[0] =='보':
    #     print("Result : Drow")
