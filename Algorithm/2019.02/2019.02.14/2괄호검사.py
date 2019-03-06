stack = [0] * 100
top = -1
str = "(()()))"

wrong = 0
for i in range(len(str)):
    if str[i] == '(':
        top += 1; stack[top] = str[i]
    elif str[i] == ')':
        if top == -1:
            wrong = 1
            break
        if stack[top] == '(':
            top -= 1

if top == -1 and not wrong : print("correct!")
else: print("wrong!")