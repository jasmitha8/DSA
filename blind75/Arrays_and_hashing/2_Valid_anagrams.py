"""
242. Valid Anagram
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
"""

from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sDict = defaultdict(int)
        tDict = defaultdict(int)
        for c in s:
            sDict[ord(c)] += 1
        for c in t:
            tDict[ord(c)] += 1
        return sDict == tDict
    

s = "anagram"
t = "nagaram"   # True
obj = Solution()
obj.isAnagram(s, t)