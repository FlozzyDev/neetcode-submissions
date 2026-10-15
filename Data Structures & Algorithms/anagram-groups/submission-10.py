class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #way 1 - join string / way 2 - count ord

        # init defaultdict
        mem = defaultdict(list)
        # loop each word
        for word in strs:
        
        # join or count?
            key = ''.join(sorted(word))
            mem[key].append(word)
            
        # return list of dict values
        return list(mem.values())
        

        
        

        

            

