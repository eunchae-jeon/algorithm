import sys
import math
sys.setrecursionlimit(10**4)
In = sys.stdin.readline
max_int = 1000000001

def init(start, end, index):
    if start == end:
        seg_tree[index] = (num[start], num[start])
        return seg_tree[index]
    
    mid = (start + end) // 2
    lv = init(start, mid, index*2 + 1)
    rv = init(mid+1, end, index*2 + 2)
    seg_tree[index] = (max(lv[0], rv[0]), min(lv[1], rv[1]))

    return seg_tree[index]

def get_max_min(start, end, left, right, index):
    
    if right < start or left > end:
        ret = (0, max_int)
    elif left <= start and right >= end:
        ret = seg_tree[index]
        
    else:
        mid = (start + end) // 2
        lv = get_max_min(start, mid, left, right, index*2 + 1)
        rv = get_max_min(mid+1, end, left, right, index*2 + 2)
        ret = (max(lv[0], rv[0]), min(lv[1], rv[1]))
    # print(start, end, left, right, index, ret)
    
    return ret

n, m = map(int, In().split())
num = [int(In()) for _ in range(n)]
seg_tree = [0 for _ in range(2**(math.ceil(math.log2(n))+1))]
init(0, n-1, 0)
# print(seg_tree)
for _ in range(m):
    l, r = map(int, In().split())
    # print(l, r)
    result = get_max_min(0, n-1, l-1, r-1, 0)
    print(result[1], result[0])

