class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            summed = numbers[l] + numbers[r]
            match summed:
                case summed if summed < target:
                    l+=1
                case summed if summed > target:
                    r-=1
                case target:
                    return [l+1, r+1]
