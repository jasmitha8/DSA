class Solution:
    def maxArea(self, height):
        maxArea = -float('inf')
        for ht in range(len(height)):
            l = ht
            r = ht + 1
            while r < len(height):
                maxHeight = min(height[l], height[r])
                maxArea = max(maxArea, maxHeight * (r - l))
                r += 1
        return maxArea
    
    def optimizedMaxArea(self, height) -> int:
        maxArea = -float('inf')
        l, r = 0, len(height) - 1
        while l < r:
            maxHeight = min(height[l], height[r])
            maxArea = max(maxArea, maxHeight * (r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxArea
    

if __name__ == "__main__":
    obj = Solution()
    print(obj.maxArea([1,8,6,2,5,4,8,3,7]))
    print(obj.optimizedMaxArea([1,8,6,2,5,4,8,3,7]))