class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0  ## Using Booyer Moore approach 
        for num in nums:
            if count==0:
                val=num
            count+=(1 if num ==val else -1 )    ## reward and penalty 
        return val  ## the only one wiith +ve count 
  
        
