class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        res=[]
        for i in nums:
            freq[i]=freq.get(i,0)+1
        arr = sorted(freq.items(),key=lambda x: x[1], reverse=True)
        
        for i in range(k):
            res.append(arr[i][0])
        return res
