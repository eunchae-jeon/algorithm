import sys
In = sys.stdin.readline

def main():
    n, m = map(int, In().split())
    b = 1000
    e = 1000

    for _ in range(m):
        b_temp, e_temp = map(int, In().split())
        if b_temp < b:
            b = b_temp
        if e_temp < e:
            e = e_temp
    print(cal_price(n, (b, e)))


def cal_price(n, p):
    if p[0] >= p[1] * 6:
        return n * p[1]
    elif p[0] < (n%6)*p[1]:
        return p[0]*((n//6)+1)
    else :
        return p[0]*(n//6) + p[1]*(n%6)

main()