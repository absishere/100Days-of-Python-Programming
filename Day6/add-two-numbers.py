l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]
num1 = num2 = 0

for i in range(len(l1) - 1, -1, -1):
    num1 += l1[i] * (10 ** i)

for i in range(len(l2) - 1, -1, -1):
    num2 += l2[i] * (10 ** i)

sum = num1 + num2

anstr = str(sum)
ans = []
for i in range(len(anstr) - 1, -1, -1):
    ans.append(anstr[i])

print(ans)