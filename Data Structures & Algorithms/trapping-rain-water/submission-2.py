class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        i, j = 0, len(height)-1
        s = 0
        rightMax, leftMax = height[j], height[i];
        while (i < j):
            if (leftMax < rightMax):
                i+=1
                leftMax = max(leftMax, height[i])
                s += leftMax - height[i]
            else:
                j-=1
                rightMax = max(rightMax, height[j])
                s += rightMax - height[j]
        return s