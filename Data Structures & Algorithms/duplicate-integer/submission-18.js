class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    // Count 3
    hasDuplicate(nums) {
        return new Set(nums).size < nums.length
    }
}
