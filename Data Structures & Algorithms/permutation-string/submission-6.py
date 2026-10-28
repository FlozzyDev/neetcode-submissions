class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # count 3
        l1 = len(s1)
        l2 = len(s2)

        if l1 > l2:
            return False
        
        s1_count = [0] * 26
        s2_count = [0] * 26

        for i in range(l1):
            s1_count[ord(s1[i]) - 97] += 1
            s2_count[ord(s2[i]) - 97] += 1
        
        if s1_count == s2_count:
            return True
        
        for i in range(l1, l2):
            s2_count[ord(s2[i]) - 97] += 1
            s2_count[ord(s2[i - l1]) - 97] -= 1
            if s1_count == s2_count:
                return True
        return False
            
        
             

            
            
        
