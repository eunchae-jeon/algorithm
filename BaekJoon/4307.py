import sys
In = sys.stdin.readline

testcase = int(In())
for _ in range(testcase):
    length, ant_num = map(int, In().split())
    ant_pos = [int(In()) for _ in range(ant_num)]
    mx, mn = max(ant_pos), min(ant_pos)
    ct = min(abs(pos - length/2) for pos in ant_pos)
    print(int(length/2 - ct), max(length-mn, mx))
