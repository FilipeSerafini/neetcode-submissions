class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # store original numbers and indexes
        # sort array
        # use 2 pointers to find the numbers

        # target 8
        # [5, 3, 6, 4]
        arr = [] # [[3, 0], [5, 1], [6, 2], [4, 3]]
        for i in range(len(nums)):
            arr.append([nums[i], i])

        arr.sort()
        # [[3, 1], [4, 3], [5, 0], [6, 2]]

        i = 0
        j = len(nums) - 1

        while i < j:
            currSum = arr[i][0] + arr[j][0]
            if currSum == target:
                return [min(arr[i][1], arr[j][1]), max(arr[i][1], arr[j][1])]

            if currSum > target:
                j -= 1
            
            if currSum < target:
                i += 1

            