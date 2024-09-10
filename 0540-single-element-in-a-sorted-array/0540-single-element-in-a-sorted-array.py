class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        ans = {}
        for num in nums:
            if num in ans:
                ans[num] += 1  
            else:
                ans[num] = 1
        
       
        for num, count in ans.items():
            if count == 1:
                return num
