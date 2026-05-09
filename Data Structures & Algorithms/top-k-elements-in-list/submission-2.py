class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        for n in nums:
            hashmap[n] += 1
        heapy = []
        for num in hashmap.keys():
            heapq.heappush(heapy, (hashmap[num], num))
            if len(heapy) > k:
                heapq.heappop(heapy)
        res = []
        for i in range(k):
            res.append(heapq.heappop(heapy)[1])
        return res