class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixArray= [1]*len(nums)
        prefix=1
        for i in range(len(nums)):
            prefixArray[i]=prefix
            prefix*=nums[i]
        
        sufix=1

        for i in range(len(nums)-1,-1,-1):
            prefixArray[i]*=sufix
            sufix*=nums[i]
        return prefixArray