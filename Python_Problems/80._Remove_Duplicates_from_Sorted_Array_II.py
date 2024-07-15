class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # num=sorted(nums)
        # for value in num:
        #     if num.count(value)>2:
        #         num.remove(value)
        # nums[:]=num        
        # return(len(num))  # Do not allocate extra space for another array        constarint 
        if len(nums)<=2:
            return len(nums)
        j=2
        for i in range(2,len(sorted(nums))):
            if nums[i]!=nums[j-2]:  ## if current element is not same as 
                nums[j]=nums[i]
                j+=1    
        return j         
