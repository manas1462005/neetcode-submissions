class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low=0
        high=len(nums)-1
        while low<=high:
            s=(low+high)//2
            if nums[s]>target:
                high=s-1
            elif nums[s]<target:
                low=s+1
            else:
                return s
        return -1