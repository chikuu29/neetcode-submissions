class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        f={}
        for i in nums:
            f[i]=f.get(i,0)+1

        flist=[ list(i) for i in f.items()]
        flist.sort(key=lambda x:x[1],reverse=True)

        result=[]
        for i in range(len(flist)):
            if i ==k:
                break
            result.append(flist[i][0])
        

        return result

        



        