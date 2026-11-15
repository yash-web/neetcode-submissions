class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        res={}

        for i in s:
            if i in res:
                res[i]+=1
            else:
                res[i]=1
        for i in t:
            if i not in res:
                return False
            else:
                res[i]-=1
            if res[i]==0:
                res.pop(i)
        # print(res)
        if len(res)==0:
            return True
        # return s==t.reverse
        return False        