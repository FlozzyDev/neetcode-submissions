class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const bank = new Map();

        for (let i = 0; i < nums.length; i++){
            let comp = target - nums[i];

            if(bank.has(comp)){
                const j = bank.get(comp);
                return [j , i];
            } 
            bank.set(nums[i], i);
        } 
        return[]
    } 

}
