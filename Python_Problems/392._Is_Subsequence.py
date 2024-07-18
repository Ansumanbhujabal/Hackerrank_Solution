class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # for i in s:
        #     if i not in t:
        #         return False
        #     t.replace(i,'',1)    
        # return True 
        it=iter(t)
        return all(char in it for char in s) 
