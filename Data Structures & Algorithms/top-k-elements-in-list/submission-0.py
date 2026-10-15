class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        memBank = {}
        for i in range(len(nums)):
            if nums[i] in memBank:
                memBank[nums[i]] += 1
            else: 
                memBank[nums[i]] = 1
        sortedList = sorted(memBank.items(), key=lambda x: x[1])[-k:]
        result = [pair[0] for pair in sortedList]
        return result




