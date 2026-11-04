class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        // count 3
        const mem = new Map()
        for (let i = 0; i < nums.length; i++) {
            const diff = target - nums[i]
            if (mem.has(diff)) {
                return [mem.get(diff), i]
            } else {
                mem.set(nums[i], i)
            }
        }
        return []
    }
}