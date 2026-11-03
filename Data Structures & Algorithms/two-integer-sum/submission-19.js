class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        // count 1
        const bank = new Map()
        for (let i = 0; i < nums.length; i++) {
            const num = nums[i]
            const diff = target - num
            if (bank.has(diff)) {
                return [bank.get(diff), i]
            }
            bank.set(num, i)
        }
        return []
    }

}