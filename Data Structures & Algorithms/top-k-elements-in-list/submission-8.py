class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for n in nums:
            d[n] = 1 + d.get(n, 0)
        return sorted(d, key=d.get, reverse=True)[:k]
            
        

        
        

        
        




