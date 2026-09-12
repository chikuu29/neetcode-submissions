class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        shas= [0]*26
        thas= [0]*26
        for i in s:
            shas[ord(i)-ord('a')]+=1
        for i in t:
            thas[ord(i)-ord('a')]+=1

        return shas==thas
        