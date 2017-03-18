from bs4 import BeautifulSoup
import urllib2

class descriptionAppender:

    commentStart=''
    commentEnd=''

    def __init__(self,problem,ext):
        self.problemName=problem
        self.ext=ext


    def CamelFilenameConverter(self):
        string=self.problemName.lower()
        temp=string.split(' ')
        newFile=''
        noOfSpaces=len(temp)
        for i in range(0,noOfSpaces):
            newFile+=temp[i].capitalize()
        return newFile


    def folderFinder(self):
        if self.ext==".py":
            self.commentStart = "'''"
            self.commentEnd = "''' "
            return "Python Solutions"
        elif self.ext == ".java":
            self.commentStart = "/*"
            self.commentEnd = "*/ "
            return "Java Solutions"
        else:
            return "File formal does not exist"

    def getDiscriptionFromLeet(self):
        questionName = self.problemName.lower().replace(" ", "-")
        leet = "https://leetcode.com/problems/" + questionName + "/#/description"
        page3 = urllib2.urlopen(leet).read()
        soup3 = BeautifulSoup(page3)
        desc = soup3.findAll(attrs={"name": "description"})
        finalDesc = self.commentStart + (desc[0]['content'].encode('utf-8')) + self.commentEnd
        return finalDesc


    def writeIntoFile(self,folder,filename,finalDesc):
        with open("./{0}/{1}".format(folder, filename), "r+") as f: s = f.read(); f.seek(0); f.write(finalDesc + s)
        

if __name__ == "__main__":
	    problem = input("Enter the problem name (eg: Fizz Buzz): ")
	    extension = input("Please give the extension of the fileName (eg: .py): ")
	    o1 = descriptionAppender(problem, extension)
	    filename=o1.CamelFilenameConverter()+extension
            folder=o1.folderFinder()
            description=o1.getDiscriptionFromLeet()
	    o1.writeIntoFile(folder,filename,description)

