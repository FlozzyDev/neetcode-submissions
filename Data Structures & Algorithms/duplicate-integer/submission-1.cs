public class Solution {
    public bool hasDuplicate(int[] nums) {

        HashSet<int> hs = new HashSet<int>();
        foreach(int n in nums) {
            hs.Add(n);
        }
        if (hs.Count != nums.Length)
            return true;
        else
            return false;
    }
}
