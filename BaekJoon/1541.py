import sys

f = sys.stdin.readline()
ans = 0
num = ""
flag = False
for c in f:
    if c.isdigit() == True:
        num += c
    else:
        if flag == True:
            ans -= int(num)
        else:
            ans += int(num)
        num = ""
        if c == "-":
            flag = True       

print(ans)