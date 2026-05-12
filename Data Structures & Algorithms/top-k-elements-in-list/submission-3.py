class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hs = defaultdict(int)
        res = []
        for n in nums:
            hs[n] += 1
        heap = []
        for n in hs.keys():
            heapq.heappush(heap, (hs[n], n))
            if len(heap) > k:
                heapq.heappop(heap)
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res