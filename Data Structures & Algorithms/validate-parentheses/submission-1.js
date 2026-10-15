class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
        const checker = new Map();
        let arr = [];
        checker.set(']', '[');
        checker.set('}', '{');
        checker.set(')', '(');

        for (let char of s) {
            if (char === '(' || char === '{' || char === '['){
                arr.push(char);
            } else {
                if (arr.length === 0) {
                    return false
                } else {
                    let lastChar = arr[arr.length - 1];
                    if (lastChar === checker.get(char)){
                        arr.pop();
                        } else {
                            return false;
                                }}}
        }
        return arr.length === 0;

    
    }
}
