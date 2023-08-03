class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=0
        for i in nums:
            if n<2 or i>nums[n-2]:
                nums[n] = i
                n+=1
        return n
