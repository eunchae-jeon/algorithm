class Solution:
    def longestCommonPrefix(self, strs) -> str:
        
        try:
            answer = strs[0]
        except:
            answer = ''

        for s in strs:
            temp = ''
            for i in range(min(len(answer), len(s))):
                if answer[i] == s[i]:
                    temp += s[i]
                else:
                    break
            answer = temp

        return answer

s = Solution()
print(s.longestCommonPrefix(["aca","cba"]))