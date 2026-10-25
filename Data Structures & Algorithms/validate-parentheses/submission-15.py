class Solution:
    def isValid(self, s: str) -> bool:
        # count 6
        stack = []
        mem = {")" : "(", "}" : "{", "]" : "[" }

        for v in s:
            if v in mem and stack:
                if mem[v] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(v)
        return True if not stack else False

    
            