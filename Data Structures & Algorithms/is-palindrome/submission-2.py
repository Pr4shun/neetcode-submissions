class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        p1 = 0;
        p2 = len(s)-1;

        while(p1 < p2):
            while(p1 < p2 and s[p1].isalnum() == False):
                p1 = p1+1;

            while(p1 < p2 and s[p2].isalnum() == False):
                p2 = p2-1;
            
            if(s[p1] == s[p2]):
                p1 = p1+1;
                p2 = p2-1;
            
            elif(s[p1]!= s[p2]):
                return False
            
        return True

            
        






        