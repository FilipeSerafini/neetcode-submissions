class Solution:
    def isValid(self, s: str) -> bool:

        opens = ["(", "{", "["]
        stack = []
        for brkt in s:
            if brkt in opens:
                stack.append(brkt)
            else: 
                if len(stack) == 0:
                    return False

                last = stack.pop()
                if last == "{" and brkt != "}":
                    return False
                if last == "[" and brkt != "]":
                    return False
                if last == "(" and brkt != ")":
                    return False

        if len(stack) > 0:
            return False

        return True
