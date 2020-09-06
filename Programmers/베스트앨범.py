def solution(genres, plays):
    album = {}
    for i in range(len(genres)):
        if genres[i] not in album:
            album[genres[i]] = {0: plays[i], 1: (i, plays[i]), 2: (-1, 0)}
        else:
            album[genres[i]][0] += plays[i]
            if plays[i] > album[genres[i]][1][1]:
                album[genres[i]][2] = album[genres[i]][1]
                album[genres[i]][1] = (i, plays[i])
            elif plays[i] > album[genres[i]][2][1]:
                album[genres[i]][2] = (i, plays[i])

    genre_order = sorted(album.keys(), key=lambda k: album[k][0], reverse=True)
    answer = []
    for genre in genre_order:
        answer.append(album[genre][1][0])
        if album[genre][2][0] > -1:
            answer.append(album[genre][2][0])
    return answer
