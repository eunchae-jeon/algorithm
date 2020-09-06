import sys
import bisect
In = sys.stdin.readline

length = int(In())
ports = list(map(int, In().split()))
dp =[0]

for port in ports:
    if port > dp[-1]:
        dp.append(port)
    else:
        i = bisect.bisect_left(dp, port, lo=0, hi=len(dp))    
        dp[i] = port
    #print(dp)

print(len(dp)-1)

# for i in range(length):
#     cur = -1
#     while True:
#         if ports[i] > dp[cur]:
#             if cur == -1:
#                 dp.append(ports[i])
#             else:
#                 dp[cur+1] = ports[i]
#             break
#         cur-=1
#     print(dp)

# print(len(dp)-1)