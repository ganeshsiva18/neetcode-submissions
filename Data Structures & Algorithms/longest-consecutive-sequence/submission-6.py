class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        f = 0
        for n in nums:
            if n-1 not in nums:
                c = 1
                while (n + c) in numset:
                    c += 1
                f = max(c, f)
        return f
