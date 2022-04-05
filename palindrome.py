""" Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.
 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome. """


import string
from typing import List

class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if(x<0):
            return False
        string = str(x)
        list = [int(x) for x in string]
        reversed_list = []
        length = len(list)
        for i in reversed(range(length)):
            reversed_list.append(list[i])
        print(f"List= {list}")
        print(f"reversed_list= {reversed_list}")
        
        for i in range(length):
            if(reversed_list[i] != list[i]):
                return False
            
        
        
        return True
        
        
        
       

if __name__=='__main__':
    print(Solution().isPalindrome(1221))
    print(Solution().isPalindrome(12231))