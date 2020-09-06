import sys
In = sys.stdin.readline

def main():
    In()
    dic = {}
    cards = list(map(int, In().split()))
    for card in cards:
        if card in dic:
            dic[card] += 1
        else:
            dic[card] = 1
    
    In()
    answer = ""
    checks = list(map(int, In().split()))
    for check in checks:
        if check in dic:
            answer += str(dic[check]) + " "
        else:
            answer += "0 "
    return answer.rstrip()

    


if __name__ == "__main__":
    print(main())

