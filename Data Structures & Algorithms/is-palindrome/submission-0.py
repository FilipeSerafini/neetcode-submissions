class Solution:
    def isPalindrome(self, s: str) -> bool:

        alphaNum = []
        for c in s:
            if c.isalnum():
                alphaNum.append(c.lower())
            
        print(str(alphaNum))

        j = len(alphaNum) -1
        for i in range(len(alphaNum)):
            if i > j:
                break

            if alphaNum[i] != alphaNum[j]: # t t, a a, b c
                return False
            
            j -= 1
        
        return True
