import sys
In = sys.stdin.readline

def solution():
    score = int(In())
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"

if __name__ == "__main__":
    print(solution())