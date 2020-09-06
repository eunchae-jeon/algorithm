class Solution:
    def findPoisonedDuration(self, timeSeries: list, duration: int) -> int:
        end = 0
        answer = 0
        for t in timeSeries:
            if t < end:
                answer -= (end - t)
            answer += duration
            end = t + duration
        return answer

s = Solution()
print(s.findPoisonedDuration([1,4], 2))