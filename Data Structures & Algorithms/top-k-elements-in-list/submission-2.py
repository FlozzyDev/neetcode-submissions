class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # part 1 - count frequency
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        # part 2 - build frequency
        freq = [[] for i in range(len(nums) +1)]
        for n, c in count.items():
            freq[c].append(n)
        
        # part 3 - build return array
        res = []
        for i in range(len(freq) -1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

        
        

        
        




