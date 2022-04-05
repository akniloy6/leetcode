""" 

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: [] 
"""


from typing import List


class Solution:
    def threeSum(self, nums : List[int]):
        
        nums.sort()
        
        length = len(nums) - 1
        
        triplet_list = []
    
        
        
        #print(nums)
        
        for i,value in enumerate(nums):
        #while (i<length):   
            #for k in reversed(range(length+1)):
            # print(nums[i])
            # print(nums[i-1])
            if(i>0 and nums[i] == nums[i-1]):
                #i +=1
                # print("dhukse")
                continue
            j = i+1
            k= length
            # print(f"i={i}")
            
            while(j<k):
                
                    
                sum = nums[i] + nums[j] + nums[k]
                # print(f"for i={i}, j= {j}, k={k}, sum={sum}")
                
                if(sum>0):
                    k -= 1
                elif(sum<0):
                    j += 1
                elif(sum==0):
                    triplet_list.append([nums[i] , nums[j] , nums[k]])
                    # print(triplet_list)
                    j += 1
                    while (nums[j]==nums[j-1] and j<k):
                        j += 1        
    
        return triplet_list
    

if __name__=='__main__':
    print (Solution().threeSum([-1,0,1,4,6])) 
    print (Solution().threeSum([-1,0,1,2,-1,-4]))
    print (Solution().threeSum([0]))
    print (Solution().threeSum([]))
    print (Solution().threeSum([-1,0,1,4,6]))   

