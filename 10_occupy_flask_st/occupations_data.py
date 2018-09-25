from random import uniform #allows us to read CSV files

def read(CSVfileR):#taken from Intro II hw!Opens a file and returns the contents of the file in a list of strings
    data = open(CSVfileR,"r")
    CSV =  data.readlines()
    data.close()
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
    dict = {}
    for string in list:
        string = string[0:len(string) -1]
        val = []
        if string[0] == '"':#splits the string by double quotation marks if there are commas in the occupation description
            val = string.split('"')
            val.pop(0)
            val[1] = val[1][1:]
        else:#splits the string by commas if there are no commas in the occupation description
            val = string.split(",")
        #print (l)
        dict[val[0]] = float(val[1])#Creates the dictionary using the occupation as the key and the percentage as the value
    return dict

#Dict = makeDict(File)
def randOccupation(dict,totalPercentage):#returns a random occupation based on percentages in the data
    percent = uniform(0,totalPercentage)#picks a random float from 0 - 99.8
    for pval in dict:
        percent -= dict[pval]#subtracts each percentage  from the randomly picked percentage from 0 - 99.
        if percent < 0:
            return pval
#print (randOccupation(Dict))
        
def table():
    File = read("data/occupations.csv")
    head = File[0]
    head = head[0:len(head) - 1] 
    listH = head.split(",")      #Splits up occ names for table
    h1 = listH[0]  #Makes First header
    h2 = listH[1]  #Makes Second header
    Data = File
    Data = Data[1: len(Data)]
    Data = makeDict(Data)
    totalPercentage = editData(File)#total percentage is stored globally
    Dict = makeDict(File)  #Makes File into Dict again for randOccupation fnx
    return (randOccupation(Dict,totalPercentage), Data, h1, h2)  #returns both rand occ, data for table, and headers
table()
