class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # store in map -> {num: idx, num2: idx2}
        # iterate over nums and check if diff between target - curr exists on map

        numIdxMap = {}
        for i in range(len(nums)):
            numIdxMap[nums[i]] = i
        
        # [3, 4, 5, 6]
        # {3:0, 4:1, 5:2, 6:3}
        # [1, 3, 4, 2] target = 6
        # {1:0, 3:1, 4:2, 2:3}

        for i in range(len(nums)):
            curr = nums[i]
            diff = target - curr

            if diff in numIdxMap and i != numIdxMap[diff]:
                return[i, numIdxMap[diff]]            
        
    