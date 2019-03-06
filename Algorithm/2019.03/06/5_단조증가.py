import sys
sys.stdin = open('5_input.txt','r')

def get_guess(guess):
    guess = str(guess)
    for i in range(len(guess)-1):
        if int(guess[0]) > int(guess[-1]):
            return False
        elif int(guess[i]) <= int(guess[i+1]):
            return True
        else:
            return False

T = int(input())

for test_case in range(T):
    N = int(input())
    alists = list(map(int,input().split()))

    result = 0
    for i in range(len(alists)):
        for j in range(len(alists)):
            if i < j:
                guess = alists[i] * alists[j]
                if get_guess(guess) == True:
                    if result < guess:
                        result = guess
    print('#{} {}'.format(test_case+1, result))