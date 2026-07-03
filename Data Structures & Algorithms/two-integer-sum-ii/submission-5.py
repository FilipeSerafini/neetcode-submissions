class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #  i           j 
        # [1, 2, 2, 3, 3] - target = 3
        #  1 + 3 > target -> j -= 1
        # [1, 2, 2, 3, 4, 4] - target = 6
        #  1 + 4 < target -> i += 1

        i = 0
        j = len(numbers) - 1

        while i < j:
            if numbers[i] + numbers[j] == target:
                return [i+1, j+1]
            
            if numbers[i] + numbers[j] > target:
                j -= 1
                continue
            
            if numbers[i] + numbers[j] < target:
                i += 1
                continue
            
