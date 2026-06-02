class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myDict = defaultdict(list)

        for word in strs:
            char = [0]*26

            for letter in word:
                char[ord(letter) - ord("a")] +=1

            myDict[tuple(char)].append(word)

        return list(myDict.values())
            
        