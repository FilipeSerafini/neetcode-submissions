class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        res = 1
        store = set(nums)
        nxt = 0
        for num in store:
            if num - 1 not in store:
                continue
            
            currStreak = 2
            nxt = num + 1
            while nxt in store:
                currStreak += 1
                nxt += 1
            
            res = max(res, currStreak)
        
        return res
            
                
