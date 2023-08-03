class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=0
        for i in nums:
            if i>nums[n-1] or n==0:
                nums[n] = i
                n+=1
        return n
