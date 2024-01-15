#break: for, while에 반복을 끊는 역할
#continue: jump 같은 역할


for i in range(100):
    if i == 50:
        break
    else:
        print(i)

for i in range(100):
    if i == 50:
        continue
    else:
        print(i)