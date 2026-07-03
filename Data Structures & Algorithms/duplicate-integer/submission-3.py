class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        hm = {}

        for number in nums:
            if number not in hm:
                hm[number] = hm.get(number, 0) + 1
            else:
                return True

        return False