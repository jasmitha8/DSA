"""
49. Group Anagrams

Given an array of strings strs, group the anagrams together. You can return the answer in any order.
"""


from collections import defaultdict, Counter
class Solution:
    def groupAnagrams(self, strs):
        """
        O(n * nlogn)
        """
        anagram = defaultdict(list)
        for s in strs:
            anagram[''.join(sorted(s))].append(s)
        return anagram.values()
    
    def optimizedGroupAnagrams(self, strs):
        """
        O(nlogn)
        """
        anagram = defaultdict(list)
        for s in strs:
            characters = [0] * 26

            for c in s:
                characters[ord(c) - ord('a')] += 1
                
            anagram[tuple(characters)].append(s)
        return anagram.values()


strs = ["eat","tea","tan","ate","nat","bat"]
output = [["eat","tea","ate"],["tan","nat"],["bat"]]
obj = Solution
obj.groupAnagrams(strs)
obj.optimizedGroupAnagrams(strs)
