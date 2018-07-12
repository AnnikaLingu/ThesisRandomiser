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
resplist = readfile("NGTsignsForPseudo.txt")
vidlist = readfile("Pseudosigns.txt")

# Create list of FMUs with translation options
for i in range(len(resplist)):
    for j in range(len(resplist[i])):
        if j < 2:
            translation = []
        else:
            translation.append(resplist[i][j])
    templist.append(resplist[i][1])
    templist.append(translation)
    experimentlist.append(templist)
    templist = []

print(experimentlist)

for i in range(len(experimentlist)):
    Gloss = vidlist[i][0]
    FMU = vidlist[i][1]
    
    # Search for correct response -> shares FMU with GLOSS-line
    l = randint(0,len(experimentlist)-1)
    while experimentlist[l][0] != FMU:
        l = randint(0,len(experimentlist)-1)
    o = randint(0,len(experimentlist[l][1])-1)
    corr_resp = experimentlist[l][1][o]

    #Search for distractor -> FMU different from GLOSS-line
    p = randint(0,len(experimentlist)-1)
    while experimentlist[p][0] == FMU:
        p = randint(0,len(experimentlist)-1)
    q = randint(0,len(experimentlist[p][1])-1)
    other_resp = experimentlist[p][1][q]

    #Print everything into output file
    outputlist.append([])
    outputlist[i].append(Gloss)
    outputlist[i].append(corr_resp)
    outputlist[i].append(other_resp)

create_output = outputfile("Output.txt", outputlist)

