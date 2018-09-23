from random import uniform

def read(CSVfileR):#taken from Intro II hw!Opens a file and returns the contents of the file in a list of strings
    c = open(CSVfileR,"r")
    CSV =  c.readlines()
    c.close()
    return CSV

#File = read("occupations.csv")
def editData(list):#edits the list containing the contents of the csv file to make it easier to parse; returns totalPercentage as a float
    list.pop(0)#Removes column descriptions
    totalString = list[-1]
    totalString = totalString[0:len(totalString) -1]
    totalList = totalString.split(",")
    totalPercentage = float(totalList[1])
    list.pop()#Removes total occupation and percentage
    return totalPercentage#returns total percentage to be stored globally

#totalPercentage = editData(File)#total percentage is stored globally
#print (File)

def makeDict(list):#returns a dictionary using the occupation as the key and the percentage as the value
    d = {}
    for s in list:
        s = s[0:len(s) -1]
        l = []
        if s[0] == '"':#splits the string by double quotation marks if there are commas in the occupation description
            l = s.split('"')
            l.pop(0)
            l[1] = l[1][1:]
        else:#splits the string by commas if there are no commas in the occupation description
            l = s.split(",")
        #print (l)
        d[l[0]] = float(l[1])#Creates the dictionary using the occupation as the key and the percentage as the value
    return d

#Dict = makeDict(File)
def randOccupation(dict,totalPercentage):#returns a random occupation based on percentages in the data
    percent = uniform(0,totalPercentage)#picks a random float from 0 - 99.8
    for x in dict:
        percent -= dict[x]#subtracts each percentage  from the randomly picked percentage from 0 - 99.
        if percent < 0:
            return x
#print (randOccupation(Dict))
def main():
    File = read("data/occupations.csv")
    head = File[0]
    head = head[0:len(head) - 1]
    listH = head.split(",")
    h1 = listH[0]
    h2 = listH[1]
    Data = File
    Data = Data[1: len(Data)]
    Data = makeDict(Data)
    totalPercentage = editData(File)#total percentage is stored globally
    Dict = makeDict(File)
    return (randOccupation(Dict,totalPercentage), Data, h1, h2)
main()
