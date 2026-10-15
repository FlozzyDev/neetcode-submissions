class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        memBank = defaultdict(list)

        for word in strs:
            key = ''.join(sorted(word))
            memBank[key].append(word)
        return list(memBank.values())
            

