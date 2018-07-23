###Randomizer für Annika
from random import shuffle, choice, random, randint
import sys

#Read input file
def readfile(infilename):
    inputfile = open(infilename, 'r')
    vidlist = []
    for line in inputfile:
        line = line.replace('\n','')    #Replace newlines in original file by commas
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

translation = []    #List of possible translations per item, to be stacked within list structure
templist =[]        #Serves for matching FMUs with translation options
experimentlist = [] #List with stacked list per line and within that a stacked list with the translations
outputlist = []     #List with structure for outputfile
resplist = readfile("NGTsignsForPseudo.txt")    #Inputfile for list of response options: GLOSS, FMU, translation1, translation2,...,translationN
vidlist = readfile("Pseudosigns.txt")           #List of videos: VIDEO, FMU

# Create list of FMUs with translation options
for i in range(len(resplist)):
    for j in range(len(resplist[i])):
        if j < 2:
            translation = []    #Exclude GLOSS and FMU from translations
        else:
            translation.append(resplist[i][j])  #Append all translations in line
    templist.append(resplist[i][1]) #Append FMU to templist
    templist.append(translation)    #Append all translation options for FMU in this line
    experimentlist.append(templist)
    templist = []

print(experimentlist)

for i in range(len(experimentlist)):
    Gloss = vidlist[i][0]
    FMU = vidlist[i][1]
    
    # Search for correct response -> shares FMU with GLOSS-line
    l = randint(0,len(experimentlist)-1)
    while experimentlist[l][0] != FMU:          #Search for a line that has the target FMU
        l = randint(0,len(experimentlist)-1)
    o = randint(0,len(experimentlist[l][1])-1)  #Within line, pick a random translation
    corr_resp = experimentlist[l][1][o]

    #Search for distractor -> FMU different from GLOSS-line
    p = randint(0,len(experimentlist)-1)
    while experimentlist[p][0] == FMU:          #Search for line that has an FMU different from that in GLOSS line
        p = randint(0,len(experimentlist)-1)
    q = randint(0,len(experimentlist[p][1])-1)  #Within line, pick a random translation
    other_resp = experimentlist[p][1][q]

    #Print everything into output file
    outputlist.append([])
    outputlist[i].append(Gloss)
    outputlist[i].append(corr_resp)
    outputlist[i].append(other_resp)

create_output = outputfile("Output.txt", outputlist)

