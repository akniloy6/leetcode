""" 
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 """



from cgi import print_directory
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l1 = len(strs) - 1
        prefix = ""
        
        for i in range(len(strs[0])):
            for str in strs:
                if i == len(str) or str[i] != strs [0][i]:
                    return prefix
            prefix += strs [0][i]
            
        

        return prefix
    
if __name__ == '__main__':
    print (Solution().longestCommonPrefix(["flower","flow","flight"]))
    print (Solution().longestCommonPrefix(["dog","racecar","car"]))
     
        