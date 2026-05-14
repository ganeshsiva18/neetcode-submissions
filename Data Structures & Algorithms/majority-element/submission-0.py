class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        tab = defaultdict(int)
        for n in nums:
            tab[n] += 1
        tab = sorted(tab.items(), key=lambda item:item[1], reverse=True)
        return tab[0][0]