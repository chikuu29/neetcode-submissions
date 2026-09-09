class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hasmap=set()
        output= False
        for i in nums:
            if i in hasmap:
                output=True
                break
            else:
                hasmap.add(i)



        return output


        