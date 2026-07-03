class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hm = {}
        for s in strs:
            srtd = str(sorted(s))
            
            if srtd in hm:
                hm[srtd].append(s)
            else:    
                hm[srtd] = [s]
        
        toReturn = []
        for key in hm:
            toReturn.append(hm[key])
        
        return toReturn
        