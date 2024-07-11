class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for num in sorted(nums): ## sort 1st 
            if val==num:
                nums.remove(val)  # remove by value 
        return len(nums)        
                
        
