class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # n log n
        # [5, 4, 3, 6]
        # [[3, 2], [4, 1], [5, 0], [6, 3]]

        arr = []
        for i in range(len(nums)):
            arr.append([nums[i], i])

        arr.sort() # n log n
        # [[3, 2], [4, 1], [5, 0], [6, 3]]

        i = 0
        j = len(nums) - 1
        while i < j:
            currSum = arr[i][0] + arr[j][0]
            if currSum > target:
                j -= 1
            elif currSum < target:
                i += 1

            if currSum == target:
                return [min(arr[i][1], arr[j][1]), max(arr[i][1], arr[j][1])]

        
        
    