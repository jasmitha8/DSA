class Solution:
    def findMin(self, nums):
        mini = nums[0]
        l, r = 1, len(nums) - 1
        while l <= r:
            # base condition: array is sorted, return the first element
            if nums[l] < nums[r]:
                mini = min(mini, nums[l])
                return mini
            
            # Binary search
            m = (l + r) // 2
            mini = min(mini, nums[m])
            if nums[m] >= nums[l]: 
            # m is in the subarray with greater values after rotation, 
            # go left where there are smaller values 
                l = m + 1
            else:
            # m is in the subarray with smaller values, 
            # keey going right to find even smaller values
                r = r - 1
        return mini
    

if __name__ == "__main__":
    obj = Solution()
    print(obj.findMin([4,5,6,7,0,1,2]))
        