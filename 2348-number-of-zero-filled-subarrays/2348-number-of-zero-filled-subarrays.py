class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        sNum = 0
        ans = 0
        
        for i in range(len(nums)):
            
            if(nums[i] == 0):
                sNum += 1
                ans += sNum
            else:
                sNum = 0
        
        return ans
                
                
        