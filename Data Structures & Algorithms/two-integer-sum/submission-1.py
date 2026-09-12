class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hasmap={}
        output=[]
        for i in range(len(nums)):
            remider=target-nums[i]
            if remider in hasmap:
                output = [hasmap[remider],i]
            hasmap[nums[i]]=i
        return output


        