class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        numIdxMap = {}
        for i in range(len(nums)):
            curr = nums[i]
            diff = target - curr

            if diff in numIdxMap and i != numIdxMap[diff]:
                return [min(i, numIdxMap[diff]), max(i, numIdxMap[diff])]
            
            numIdxMap[nums[i]] = i
        
        
        