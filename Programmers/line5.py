def solution(dataSource, tags):
    answer = []
    tag_dict = {}
    for data in dataSource:
        doc = data[0]
        for i in range(1, len(data)):
            if data[i] not in tag_dict:
                tag_dict[data[i]] = [doc]
            else:
                tag_dict[data[i]].append(doc)
    
    called_num = {}
    for tag in tags:
        for doc in tag_dict[tag]:
            if doc not in called_num:
                called_num[doc] = 1
            else:
                called_num[doc] += 1
            
    answer = [a[0] for a in sorted(called_num.items(), key=lambda d: (-d[1], d[0]))]
    return answer

print(solution([
    ["doc1", "t1", "t2", "t3"],
    ["doc2", "t0", "t2", "t3"],
    ["doc3", "t1", "t6", "t7"],
    ["doc4", "t1", "t2", "t4"],
    ["doc5", "t6", "t100", "t8"]
],
    ["t1", "t2", "t3"]
))