"""
659. Encode and Decode Strings
Design an algorithm to encode a list of strings to a string. 
The encoded string is then sent over the network and is decoded back to the original list of strings. 
Please implement encode and decode
"""
class Solution:

    def encode(self, strs) -> str:
        outputStr = ''
        for s in strs:
            outputStr += str(len(s)) + "#" + s
        return outputStr

    def decode(self, s: str):
        outputLst = []
        i = 0
        while i < len(s):
            if s[i].isdigit():
                wordLen = int(s[i])
                start = i + 2
                end = i + 2 + wordLen
                outputLst.append(s[start:end])
            i = i + 2 + wordLen
        return outputLst


Input = ["neet","code","love","you"]
Output = ["neet","code","love","you"]
obj = Solution()
s = obj.encode(Input)
d = obj.decode(s)

print("encoded: ", s)
print("decoded: ", d)

