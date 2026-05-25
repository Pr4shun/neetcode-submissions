class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dictionary = {};
        t_dictionary = {};

        if len(s)!= len(t):
            return False;

        for i in range(len(s)):
            s_dictionary[s[i]] = 1+ s_dictionary.get(s[i], 0);
            t_dictionary[t[i]] = 1 + t_dictionary.get(t[i], 0);
        
        for count in s_dictionary:
            if s_dictionary[count] != t_dictionary.get(count,0):
                return False;
        return True;


        