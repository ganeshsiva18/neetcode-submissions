class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = 1
        while True:
            if i == j:
                j += 1
                continue
            if j >= len(numbers):
                j = 0
                i += 1
            cursum = numbers[i] + numbers[j]
            match cursum:
                case cursum if cursum > target:
                    j = 0
                    i += 1
                case cursum if cursum < target:
                    j += 1
                case target:
                    return [i+1, j+1]
        return [-1, -1]