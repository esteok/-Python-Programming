# this function display the menu
def printMenu():
    print("Hello, this program allows you to translate text to morse code or translate morse code to text.\n")
    print("Please, select one of the below option:\n")
    print("*** Enter 't' for encoding text")
    print("*** Enter 'm' for decoding morse code")
    print("*** Enter 'e' to exit the program.")
    # input an option
    option = input("\nMy input is: ")
    # loop until user not select a valid option
    while option != "t" and option != "m" and option != "e":
        print("***invalid option***")
        option = input("Please enter a valid option: ")
    # return the option
    return option


# this function load morse code from file and load into dictionary
def loadMorseCodeToDictionary(fileName):
    # open file
    file = open(fileName, "r")
    # create a dictionary
    dict = {}
    # process all line of file
    for line in file.readlines():
        # split the data and add into dictionary
        data = line.strip().split(" ")
        dict[data[0]] = data[1]
    # close the file
    file.close()
    # return the dictionary
    return dict

# this function convert a text to morse code
def convertTextToMorseCode(text, dict):
    # convert the text to upper case
    text = text.upper()
    morseCode = ""
    # process all letters in text
    for ch in text:
        # if letter is space
        if ch == ' ':
            morseCode += "   "
        else:
            # add value of letter from dictionary
            morseCode += dict[ch] + " "
    # return morse code
    return morseCode.strip()

# this function convert the morse code to text
def convertMorseCodeToText(morseCode, dict):
    text = ""
    # create another dictionary to store morse code as key and letter as value
    dict2 = {}
    # process all keys of first dictionary
    for key in dict.keys():
        # add current key in 2nd dictionary
        dict2[dict[key]] = key
    # split morse code for words
    for word in morseCode.split("   "):
        # split the morse code for letter
        for letter in word.strip().split(" "):
            text += dict2[letter] # add letter of morse code in text
        # add space in text
        text += " "
    # return the text
    return text.strip()


def run():
# read data from file and load into dictionary
    dict = loadMorseCodeToDictionary("morse.txt")
    exitProgram = False
    while exitProgram == False:
        # display menu and select an option
        option = printMenu()
        # if user select "t"
        if option == "t":
            text = input("\nPlease enter text to translate:\n") # input text
            print(convertTextToMorseCode(text, dict) + "\n\n")  # convert text to morse code and display
        elif option == "m":
            morseCode = input("\nPlease enter morse to translate:\n")
            # convert morse code to text and display
            print(convertMorseCodeToText(morseCode, dict) + "\n\n")
        # if user select "e"
        elif option == "e":
            print("\nThanks for using this program!")
            exitProgram = True


# run the program
run()
