s = "pwwkew"
ls = []
lcs = 0

for i in s:
    if i not in ls:
        ls.append(i)
    else:
        lcs = len(ls)
        print(lcs)
        break   