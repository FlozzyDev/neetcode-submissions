class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # count 3
        mem = defaultdict(list)

        for word in strs:
            key = [0] * 26
            for char in word:
                key[ord(char) - ord("a")] += 1
            mem[tuple(key)].append(word)
        return list(mem.values())
        

        

        
        

        

            

