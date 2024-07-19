class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return[int(i) for i in str(int("".join([str(x)for x in digits]))+1)]
        ## for number in digts 
        # get number 
        # join  str fo that
        # +1  int for that 
        # str 
        # int 
