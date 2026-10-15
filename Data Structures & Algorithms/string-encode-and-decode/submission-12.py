class Solution:

    def encode(self, strs: List[str]) -> strs:
        # Set a empty string var
        encodedString = ""
        # Loop through each word, append it to the return string
        # We need to first get it's length + add a delimeter
        for word in strs:
            encodedString += str(len(word)) + "#" + word
        return encodedString
        




    def decode(self, s: str) -> List[str]:
        # create a list, create an index
        res = []
        i = 0

        # loop through all characters
        while i < len(s):
            # set j to the index of delimter
            j = s.index("#", i)
            #set length value to word length
            length = int(s[i:j])
            # append the word using j + 1 -> j + 1 + length
            res.append(s[j+1 : j + 1 + length])
            # set i to the last value we used
            i = j + 1 + length
        return res

            

