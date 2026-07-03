class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCount = {}
        for n in nums:
            numCount[n] = 1 + numCount.get(n, 0)

        arr = []
        for num, cnt in numCount.items():
            arr.append([cnt, num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        
        return res