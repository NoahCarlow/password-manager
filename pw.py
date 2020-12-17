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
            print("CHANGE(-c) : -c service password")
            print("\t options: entering 'random' as password generates random password")
            print("DELETE(-c) : -d service")
            print("INSERT(-i) : -i service password")
            print("\t options: entering 'random' as password generates random password")

        # Search
        if (sys.argv[1] == "-s"):
            results = prefixSearch(sys.argv[2]) # stores index list of results
            passwords = readFile("passwords.txt")

            if not results:
                print("No Results")

            elif (len(results) == 1):
                print("Password Copied")
                passResult = passwords[results[0]]
                passDelimited = passResult.split()
                pyperclip.copy(passDelimited[1]) # copy password

            elif (len(results) > 1):
                print("Did you mean:") 
                for i in range (0, len(results)):
                    passResult = passwords[results[i]]
                    passDelimited = passResult.split()
                    print(passDelimited[0])

        # Change
        if (sys.argv[1] == "-c"):
            results = prefixSearch(sys.argv[2]) # stores index list of results
            passwords = readFile("passwords.txt")

            if not results:
                print("No Results")

            elif (len(results) == 1):
                print("Updated")
                passResult = passwords[results[0]]
                passDelimited = passResult.split()

                deleteLine(passDelimited[0], passDelimited[1]) # delete existing line
                insertAccount(passDelimited[0], sys.argv[3]) # write new line

            elif (len(results) > 1):
                print("Did you mean:") 
                for i in range (0, len(results)):
                    passResult = passwords[results[i]]
                    passDelimited = passResult.split()
                    print(passDelimited[0])

        # Delete
        if (sys.argv[1] == "-d"):
            results = prefixSearch(sys.argv[2]) # stores index list of results
            passwords = readFile("passwords.txt")

            if not results:
                print("No Results")

            elif (len(results) == 1):
                print("Deleted")
                passResult = passwords[results[0]]
                passDelimited = passResult.split()

                deleteLine(passDelimited[0], passDelimited[1]) # delete existing line

            elif (len(results) > 1):
                print("Did you mean:") 
                for i in range (0, len(results)):
                    passResult = passwords[results[i]]
                    passDelimited = passResult.split()
                    print(passDelimited[0])
        
        # Insert
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
        serviceString =  service[:len(search)] # store service name for some len of chars
        if (search.lower() == serviceString.lower()): # search for service name
            indexList.append(index) # return index of search result
        index += 1

    return indexList # return list of search indexes

# Delete a service and password in the file
def deleteLine(service, password):
    with open("passwords.txt", "r") as f:
        lines = f.readlines()
    with open("passwords.txt", "w") as f:
        for line in lines: # rewrite file skipping line of existing service
            if line.strip("\n") != "{} {}".format(service, password):
                f.write(line)

# Autogenerate a random password
def autoGenPass():
    return (''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase
            + string.digits + string.punctuation, k = 20)))

# Insert service and password
def insertAccount(service, password):
    if (password == "random"):
        password = autoGenPass()

    file = open("passwords.txt", "a")
    file.write("{} {}\n".format(service, password)) # append service and pw to file
    file.close()


if __name__ == "__main__":
    main()
