import bisect
import sys
In = sys.stdin.readline
universes = []
planets_order = {}
answer = 0
m, n = map(int, In().split())
for _ in range(m):
    universes.append(list(map(int, In().split())))
for planets in universes:
    sorted_planets = sorted(planets)
    temp = ""
    for planet in planets:
        temp += str(bisect.bisect(sorted_planets, planet, lo=0, hi=len(sorted_planets)))
    if temp in planets_order:
        answer += planets_order[temp]
        planets_order[temp] += 1
    else:
        planets_order[temp] = 1

print(answer)
