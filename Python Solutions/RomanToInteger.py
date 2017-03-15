'''Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.''' class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict={"X":10,"I":1,"V":5,"L":100,"C":100,"D":500,"M":1000,"L":50}
     
        num=0
        i=0
        while i<(len(s)-1):
        
            if dict[s[i]]>=dict[s[i+1]]:
                num=num+dict[s[i]]
                i+=1
            else:
                temp=dict[s[i+1]]-dict[s[i]]
                num+=temp
                i+=2
                
        if len(s)>1:    
            if dict[s[-1]]<=dict[s[-2]]:
                num+=dict[s[-1]]
            
        else:
            num+=dict[s[-1]]

                
                
        return num
       
                
                