import sys       # used for argv
import random    # used for autogen passwords
import pyperclip # used for clipboard
import string    # used for strings

def main():
    if (len(sys.argv) != 3):
        print("too few arguments: -option | argument")

    else:
        if (sys.argv[1] == "-s"):
            print(prefixSearch(sys.argv[2]))
            print(autoGenPass())

# Read password file
def readFile(fileName):
    file = open(fileName, "r")
    fileLines = file.readlines() # read file line by line
    return fileLines # returns list

# Search for a service/s name using a prefix
def prefixSearch(search):
    serviceNames = list()
    lines = readFile("passwords.txt")

    for line in lines:
        delimitLine = line.split() # separate line by spaces
        serviceNames.append(delimitLine[0]) # store list of service names

    index = 0
    indexList = list() # keep track of indexes where search is found
    for service in serviceNames:
        if (search == service[:len(search)]): # search for service name
            indexList.append(index) # return index of search result
        index += 1

    return indexList # return list of search indexes

# Autogenerate a random password
def autoGenPass():
    return (''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase
            + string.digits + string.punctuation, k=20)))

if __name__ == "__main__":
    main()
