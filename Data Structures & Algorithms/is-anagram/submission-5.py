class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False


        # racecar
        # [[r,2], [a,2], [c,2], [e, 1]]
        hmS = {}
        for char in s:
            hmS[char] = hmS.get(char, 0) + 1

        hmT = {}
        for char in t:
            hmT[char] = hmT.get(char, 0) + 1
        
        if hmS == hmT:
            return True
        else:
            return False