class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums: number[], target: number): number[] {
        const mem = new Map <number, number>();

        for (let i = 0; i < nums.length; i++) {
            const diff: number = target - nums[i]
            if (mem.has(diff)) {
                return [mem.get(diff), i]
            }
            mem.set(nums[i], i)
        }
    }
}
