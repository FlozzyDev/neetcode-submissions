class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs: string[]): string[][] {
        const mem = new Map<string, string[]>();
        for (const word of strs) {
            const key: number[] = new Array(26).fill(0)
            for (const char of word) {
                key[char.charCodeAt(0) - 'a'.charCodeAt(0)]++;
            }
            const k = key.join('.');
            const group = mem.get(k)
            if (group !== undefined) {
                group.push(word)
            } else {
                mem.set(k, [word])
            }
        }
        return Array.from(mem.values())
    }
}
