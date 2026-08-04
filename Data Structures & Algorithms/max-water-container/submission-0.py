class Solution:
    def maxArea(self, nums: List[int]) -> int:
        ans_max=0


        i,j=0,len(nums)-1

        while(i<j):

            diff=min(nums[i],nums[j])

            ans_max=max(ans_max,(j-i)*diff)

            if nums[i]<nums[j]:
                i+=1
            else:
                j-=1

        
        return ans_max






        