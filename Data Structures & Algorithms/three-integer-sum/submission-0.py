class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # [ -1, 0, 1, 2, -1, -4]
        # i = -1
        # j = 0 
        # k = -1

        res = []
        checkMap = {}
        count = 0
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if j == i:
                    continue
                for k in range(2, len(nums)):
                    if k == j or k == i:
                        continue
                    
                    currTriplet = [nums[i], nums[j], nums[k]]
                    currTriplet.sort()

                    if nums[i] + nums[j] + nums[k] == 0:
                        if currTriplet not in checkMap.values():
                            checkMap[count] = currTriplet
                            count += 1
                            res.append(currTriplet)

        return res

