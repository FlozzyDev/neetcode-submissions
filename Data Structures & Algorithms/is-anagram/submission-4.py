class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # make 2 dict
        sDict, tDict = {}, {}
        # Loop each word to add to dict
        for char in s:
            if char in sDict:
                sDict[char] += 1
            else:
                sDict[char] = 1

        for char in t:
            if char in tDict:
                tDict[char] += 1
            else:
                tDict[char] = 1

        # compare dic
        return sDict == tDict

             
        