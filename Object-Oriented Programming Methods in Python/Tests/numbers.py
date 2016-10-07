'''
* Program #: LabThree_FileInputOutput
* Programmer: Diogo M Delgado
* Due: 7/15/2016
* CS 3A, summer 2016
* Description: Create a program that asks the user for two files to be inputed
    into the other with line markers at the beginning of the sentence.
'''
#open files
infile = open(input(str("Please enter the name of the input file.")), "r")
outfile = open(input(str("Please enter the name of the output file.")), "w")
#initiate the line counter and read the first line
counter = 0
line = infile.readline()
#go through the document and stop once an empty line is found.
while line != "" :
    counter += 1
    precedingLine = "/* " + str(counter) + " */ " + line
    outfile.write(precedingLine)
    line = infile.readline()
#close files
infile.close()
outfile.close()
