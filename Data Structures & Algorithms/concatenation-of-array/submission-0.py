class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        newa = [0]*(n*2)
        for i in range(n):
            newa[i] = nums[i]
            newa[i+n] = newa[i]
        return newa