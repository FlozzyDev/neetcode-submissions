class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # make 2 dict
        sDict, tDict = {}, {}
        # Loop each word to add to dict
        for i in range(len(s)):
            sDict[s[i]] = 1 + sDict.get(s[i], 0)
            tDict[t[i]] = 1 + tDict.get(t[i], 0)

        # compare dic
        return sDict == tDict
        

             
        