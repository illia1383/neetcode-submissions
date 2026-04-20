class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        ma = 0
        
        h = 0
        leng = 0

        l,r = 0,len(heights) -1
        



        while l<r:
            h = min(heights[l],heights[r])
            leng = r-l 
            tempMa = h * leng
            if(heights[l] < heights[r]):
                l += 1
            elif(heights[l]> heights[r]):
                r-=1
            else:
                l+=1
            ma= max(ma,tempMa)
            print(h,leng,ma)
        return ma 
            
            


