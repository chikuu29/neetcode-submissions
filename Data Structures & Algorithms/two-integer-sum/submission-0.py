class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        output = []
        for i,num in enumerate(nums):
            need = target-num
            if need in seen:
                output =[seen[need],i]
            
            seen[num]=i
        
        return output

        