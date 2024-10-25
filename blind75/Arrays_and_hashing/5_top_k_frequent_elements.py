from collections import Counter
from heapq import heapify, heappop
class Solution:
    def topKFrequent(self, nums, k: int):
        numsDict = Counter(nums)
        numsTuple = []
        output = []
        for key, value in numsDict.items():
            numsTuple.append((value, key))

        numsSort = sorted(numsTuple, reverse=True)
        
        for i in range(k):
            output.append(numsSort[i][1])

        return output
    
    def optimizedTopKFrequent(self, nums, k):
        numsDict = Counter(nums)
        numsList = []
        output = []

        for key, value in numsDict.items():
            numsList.append((-value, key))      # negative value for max heap
        
        heapify(numsList)
        output = [heappop(numsList)[1] for _ in range(k)]
        return output

nums = [3,0,1,0]
k = 1
obj = Solution()
print(obj.topKFrequent(nums, k))    # [0]
print(obj.optimizedTopKFrequent(nums, k))
