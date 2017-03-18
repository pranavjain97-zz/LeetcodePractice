
from bs4 import BeautifulSoup
import urllib2

input="Best Time To Buy And Sell Stock II"
ext=".java"


def filenameConverter(string):
    string=string.lower()
    temp=string.split(' ')
    newFile=''
    noOfSpaces=len(temp)
    for i in range(0,noOfSpaces):
        newFile+=temp[i].capitalize()
    return newFile


filename=filenameConverter(input)+ext

if ext==".py":
    commentStart = "'''"
    commentEnd = "''' "
    folder = "Python Solutions"
elif ext == ".java":
    commentStart = "/*"
    commentEnd = "*/ "
    folder="Java Solutions"
else:
    print "File formal does not exist"


questionName=input.lower().replace(" ", "-")
print questionName

leet="https://leetcode.com/problems/"+questionName+"/#/description"
page3 = urllib2.urlopen(leet).read()
soup3 = BeautifulSoup(page3)

desc = soup3.findAll(attrs={"name":"description"})
finalDesc = commentStart + (desc[0]['content'].encode('utf-8'))+commentEnd


with open("./{0}/{1}".format(folder, filename), "r+") as f: s = f.read(); f.seek(0); f.write(finalDesc + s)



