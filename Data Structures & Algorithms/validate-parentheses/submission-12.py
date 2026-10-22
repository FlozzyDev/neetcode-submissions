class Solution:
    def isValid(self, s: str) -> bool:
        # count 5
        stack = []
        mem = {")" : "(",  "]" : "[", "}" : "{"}

        for c in s:
            if c in mem:
                if stack and stack[-1] == mem[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False

    
            