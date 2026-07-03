class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # [5, 4, 3, 6]
        arr = []
        for i in range(len(nums)):
            num = nums[i]
            arr.append([num, i])

        # [[5, 0], [4, 1], [3, 2], [6, 3]]
        arr.sort() 
        # [[4, 1], [3, 2], [5, 0], [6, 3]]
        # 2 pointers

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


            