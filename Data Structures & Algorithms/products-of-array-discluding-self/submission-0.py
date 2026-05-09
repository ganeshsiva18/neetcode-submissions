class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        fin = []
        for i in range(len(nums)):
            fin.append(math.prod(nums[:i]+nums[i+1:]))
        return fin
