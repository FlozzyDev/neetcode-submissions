class Solution:
    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(w)}#{w}" for w in strs)
    
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = s.index("#", i)
            length = int(s[i:j])
            start = j + 1
            end = start + length
            res.append(s[start:end])
            i = end
        return res

        