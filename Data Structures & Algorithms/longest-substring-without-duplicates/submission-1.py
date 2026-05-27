class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        count = 0
        mp = {}

        for r in range(len(s)):
            if s[r] in mp:
                l = max(l, mp[s[r]]+1)
            mp[s[r]] = r
            count = max(count, r-l+1)
        return count