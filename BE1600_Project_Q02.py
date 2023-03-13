from os.path import exists

# this function display menu
def printMenu():
    print("Menu")
    print("----------------------------------------")
    print("1. Look up an email address")
    print("2. Add a new name and email address")
    print("3. Change an existing email address")
    print("4. Delete a name and email address")
    print("5. Quit the program")
    # input choice
    choice = input("Enter your choice: ").strip()
    # loop until user not select a valid option
    while choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5":
        # input choice
        choice = input("Enter your choice: ").strip()
    # return the choice
    return choice


# this function search an email from dictionary
def searchEmail(dict):
    # input name
    name = input("Enter a name: ")
    # check that name exist in dictionary
    if name in dict.keys():
        # print name and email
        print("Name: " + name)
        print("Email: " + dict[name])
    else:
        # print message that name not found in dictionary
        print("The specified name was not found")


# this function add a name and email in dictionary
def addNewNameAndEmail(dict):
    # input name
    name = input("Enter name: ")
    # input email
    email = input("Enter email address: ")
    # check that name exist in dictionary
    if name in dict.keys():
        # print message that name already exist in dictionary
        print("That name already exists")
    else:
        # add name and email in dictionary
        dict[name] = email
        print("Name and address have been added")


# this function change email in dictionary
def changeEmail(dict):
    # input name
    name = input("Enter name: ")
    # check that name exist in dictionary
    if name in dict.keys():
        # input email
        email = input("Enter the new address: ")
        # update email in dictionary
        dict[name] = email
        print("Information updated")
    else:
        # print message that name not found in dictionary
        print("The specified name was not found")


# this function delete a name and email from dictionary
def deleteNameAndEmail(dict):
    # input name
    name = input("Enter name: ")
    # check that name exist in dictionary
    if name in dict.keys():
        # delete name and email from dictionary
        dict.pop(name)
        print("Information deleted")
    else:
        # print message that name not found in dictionary
        print("The specified name was not found")


def loadEmailsFromFile(fileName):
    # create a dictionary
    dict = {}
    # check that file exist or not
    if exists(fileName) == False:
        # return the dictionary
        return dict
    # open file for reading
    file = open(fileName, "r")
    # read all lines from file
    lines = file.readlines()
    # loop to process all lines
    for i in range(len(lines)):
        name = lines[i].strip()
        i = i + 1
        if i < len(lines):
            email = lines[i].strip()
            # add name and email in dictionary
            dict[name] = email
    # close the file
    file.close()
    # return the dictionary
    return dict


def saveEmailsInFile(dict, fileName):
    # open the file
    file = open(fileName, "w")
    # loop to process all keys of dictionary
    for name in dict.keys():
		# write name and email in file
        file.write(name + "\n" + dict[name] + "\n")
    # close the file
    file.close()
    print("Information saved")


def run():
    # read data from file and load into dictionary
    dict = loadEmailsFromFile("file.txt")
    exitProgram = False
    # loop until user not select exit
    while exitProgram == False:
        # print menu and input choice
        choice = printMenu()
        # if user select "1"
        if choice == "1":
            # search email in dictionary
            searchEmail(dict)
        # if user select "2"
        elif choice == "2":
            # add new name and email in dictionary
            addNewNameAndEmail(dict)
        # if user select "3"
        elif choice == "3":
            # change email in from dictionary
            changeEmail(dict)
        # if user select "4"
        elif choice == "4":
            # delete name and email from dictionary
            deleteNameAndEmail(dict)
        # if user select "5"
        elif choice == "5":
            # save data in file from dictionary
            saveEmailsInFile(dict, "file.txt")
            exitProgram = True
        if exitProgram == False:
            print()


# run the program
run()


