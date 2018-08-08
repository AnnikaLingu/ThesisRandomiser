###randomizer für annika
from random import shuffle, choice, random, randint
import sys

#read input file
def readfile(infilename):
    inputfile = open(infilename, 'r')
    vidlist = []
    for line in inputfile:
        line = line.replace('\n','')    #replace newlines in original file by commas
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


def randomiser(number, inputfile, respfile):
    for y in range(number):
        translation = []    #list of possible translations per item, to be stacked within list structure
        templist =[]        #serves for matching fmus with translation options
        experimentlist = [] #list with stacked list per line and within that a stacked list with the translations
        outputlist = []     #list with structure for outputfile
        resplist = readfile(respfile)    #inputfile for list of response options: gloss, fmu, translation1, translation2,...,translationn
        vidlist = readfile(inputfile)           #list of videos: video, fmu


        # create list of fmus with translation options
        for i in range(len(resplist)):
            for j in range(len(resplist[i])):
                if j < 2:
                    translation = []    #separate gloss and fmu from translations
                else:
                    translation.append(resplist[i][j])  #append all translations in line
            templist.append(resplist[i][1]) #append fmu to templist
            templist.append(translation)    #append all translation options for fmu in this line
            experimentlist.append(templist)
            templist = []
            print('Experimentlist is ' + str(len(experimentlist)) + ' long')

        for i in range(len(vidlist)):
            gloss = vidlist[i][0]
            print(gloss)
            fmu_real = vidlist[i][1]
            if fmu_real == 'SPR':
                random = randint(0,1)
                if random == 0:
                    fmu = 'IND'
                else:
                    fmu = 'WID'
            else:
                fmu = fmu_real
            print(fmu)
            # search for correct response -> shares fmu with gloss-line
            l = randint(0,len(resplist)-1)
            while experimentlist[l][0] != fmu:          #search for a line that has the target fmu
                l = randint(0,len(experimentlist)-1)
            o = randint(0,len(experimentlist[l][1])-1)  #within line, pick a random translation
            corr_resp = experimentlist[l][1][o]

            #search for distractor -> fmu different from gloss-line
            p = randint(0,len(experimentlist)-1)
            while experimentlist[p][0] == fmu:          #search for line that has an fmu different from that in gloss line
                p = randint(0,len(experimentlist)-1)
            q = randint(0,len(experimentlist[p][1])-1)  #within line, pick a random translation
            other_resp = experimentlist[p][1][q]

            #print everything into output file
            outputlist.append([])
            outputlist[i].append(gloss)
            outputlist[i].append(corr_resp)
            outputlist[i].append(other_resp)
            if fmu == 'IND' or fmu == 'WID':
                fmu = 'SPR'
            outputlist[i].append(fmu)
            outputlist[i].append('')
            outputlist[i].append('')

        output_header = "gloss,correct response,other response,fmu"
        create_output = outputfile("pp" + str(y) +"_randompseudosigns.txt", outputlist, output_header)

def listmaker(number):
    for i in range(number):
        vidlist = readfile("pp"+str(i)+"_randompseudosigns.txt")
        outputlist = []
        output_header = "gloss,left_resp,right_resp,correct_response,fmu,phase\n"

        for j in range(len(vidlist)-1):
            gloss = vidlist[j+1][0]
            fmu = vidlist[j+1][3]
            if fmu in 'IND,WID':
                fmu = 'SPR'
            if j%2 == 0:
                #print('j+1 is '+str(j+1))
                #print('even row')
                resp_right = vidlist[j+1][1]  #correct response
                resp_left = vidlist[j+1][2]   #distractor
                correct_response = "r"
            else:
                #print('j+1 is '+str(j+1))
                #print('uneven row')
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
            outputlist[j].append("pseudo")

        #print(outputlist)

        cleanoutputlist = [x for x in outputlist if x != []]

        #print(cleanoutputlist)
        create_output = outputfile("pp" + str(i) + "_pseudosigns.csv", cleanoutputlist, output_header)
        print("i'm done with ordered list for pp " + str(i))


randomiser(21, "pseudosigns.txt", "ngtsigns.txt")
listmaker(21)