class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mem = defaultdict(list)

        for word in strs:
            key = "".join(sorted(word))
            mem[key].append(word)

        return list(mem.values())
        

        
        

        

            

