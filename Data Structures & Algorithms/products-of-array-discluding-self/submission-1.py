class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product, zeroCt = 1, 0

        for num in nums:
            if num == 0:
                zeroCt += 1
                if zeroCt >= 2:
                    return [0] * len(nums)
            else:
                product *= num

        res = []
        for i, c in enumerate(nums):
            if c == 0:
                res = [0] * len(nums)
                res[i] = product
                return res
            else:
                res.append(int(product // c))
        return res
            
                    
            
            
            

        
        