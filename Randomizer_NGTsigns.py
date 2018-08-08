###randomizer für annika
from random import shuffle, choice, random, randint
import sys

#read input file
def readfile(infilename):
    inputfile = open(infilename, 'r')
    vidlist = []
    for line in inputfile:
        line = line.replace('\n','')    #replace newlines from original file by commas
        line = line.split(',')          #split lines by comma
        vidlist.append(line)            #create a list with all read items
    return vidlist

#create output file
def outputfile(outfilename, newlist, header):
    outfile = open(outfilename, 'w')
    outfile.write(header)
    for z in range(len(newlist)):
        outfile.write(newlist[z][0] + "," + newlist[z][1] + ',' + newlist[z][2] + ',' + newlist[z][3] + ',' + newlist[z][4] + ',' + newlist[z][5] + '\n')    #write items in output file
    outfile.close()


inputlist = readfile("ngtsigns.txt")   #inputfile: gloss, fmu, translation1, translation2,..., translationn

def randomiser(number, vidlist):
    for r in range(number):
        #create list of fmus with translation options
        translation = []  # list of translation options per item, to be stacked within list structure
        templist = []  # serves for matching fmus with translation options
        temptrans = []  # serves for temporarily storing the current translation list
        experimentlist = []  # list with stacked list per line and within that a stacked list with the translation
        outputlist = []  # list with structure for outputfile
        for i in range(len(vidlist)):
            for j in range(len(vidlist[i])):
                if j < 2:
                    translation = []    #separate gloss and fmu from translations
                else:
                    translation.append(vidlist[i][j])   #append all translations in line
            templist.append(vidlist[i][0])  #append gloss to templist
            templist.append(vidlist[i][1])  #append fmu to templist
            templist.append(translation)    #append all translation options for fmu in this line
            experimentlist.append(templist)
            templist = []

        for i in range(len(experimentlist)):
            gloss = experimentlist[i][0]
            fmu = experimentlist[i][1]
            temptrans = experimentlist[i][2]
            #print(temptrans)

            # search for correct response -> shares fmu with gloss-line
            l = randint(0,len(experimentlist)-1)
            while experimentlist[l][1] != fmu or l == i:
                l = randint(0,len(experimentlist)-1)    #search for a line that has the target fmu and is different from line i
            o = randint(0,len(experimentlist[l][2])-1)  #within line, pick a random translation
            while experimentlist[l][2][o] in temptrans:
                print('i found my own translation')
                o = randint(0,len(experimentlist[l][2])-1)
            corr_resp = experimentlist[l][2][o]

            #search for distractor -> fmu different from gloss-line
            p = randint(0,len(experimentlist)-1)
            if fmu == "wid" or fmu == "ind":
                while experimentlist[p][1] == fmu or experimentlist[p][1] in ("wid","ind"): #ind and wid refer to the same form/unit, therefore distractors for one can't have an fmu from the other
                    p = randint(0,len(experimentlist)-1)    #search for a line that has an fmu different from that in gloss line
                q = randint(0,len(experimentlist[p][2])-1)  #within line, pick a random translation
                while experimentlist[p][2][q] in temptrans:
                    print('i found my own translation')
                    q = randint(0, len(experimentlist[p][2]) - 1)
                other_resp = experimentlist[p][2][q]
            else:
                while experimentlist[p][1] == fmu:
                    p = randint(0,len(experimentlist)-1)    #see line 57
                q = randint(0,len(experimentlist[p][2])-1)  #see line 58
                while experimentlist[p][2][q] in temptrans:
                    q = randint(0, len(experimentlist[l][2]) - 1)
                other_resp = experimentlist[p][2][q]

            #print everything into output file
            outputlist.append([])
            outputlist[i].append(gloss)
            outputlist[i].append(corr_resp)
            outputlist[i].append(other_resp)
            outputlist[i].append(fmu)
            outputlist[i].append('')
            outputlist[i].append('')

        output_header = "gloss,corr_resp,other_resp,fmu\n"   #header line: gloss of the sign, expected response, distractor
        create_output = outputfile("pp" + str(r) + "_ngtrandom.txt", outputlist, output_header)
        print("i'm done with pp " + str(r))


def listmaker(number):
    for i in range(number):
        vidlist = readfile("pp"+str(i)+"_ngtrandom.txt")
        outputlist = []
        output_header = "gloss,left_resp,right_resp,correct_response,fmu,phase\n"

        for j in range(len(vidlist)-1):
            gloss = vidlist[j+1][0]
            fmu = vidlist[j+1][3]
            if j%2 == 0:
                print('j+1 is '+str(j+1))
                print('even row')
                resp_right = vidlist[j+1][1]  #correct response
                resp_left = vidlist[j+1][2]   #distractor
                correct_response = "r"
            else:
                print('j+1 is '+str(j+1))
                print('uneven row')
                resp_right = vidlist[j+1][2]  #distractor
                resp_left = vidlist[j+1][1]   #correct response
                correct_response = "l"

            outputlist.append([])
            outputlist.append([])
            outputlist[j].append(gloss)
            outputlist[j].append(resp_left)
            outputlist[j].append(resp_right)
            outputlist[j].append(correct_response)
            outputlist[j].append(fmu)
            outputlist[j].append("ngt")

        print(outputlist)

        cleanoutputlist = [x for x in outputlist if x != []]

        print(cleanoutputlist)
        create_output = outputfile("pp" + str(i) + "_ngtsigns.csv", cleanoutputlist, output_header)
        print("i'm done with ordered list for pp " + str(i))

randomiser(21, inputlist)
listmaker(21)