class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        for n in nums:
            hashmap[n] += 1
        arr = []
        for num, amt in hashmap.items():
            arr.append([amt, num])
        arr.sort()
        res = []
        for i in range(k):
            res.append(arr.pop()[1])
        return res