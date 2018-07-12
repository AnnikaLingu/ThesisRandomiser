###Randomizer für Annika
from random import shuffle, choice, random, randint
import sys

def readfile(infilename):
    inputfile = open(infilename, 'r')
    vidlist = []
    for line in inputfile:
        line = line.replace('\n','')
        line = line.split(',')
        vidlist.append(line)
    return vidlist

def outputfile(outfilename, newlist):
    outfile = open(outfilename, 'w')
    outfile.write("Gloss, corr_resp, other_resp \n")
    for i in range(len(newlist)):
        outfile.write(newlist[i][0] + "," + newlist[i][1] + ',' + newlist[i][2] +  '\n')
    outfile.close()

translation = []
templist =[]
experimentlist = []
outputlist = []
vidlist = readfile("Fillers.txt")

for i in range(len(vidlist)):
    for j in range(len(vidlist[i])):
        if j < 2:
            translation = []
        else:
            translation.append(vidlist[i][j])
    templist.append(vidlist[i][0])
    templist.append(vidlist[i][1])
    templist.append(translation)
    experimentlist.append(templist)
    templist = []

for i in range(len(experimentlist)):
    Gloss = experimentlist[i][0]
    FMU = experimentlist[i][1]
    
    # Search for correct response -> shares FMU with GLOSS-line
    l = randint(0,len(experimentlist)-1)
    while experimentlist[l][1] != FMU:
        l = randint(0,len(experimentlist)-1)
    o = randint(0,len(experimentlist[l][2])-1)
    corr_resp = experimentlist[l][2][o]

    #Search for distractor -> FMU different from GLOSS-line
    p = randint(0,len(experimentlist)-1)
    if FMU == "WID" or FMU == "IND":        
        while experimentlist[p][1] == FMU or experimentlist[p][1] in ("WID","IND"):
            p = randint(0,len(experimentlist)-1)
        q = randint(0,len(experimentlist[p][2])-1)
        other_resp = experimentlist[p][2][q]
    else:
        while experimentlist[p][1] == FMU:
            p = randint(0,len(experimentlist)-1)
        q = randint(0,len(experimentlist[p][2])-1)
        other_resp = experimentlist[p][2][q]

    #Print everything into output file
    outputlist.append([])
    outputlist[i].append(Gloss)
    outputlist[i].append(corr_resp)
    outputlist[i].append(other_resp)

create_output = outputfile("Output.txt", outputlist)

