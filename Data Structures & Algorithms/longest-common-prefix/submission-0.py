class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for i in range(1, len(strs)):
            j = 0
            n = strs[i]
            while j < min(len(n), len(prefix)):
                if prefix[j] != n[j]:
                    break
                j+=1
            prefix = prefix[:j]
        return prefix
