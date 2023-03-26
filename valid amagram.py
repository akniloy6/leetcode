#hasmap solution, O(s+t) memory complexity and time complexity
class Solution:
    def isAnagram(self, s:str, t:str) -> bool:

        #first check if the length of both string is equal, if not, we return false immediately 
        if len(s) != len(t):
            return False
        
        #create two hashmaps for two strings

        countS, countT = {}, {}

        # let us iterate through the length of the string to store 
        # the count of each character in the hashmap. this is how we build the hashmap
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i],0) # s[i] represents the key of the hashmap. Each time we find a key, that is a character, we increment the value of that key by +1.
            countT[t[i]] = 1 + countT.get(t[i],0) # .get method is used to handle for when we dont find a key. it will retunr 0 then.

        #iterate through the hashmap to check the counts of each character in both hashmap are the same

        for c in countS:
            if countS[c] != countT.get(c,0):
                return False #return false if count are not the same

        return True
