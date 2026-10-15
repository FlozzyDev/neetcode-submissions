class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count steps
        count = {}
        # for loop to count each numbers freq
        for n in nums:
            count[n] = 1 + count.get(n,0)
        
        # step 2 - create freq array + fill it
        freq = [[] for i in range(len(nums) + 1)]
        for n, c in count.items():
            freq[c].append(n)

        # step 3 - Create res[] and append values to it
        res = []
        for i in range(len(freq) -1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
            
        

        
        

        
        




