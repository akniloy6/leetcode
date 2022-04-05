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
        list = str(x)
        div = len(list) - 1
        div = 10 ** div
        
        while x:
            r = x % 10
            l = x // div
            if ( l != r):
                return False
            x = (x % div) // 10
            div = div / 100
            
        
        
        return True
        
        
        
       

if __name__=='__main__':
    print(Solution().isPalindrome(1221))
    print(Solution().isPalindrome(12231))