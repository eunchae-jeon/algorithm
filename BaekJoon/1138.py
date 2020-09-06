import sys
In = sys.stdin.readline

l = int(In())
data = list(map(int, In().split()))
ans = [0 for _ in range(l)]

for i, d in enumerate(data):
    count = 0
    for j, a in enumerate(ans):
        if ans[j] == 0:
            if count == d:
                ans[j] = i+1
                break
            count+=1
answer = ""
for a in ans:
    answer += str(a) + " "

print(answer[:-1])
