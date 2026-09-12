class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        f={}
        for i in nums:
            f[i]=f.get(i,0)+1

        bucket=[[] for _ in range(n+1)]
        for v,c in f.items():
            bucket[c].append(v)
        result=[]

        for i in range(n,0,-1):
            for j in bucket[i]:
                result.append(j)
                if len(result)==k:
                    return result
            

        

        return result
        

        