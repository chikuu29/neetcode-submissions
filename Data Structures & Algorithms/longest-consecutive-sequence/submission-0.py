class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest=0
        arraySet= set(nums)
        for i in nums:
            cval=i
            if i-1 not in arraySet:
                cl=1
                while cval+1 in arraySet:
                    cl+=1
                    cval+=1
                longest = max(cl,longest)
        return longest

        