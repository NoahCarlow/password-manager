#! /usr/bin/python3

import sys       # used for argv
import random    # used for autogen passwords
import pyperclip # used for clipboard
import string    # used for strings

def main():
    if (len(sys.argv) < 1):
        print("too few arguments: -option | argument")

    else:
        if (sys.argv[1] == "-help"):
            print("SEARCH(-s) : -s service")
            print("INSERT(-i) : -i service password")
            print("\t options: entering 'random' as password generates random password")

        if (sys.argv[1] == "-s"):
            results = prefixSearch(sys.argv[2]) # stores index list of results
            passwords = readFile("passwords.txt")

            if not results:
                print("no results")

            elif (len(results) == 1):
                print("copied!")
                passResult = passwords[results[0]]
                passDelimited = passResult.split()
                pyperclip.copy(passDelimited[1])

            elif (len(results) > 1):
                print("select service: ") 
        
        if (sys.argv[1] == "-i"):
            insertAccount(sys.argv[2], sys.argv[3])

# Read password file
def readFile(fileName):
    file = open(fileName, "r")
    fileLines = file.readlines() # read file line by line
    file.close()
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

# Insert service and password
def insertAccount(service, password):
    if (password == "random"):
        password = autoGenPass()

    file = open("passwords.txt", "a")
    file.write("{} {}\n".format(service, password)) # append service and pw to file
    file.close()


if __name__ == "__main__":
    main()
