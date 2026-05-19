class Solution:
    def trap(self, height: List[int]) -> int:
        if height == 0:
            return 0
        
        s = 0
        l, r = 0, len(height) - 1
        maxL, maxR = height[l], height[r]
        
        while l < r:
            if height[l] < height[r]:
                l += 1
                maxL = max(maxL, height[l])
                s += (maxL - height[l])
            else:
                r -= 1
                maxR = max(maxR, height[r])
                s += (maxR - height[r])
        return s