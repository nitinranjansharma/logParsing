import re
import json

def parseWholeText(fileContent):
    try:
        resultDict = dict()
        tempList = list()
        
        
        for line in fileContent.decode("utf-8").split('\r'): #convert bytes to str
            ops,file,line_number,name = parseLogLine(line)
            tempDict = dict()
            if ops != "":
                tempDict['operation'] = ops
                tempDict['filename'] = file
                tempDict['line_number'] = int(line_number)
                tempDict['name'] = name
                tempList.append(tempDict)
            #print(ops,file,line_number,name)
        if len(tempList)>0:
            resultDict['result'] = tempList
            #resultDict = json.dumps(resultDict)
            print(resultDict)
            resultDict = (resultDict)
        
            return(resultDict)
        else:
            return("The file couldn't be parsed properly, please enter proper log file")
    except():
        return("Exception while reading file")
    





def parseLogLine(line):
    #initializing values
    ops = ""
    filename = ""
    file = ""
    line_number = 0
    name = "anonymous"
    filenameRegex = re.compile(r'(?:ENTER:|EXIT:|ENTRY:)\s*(/\S*)')
    entry = re.compile(r'(ENT.+)')
    nonentry = re.compile(r'(EX.+)')
    entry.findall("EXIT: test")  
    
    try:
        filename = (filenameRegex.findall(line))
        if len(filename) >0:
            if entry.findall(line):
                ops = "ENTRY"
            elif nonentry.findall(line):
                ops = "EXIT"
            else:
                ops = "Invalid"
            file = filename[0].split(':')[0]
            line_number = filename[0].split(':')[1]
            name = line.split(" ")[-1]
            if len(name) != 0:
                gr = re.search(r'^(.*? [-\s+] )?(.*)', name, re.UNICODE)
                if gr.group(0) is not None:
                        
                    if gr.group(0) != "0" and gr.group(0) != 0:
                        name = gr.group(0)
                    else:
                        name = "anonymous"               
            
    except():
        pass
    return(ops,file,line_number,name)