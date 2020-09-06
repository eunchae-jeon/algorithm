from collections import deque

def solution(begin, target, words):
    words = [begin] + words
    target_index = 0
    connection = [[] for _ in range(len(words))]
    for i in range(len(words)):
        if words[i] == target:
            target_index = i
        for j in range(i+1, len(words)):
            diff = 0
            for k in range(len(words[i])):
                if words[i][k] != words[j][k]:
                    diff += 1
                    if diff > 1:
                        break
            else:
                if diff == 1:
                    connection[i].append(j)
                    connection[j].append(i)

    visited = [False for _ in range(len(words))]
    queue = deque([(0, 0)])
    while queue:
        cur = queue.popleft()
        if cur[0] == target_index:
            return cur[1]
        visited[cur[0]] = True
        for c in connection[cur[0]]:
            if visited[c] == False:
                queue.append((c, cur[1]+1))
        
    return 0

if __name__ == "__main__":
    print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))