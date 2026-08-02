class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:


        helper_dict={}

        for i,k in enumerate(numbers):
            # print(tagr)
            if target-k  in helper_dict:
                print(helper_dict)
                return [helper_dict[target-k]+1,i+1]
            else:
                helper_dict[k]=i

        
        



        return [-1,-1]



        