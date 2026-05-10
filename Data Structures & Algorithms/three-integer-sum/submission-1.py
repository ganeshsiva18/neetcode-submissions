class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        fin = []
        nums.sort()

        for i in range(len(nums)):
            if (nums[i]>0):
                break
            if (i > 0 and nums[i] == nums[i-1]):
                continue
            l, r = i+1, len(nums)-1
            while l<r:
                s = nums[l]+nums[r]+nums[i]
                match s:
                    case s if s > 0:
                        r -= 1
                    case s if s < 0:
                        l += 1
                    case _:
                        fin.append([nums[i], nums[r], nums[l]])
                        r -= 1
                        l += 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
        return fin