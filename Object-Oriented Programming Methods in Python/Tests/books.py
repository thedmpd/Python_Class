#open data lists
inputFile = open("books.txt", "r")
dataLine = inputFile.read().strip()

#helper functions
def merge_dicts(*dicts):
    d = {}
    for dict in dicts:
        for key in dict:
            try:
                d[key].append(dict[key])
            except KeyError:
                d[key] = [dict[key]]
    return d

def findInformation(dataLine):
    nameNumbers = dataLine.splitlines()
    dictionary = dict()
    i = 0
    j = 0
    while i < len(nameNumbers):
        holder = nameNumbers[i]
        holder = holder.split(',')
        holder[j + 1] = holder[j + 1].strip()
        dictionary[holder[1]] = holder[0]
        i += 1
    dictionary = merge_dicts(dictionary)
    return dictionary

#main program
dictionary = findInformation(dataLine)
print(dictionary)
inputFile.close()
