class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        num=list(sorted(set(nums)))  
        ## set uses hash value to order , so first set then sort 
        nums[:]=num  # this will work as , it overwrites nums
        return len(nums)
