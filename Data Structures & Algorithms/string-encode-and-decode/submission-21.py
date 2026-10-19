class Solution: # count 3
    def encode(self, strs: list[str]) -> str:
        return "".join(f"{len(w)}#{w}" for w in strs)

    def decode(self, s:str) -> list[str]:
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
