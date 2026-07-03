class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       # check lengths
       # create map for each string being char: count

        if len(s) != len(t):
            return False

        countMapS, countMapT = {}, {}
        for i in range(len(s)):
            countMapS[s[i]] = 1 + countMapS.get(s[i], 0)
            countMapT[t[i]] = 1 + countMapT.get(t[i], 0)
        
        for k in countMapS:
            if k not in countMapT:
                return False
            
            if countMapT[k] != countMapS[k]:
                return False
        
        return True

