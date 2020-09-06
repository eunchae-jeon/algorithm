import sys
In = sys.stdin.readline

def main():
    n, m = map(int, In().split())
    distances = [[0, 0, 0, 0] for _ in range(m)]
    convert = ["A", "C", "G", "T"]
    dic = {"A" : 0, "C" : 1, "G" : 2, "T" : 3}

    for _ in range(n):
        dna = In().rstrip()
        for i, d in enumerate(dna):
            distances[i][dic[d]] += 1
            
    
    ans = ""
    num = 0
    for dis in distances:
        max_dis = max(dis)
        ans += convert[dis.index(max_dis)]
        num += sum(dis) - max_dis

    print(ans)
    print(num)
    

main()

