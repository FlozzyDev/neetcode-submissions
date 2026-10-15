class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        myDict = {}
        res = []
        for i in range(len(numbers)):
            a = target - numbers[i]
            if a in myDict:
                res.append(myDict[a])
                res.append(i + 1)
            else:
                myDict[numbers[i]] = i + 1
        return res