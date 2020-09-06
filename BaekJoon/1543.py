import sys
In = sys.stdin.readline

document = In().rstrip('\n')
word = In().rstrip('\n')
i = 0
j = 0
l = len(word)
ld = len(document)
ans = 0
while True:
    if i == l:
        ans += 1
        i = 0
    if word[i] == document[j]:
        i += 1
    else:
        j -= i
        i = 0
    #print(j)
    j+= 1
    if j == ld:
        if i == l:
            ans += 1
        break


print(ans)