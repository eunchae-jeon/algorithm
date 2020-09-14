import sys
In = sys.stdin.readline

def solution():
    t = int(In())
    for _ in range(t):
        n = int(In())
        trie = [-1, False, []]
        phones = [In().rstrip() for _ in range(n)]
        # phones.sort(key=lambda phone: len(phone))
        flag = False
        for phone in phones:
            cur = trie
            for i, num in enumerate(phone):
                node = find_node(cur, num)
                if cur[1] == True:
                    flag = True
                    break
                elif node == None:
                    #number, chilren, isLeaf
                    newNode = [num, (i == len(phone)-1), []]
                    cur[2].append(newNode)
                    cur = newNode
                else:
                    if i == len(phone)-1:
                        cur[1] = True
                        if len(cur[2]) > 0:
                            flag = True
                            break
                    cur = node
            if flag:
                break
            
        if flag:
            print('NO')
        else:
            print('YES')
        
def find_node(trie, num):
    for node in trie[2]:
        if node[0] == num:
            return node
    else:
        return None

if __name__ == "__main__":
    solution()