ls = [2, 1, 2, 1, 4]

for i in ls:
    num = i
    ls.remove(i)
    if num in ls:
        ls.append(num)
    else:
        print(num)
        break