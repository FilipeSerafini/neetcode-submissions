class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        arr = []
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if i == j:
                    continue
                print(i)
                print(j)
                print("divid")
                if nums[i] + nums[j] == target:
                    return [i, j]
        
        
        