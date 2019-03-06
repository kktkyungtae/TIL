T = 1000
total = []

for x in range(T+1):
    lists = [T,x]
    i = 0
    while True:
        y = lists[i] - lists[i + 1]
        if y >= 0:
            lists.append(y)
            i += 1
        else:
            break

    if len(lists) > len(total):
        total = lists
    else:
        continue

print(len(total))
for i in total:
    print(i, end = ' ')