class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        count = 0
        s_set = set()
        for r in range(len(s)):
            while s[r] in s_set:
                s_set.remove(s[l])
                l += 1
            s_set.add(s[r])
            count = max(count, r-l+1)
        return count