i = int(input())
stack = []

for t in range(i):
    t = int(input())
    stack.append(t)

while stack:
    print(stack.pop(0))

