class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mainBank = {}
        for i in range(len(strs)):
            word = strs[i]
            checkValue = tuple(sorted(word))
            if checkValue in mainBank:
                mainBank[checkValue].append(strs[i])
            else:
                mainBank[checkValue] = [strs[i]]
        return list(mainBank.values())
            

