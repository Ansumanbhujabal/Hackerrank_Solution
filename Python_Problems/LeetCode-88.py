class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1[m:]=nums2  ## nums1[m:]  gets all content of nums1, after m: th index , the content of num2 are added 
        nums1.sort()
