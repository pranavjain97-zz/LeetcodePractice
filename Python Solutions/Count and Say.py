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