class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if len(stack) == 0:
                stack.append(s[i])
                continue
            if s[i] == "]" and stack[-1] == "[":
                stack.pop()
                continue
            if s[i] == "}" and stack[-1] == "{":
                stack.pop()
                continue
            if s[i] == ")" and stack[-1] == "(":
                stack.pop()
                continue
            stack.append(s[i])
            
        if len(stack) == 0:
            return True
        else:
            return False
            