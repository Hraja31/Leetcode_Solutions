class Solution:  
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        arr = [1]*n
        for i in range(n):
            for j in range(i):
                if nums[i]>nums[j] and arr[i]<arr[j]+1:
                    arr[i]=arr[j]+1
        return max(arr)
