class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mySet = set()
        l, longest = 0, 0, 

        for r in range(len(s)):
            while s[r] in mySet:
                mySet.remove(s[l])
                l += 1
            mySet.add(s[r])
            longest = max(r-l+1, longest)
        
        return longest

