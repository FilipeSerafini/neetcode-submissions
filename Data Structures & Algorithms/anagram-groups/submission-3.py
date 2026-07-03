class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hm = {}
        for s in strs:
            sortedString = str(sorted(s))

            if sortedString in hm:
                hm[sortedString].append(s)
            else:
                hm[sortedString] = [s]
        
        res = []
        for key, value in hm.items():
            res.append(value)

        return res


        