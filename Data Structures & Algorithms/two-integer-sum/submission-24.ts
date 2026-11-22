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
                // if we had this in strict, we need to handle undefined
                const j = mem.get(diff) 
                if (j !== undefined) {
                    return [j, i]
                }
            }
            mem.set(nums[i], i)
        }
    }
}
