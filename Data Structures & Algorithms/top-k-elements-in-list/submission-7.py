import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # [1, 1, 1, 2, 3, 3]
        hm = {}
        for n in nums:
            hm[n] = 1 + hm.get(n, 0)
        
        # hm -> {1:3, 2:1, 3:2}

        heap = []
        for num, count in hm.items():
            heapq.heappush(heap, [count, num])

            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        while len(res) < k:
            res.append(heapq.heappop(heap)[1])
        
        return res