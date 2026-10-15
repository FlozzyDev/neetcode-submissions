class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if they aren't the same length, it's false
        if len(s) != len(t):
            return False
        # create 2 dict
        sBank, tBank = {}, {}
        # loop through both, set letters to 1 and add if there was already existing
        for i in range(len(s)):
            sBank[s[i]] = 1 + sBank.get(s[i], 0)
            tBank[t[i]] = 1 + tBank.get(t[i], 0)
        # compare both dicts
        return sBank == tBank
        

             
        