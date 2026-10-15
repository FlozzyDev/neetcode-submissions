class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number}
     */
    search(nums, target) {
        if (nums.length == 0){
            return -1; 
        }
        if (nums[0] === target){
            return 0;
        }
        

        let l = 0;
        let r = nums.length - 1;
        while (l < r) {
            if (nums[l] === target){
                return l;
            }
            if (nums[r] === target) {
                return r;
            }
            const mid = Math.floor((l + r) / 2);
            if(nums[mid] === target) {
                return mid;
            }
            if (nums[mid] < target){
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }
        return -1;
    }
}
