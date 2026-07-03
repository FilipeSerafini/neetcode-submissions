class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # store numbers in hash map with num: idx
        # iterate over nums and check if target - nums[i] exists in hash map
        # if so, get index

        numsMap = {}
        for i in range(len(nums)):
            curr = nums[i]
            numsMap[curr] = i

        # [5, 4, 3, 6]
        # numsMap = {5:0, 4:1, 3:2, 6:3}
        # target: 8
        for i in range(len(nums)):
            curr = nums[i]
            diff = target - curr
            if diff in numsMap and i != numsMap[diff]: # 8 - 5 = 3
                return [min(i, numsMap[diff]), max(i, numsMap[diff])]



            