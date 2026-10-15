class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        memBank = {}

        for word in strs:
            key = ''.join(sorted(word))
            if key not in memBank:
                memBank[key] = [word]
            else:
                memBank[key].append(word)
                
        return list(memBank.values())

            

