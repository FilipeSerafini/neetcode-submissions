class Solution:
    def isPalindrome(self, s: str) -> bool:

        # i                         j  
        # Was it a car or a cat I saw?

        lowerS = s.lower()

        i = 0 
        j = len(s) - 1 # 27

        while i < j:
            if not self.isAlphaNum(lowerS[i]):
                i += 1
                continue
            
            if not self.isAlphaNum(lowerS[j]):
                j -= 1
                continue
            
            if lowerS[i] != lowerS[j]:
                return False
            
            i += 1
            j -= 1
        
        return True
    
    def isAlphaNum(self, c) -> bool:

        # check if c's ASCII value is between ranges A-Z, a-z or 0-9
        
        return ((ord("A") <= ord(c) <= ord("Z")) or
                (ord("a") <= ord(c) <= ord("z")) or 
                (ord("0") <= ord(c) <= ord("9")))



        