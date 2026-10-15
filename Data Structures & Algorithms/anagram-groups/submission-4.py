from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        memBank = defaultdict(list)
        for word in strs:
            dict_key = tuple(sorted(word))
            memBank[dict_key].append(word)
        return list(memBank.values())

            

