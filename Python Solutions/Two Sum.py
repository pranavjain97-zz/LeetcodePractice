class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d=[]
        list=[]
        
        for i in range(0,len(nums)):
            complement=target-nums[i]; 
            if complement in d:
                list.extend((d.index(complement),i))
                return list 
                
            d.append(nums[i])
            
            
                
            
        