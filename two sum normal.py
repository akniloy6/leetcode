from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        l = len(nums) - 1
        
        print(l)
        
        for i in range(l):
            #print(f"i = {i}")
            
            for j in reversed(range(l+1)):
                
                sum = nums[i] + nums[j]
                
                #print(f"j = {j}")
                
                if(j==i):
                    continue
                
                if (sum==target):
                    
                    return [i,j]
        return []
                   
#test cases

if __name__ == '__main__':
    print (Solution().twoSum([2,4,8],6))
    
    
     