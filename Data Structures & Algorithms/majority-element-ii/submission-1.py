class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums.sort()
        res, n = [], len(nums)

        i = 0
        while i < n:
            j = 1 + i
            while j < n and nums[i] == nums[j]:
                j += 1
            if n // 3 < (j - i):
                res.append(nums[i])
            i = j
        return res
                

