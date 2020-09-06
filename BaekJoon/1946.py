import sys
In = sys.stdin.readline

def main():
    test = int(In())
    ans = list()
    for _ in range(test):
        ans.append(hire())
    for a in ans:
        print(a)

def hire():
    person_num = int(In())
    person = sorted([list(map(int, In().split())) for _ in range(person_num)])
    print(person)
    flag = person_num
    ans = 0
    for p in person:
        if p[1] <= flag:
            flag = p[1]
            ans += 1
    return ans

main()