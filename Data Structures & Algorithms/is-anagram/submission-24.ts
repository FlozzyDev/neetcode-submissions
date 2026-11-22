class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s: string, t: string): boolean {
        // first check length
        if (s.length < t.length) {
            return false;
        }
        // create a 26 length array of 0
        const count = new Array(26).fill(0)
        // walk through each array and add 1 per letter. Do the same and remove 1.
        for (let i = 0; i < s.length; i++) {
            count[s.charCodeAt(i) - 'a'.charCodeAt(0)]++;
            count[t.charCodeAt(i) - 'a'.charCodeAt(0)]--;
        }
        // verify the array is all 0's
        return count.every((val) => val === 0)
    }
}
