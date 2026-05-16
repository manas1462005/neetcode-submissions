class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for n in nums:
            freq[n]=freq.get(n,0)+1
        import heapq
        max_heap=[]
        for n,c in freq.items():
            heapq.heappush(max_heap,(-c,n))
        result=[]
        for _ in range(k):
            result.append(heapq.heappop(max_heap)[1])

        return result