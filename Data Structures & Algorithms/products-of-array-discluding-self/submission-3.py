class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # hashmap (dict)
        # iterate over nums with 2 loops
        # hashmap[num] -> product

        # [0, 0]
        # [1,2,4,6,4]

        # [192,96,48,32,48]

        hm = {}
        response = []
        for i in range(len(nums)):
            curr = nums[i] # 0
            product = 1
            for j in range(len(nums)):
                if j == i:
                    continue
                
                newCurr = nums[j] # 0

                product *= newCurr
            
            response.append(product)
        
        return response
                    

        