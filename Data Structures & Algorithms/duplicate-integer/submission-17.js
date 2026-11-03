class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    // Count 2
    hasDuplicate(nums) {
    return new Set(nums).size < nums.length
    }
}
