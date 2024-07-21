class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # count=0
        # for i  in range(len(ransomNote)):
        #     if ransomNote[i]== magazine[i]:
        #             count+=1
        # return count==len(ransomNote)
        # if magazine or magazine[::-1] in ransomNote

        # if ransomNote  in magazine:
        #     return True
        # elif ransomNote[::-1]  in magazine:
        #     return True
        # else:
        #     return False
        # return  ransomNote  in magazine

      ##################################################
        count=0
        for i in ransomNote:
            if int(magazine.count(i))>=int(ransomNote.count(i)):
                count+=1
        return count==len(ransomNote)   
      ## or  ################################################
        return Counter(ransomNote) <= Counter(magazine)   ## as it keeps the original ordering   
