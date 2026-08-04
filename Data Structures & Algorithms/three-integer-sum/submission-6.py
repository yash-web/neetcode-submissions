class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        pp=set()
        nums.sort()
        # i,j=0,len(nums)-1
        # p=0

        for i in range(0,len(nums)-2):
            p=i+1
            j=len(nums)-1
            while(p<j):
                # p=i+1

                if nums[i]+nums[j]+nums[p]==0:
                    kl=[nums[i],nums[p],nums[j]]
                    if tuple(kl) in pp:
                        p+=1
                        j-=1
                    else:    
                        ans.append(kl)
                        p+=1
                        j-=1
                    pp.add(tuple(kl))
                elif nums[i]+nums[j]+nums[p]<0:
                    # ans.append([i,p,j])
                    p+=1
                    # j-=1
                else:
                    # ans.append([i,p,j])
                    # i+=1
                    j-=1
                # p+=1
            
        return ans
            
