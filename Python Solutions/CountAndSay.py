'''The count-and-say sequence is the sequence of integers beginning as follows:

1, 11, 21, 1211, 111221, ...







1 is read off as "one 1" or 11.

11 is read off as "two 1s" or 21.

21 is read off as "one 2, then one 1" or 1211.







Given an integer n, generate the nth sequence.







Note: The sequence of integers will be represented as a string.



'''
class Solution(object):
    def countAndSay(self, n):
        t = '1'
        for i in range(n-1):
            c=0
            i=0
            newS=''
            while (i<len(t)):
                if i!=len(t)-1:
                    if t[i]==t[i+1]:
                        k=i
                        c+=1
                        while(t[k]==t[k+1] and (k<len(t)-1)):
                            c+=1
                            k=k+1
                            if(k==len(t)-1):
                                break
                        newS=newS+str(c)+str(t[i])     
                        i+=c
                        c=0
                    else:
                        newS=newS+str(1)+str(t[i])
                        i+=1
                else:
                    newS=newS+str(1)+str(t[i])
                    break
            t = newS
            newS = ''
        return t