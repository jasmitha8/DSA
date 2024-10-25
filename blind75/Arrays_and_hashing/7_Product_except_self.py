class Solution:
    def productExceptSelf(self, nums):
        prefix, postfix = [1] * len(nums), [1] * len(nums)
        output = []
        for i in range(1, len(nums)):
            pre = prefix[i - 1]
            prefix[i] = pre * nums[i - 1]
        for i in range(len(nums) - 2, -1, -1):
            post = postfix[i + 1]
            postfix[i] = post * nums[i + 1]
        
        for i in range(len(nums)):
            output.append(prefix[i] * postfix[i])
        return output
    
    def optimizedProductExceptSelf(self, nums):
        prefix = [1] * len(nums)
        for i in range(1, len(nums)):
            pre = prefix[i - 1]
            prefix[i] = pre * nums[i - 1]
        
        post = 1
        for i in range(len(nums) - 1, -1, -1):
            prefix[i] = post * prefix[i]
            post = post * nums[i]

        return prefix


if __name__ == '__main__':
    obj = Solution()
    print(obj.productExceptSelf([-1,1,0,-3,3]))   # [0,0,9,0,0]
    print(obj.optimizedProductExceptSelf([1,2,3,4]))    # [24, 12, 8, 6]
