class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedString = ""
        for s in strs:
            encodedString += str(len(s)) + "π" + s
        return encodedString

    def decode(self, s: str) -> List[str]:
        decode = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "π":
                j += 1
            length = int(s[i:j])
            decode.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return decode
