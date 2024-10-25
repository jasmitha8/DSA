class Solution:
    def threeSum(self, nums):
        nums.sort()
        result = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:  # skip duplicate triplets
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                # 2sum algorithm
                threesome = nums[l] + nums[r] + nums[i]
                if threesome == 0:
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # Skip duplicates in 2sum
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif threesome > 0:
                    r -= 1
                else:
                    l += 1
        return result
    

if __name__ == "__main__":
    obj = Solution()
    print(obj.threeSum([-1,0,1,2,-1,-4]))   # [[-1, -1, 2], [-1, 0, 1]]
