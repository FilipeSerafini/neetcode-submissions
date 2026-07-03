class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # store in map -> {num: idx, num2: idx2}
        # iterate over nums and check if diff between target - curr exists on map

        numIdxMap = {}
        for i in range(len(nums)):
            curr = nums[i]
            diff = target - curr

            if diff in numIdxMap and i != numIdxMap[diff]:
                return[numIdxMap[diff], i]  
            
            numIdxMap[curr] = i
        
    