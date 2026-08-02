class Solution:
    def isPalindrome(self, s: str) -> bool:


        if len(s)==1:
            return True
        s=s.lower().strip().replace(" ","")
        i,j=0,len(s)-1

        print(i)
        print(j)


        while(i<=j):
            print(i,j)
        

            if not s[i].isalnum():
                i+=1
            if not s[j].isalnum():
                j-=1
                
            if s[i]!=s[j] and s[i].isalnum() and s[i].isalnum():
                print(s[i])
                print(s[j])
                return False
            i+=1
            j-=1


        return True
        