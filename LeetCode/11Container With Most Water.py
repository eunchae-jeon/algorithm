class Solution:
    def maxArea(self, height) -> int:
        left = [(height[0], 0)]
        right = [(height[-1], len(height)-1)]
        for i,h in enumerate(height):
            if h > left[-1][0]:
                left.append((h, i))
        for i,h in enumerate(reversed(height)):
            if h > right[-1][0]:
                right.append((h, len(height) - i - 1))
        
        area = 0
        for l in left:
            for r in right:
                a = min(l[0], r[0]) * (r[1] - l[1])
                if a > area:
                    area = a
        return area
        # print(left, right)

s = Solution()
s.maxArea([1,8,6,2,5,4,8,3,7])