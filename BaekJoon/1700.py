import sys
import bisect
In = sys.stdin.readline

n, k = map(int, In().split())

devices = list(map(int, In().split()))
multitab = []
nextidx = []
ans = 0

for i, device in enumerate(devices):
    nextd = 0
    idx = 0
    for j in range(i+1, len(devices)):
        if device == devices[j]:
            nextd = j
            break
    else:
        nextd = k
    if device in multitab:
        nextidx.remove(nextidx[multitab.index(device)])
        multitab.remove(device)
    if len(multitab) >= n:
        if multitab[-1] != device:
            # print(multitab[-1], device)
            ans += 1
        multitab.pop()
        nextidx.pop()


    idx = bisect.bisect_left(nextidx, nextd, lo=0, hi=len(nextidx))
    nextidx.insert(idx, nextd)
    multitab.insert(idx, device)

    # print(multitab)
    # print(nextidx)


print(ans)

