class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        let string1 = s;
        let string2 = t;
        let arr1 = string1.trim().split('');
        let arr2 = string2.trim().split('');

        if (arr1.length !== arr2.length){
            return false;
        } else {
            arr1.sort();
            arr2.sort();
            for (let i = 0; i < arr1.length; i++){
                if (arr1[i] !== arr2[i]){
                    return false;
                } 
            }
        }
        return true;
    }
}
