###Randomizer für Annika
from random import shuffle, choice, random, randint
import sys

#Read input file
def readfile(infilename):
    inputfile = open(infilename, 'r')
    vidlist = []
    for line in inputfile:
        line = line.replace('\n','')    #Replace newlines from original file by commas
        line = line.split(',')          #Split lines by comma
        vidlist.append(line)            #Create a list with all read items
    return vidlist

#Create output file
def outputfile(outfilename, newlist):
    outfile = open(outfilename, 'w')
    outfile.write("Gloss, corr_resp, other_resp \n")    #Header line: Gloss of the sign, expected response, distractor
    for i in range(len(newlist)):
        outfile.write(newlist[i][0] + "," + newlist[i][1] + ',' + newlist[i][2] +  '\n')    #Write items in output file
    outfile.close()

translation = []    #List of translation options per item, to be stacked within list structure
templist =[]        #Serves for matching FMUs with translation options
experimentlist = [] #List with stacked list per line and within that a stacked list with the translation
outputlist = []     #List with structure for outputfile
vidlist = readfile("NGTsigns.txt")   #Inputfile: GLOSS, FMU, translation1, translation2,..., translationN

#Create list of FMUs with translation options
for i in range(len(vidlist)):
    for j in range(len(vidlist[i])):
        if j < 2:
            translation = []    #Separate GLOSS and FMU from translations
        else:
            translation.append(vidlist[i][j])   #Append all translations in line
    templist.append(vidlist[i][0])  #Append GLOSS to templist
    templist.append(vidlist[i][1])  #Append FMU to templist
    templist.append(translation)    #Append all translation options for FMU in this line
    experimentlist.append(templist)
    templist = []

for i in range(len(experimentlist)):
    Gloss = experimentlist[i][0]
    FMU = experimentlist[i][1]
    
    # Search for correct response -> shares FMU with GLOSS-line
    l = randint(0,len(experimentlist)-1)
    while experimentlist[l][1] != FMU:
        l = randint(0,len(experimentlist)-1)    #Search for a line that has the target FMU
    o = randint(0,len(experimentlist[l][2])-1)  #Within line, pick a random translation
    corr_resp = experimentlist[l][2][o]

    #Search for distractor -> FMU different from GLOSS-line
    p = randint(0,len(experimentlist)-1)
    if FMU == "WID" or FMU == "IND":        
        while experimentlist[p][1] == FMU or experimentlist[p][1] in ("WID","IND"): #IND and WID refer to the same form/unit, therefore distractors for one can't have an FMU from the other 
            p = randint(0,len(experimentlist)-1)    #Search for a line that has an FMU different from that in GLOSS line
        q = randint(0,len(experimentlist[p][2])-1)  #Within line, pick a random translation
        other_resp = experimentlist[p][2][q]
    else:
        while experimentlist[p][1] == FMU:
            p = randint(0,len(experimentlist)-1)    #See line 57
        q = randint(0,len(experimentlist[p][2])-1)  #See line 58
        other_resp = experimentlist[p][2][q]

    #Print everything into output file
    outputlist.append([])
    outputlist[i].append(Gloss)
    outputlist[i].append(corr_resp)
    outputlist[i].append(other_resp)

create_output = outputfile("Output.txt", outputlist)

