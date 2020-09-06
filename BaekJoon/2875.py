import sys
n, m, k = map(int, sys.stdin.readline().split())
remain = 0
team = 0
if n > 2*m :
    team = m
    remain = n - 2*m
else:
    team = n//2
    remain = m + n - 3*(n//2)

if remain >= k:
    print(team)
else:
    team = team - (2+k-remain)//3
    print(team)
