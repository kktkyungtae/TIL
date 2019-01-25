a = [88,30,61,55,95]
tc = 0

for i in a:
    tc +=1
    if i >= 60:
        print(f'{tc}번 학생은 {i}점으로 합격입니다.')
    else:
        print(f'{tc}번 학생은 {i}점으로 불합격입니다.')
