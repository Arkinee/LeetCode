class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        ans = 0
        isAvail = True
        
        for i in range(len(flowerbed)):
            temp = flowerbed[i]
            
            if(temp == 0):
                if(isAvail):
                    ans += 1
                    isAvail = False
                    continue
                else:
                    isAvail = True
                    continue
            else:
                if(isAvail):
                    isAvail = False
                else:
                    ans -= 1
                
        print("ans " + str(ans))
        return ans >= n