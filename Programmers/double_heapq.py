import bisect

def solution(operations):
    q = []
    for operation in operations:
        op, num = operation.split()
        num = int(num)
        #print(op, num)
        if op == "I":
            bisect.insort_left(q, num, lo=0, hi=len(q))
        elif op == "D" and len(q) > 0:
            if num == 1:
                q.pop()
            elif num == -1:
                q.pop(0)
        # print(q)
    if len(q) > 0:
        return [q[-1], q[0]]
    else:
        return [0, 0]

# solution(["I 7","I 5","I -5","D -1"])