import os #used for clearing cmd screen
import re #used to split sentences based on multiple punctuation marks (RegEx)
import sys #used for inputting multiple lines as a string
import subprocess #used to open file in text editor on mac

#global variables
str = ""
edit_text = ""

#method for checking if user wants to repeat process
def repeat_method(methodID):
    choice = input("Enter Y to repeat Method, or N to return to Main Menu: ")

    if choice == "Y": #gets methodID from being called in method

        if methodID == 1:
            uppercase()

        elif methodID == 2:
            lowercase()
        
        elif methodID == 3:
            sentence()
        
        elif methodID == 4:
            import_text()

        elif methodID == 5:
            export_text()
        
        else:
            print("Something went wrong...Exiting\n")
            exit()
                
    elif choice == "N": #redirects user to menu if they want to go.
        menu()
    
    else:
        input("Choice was invalid. Please try again..")
        repeat_method(methodID) #makes user repeat method if input is invalid

#function checks if string is imported and if it isn't, it reads user input
def isImported():
    global str

    if not str == "":
        print("Text has been imported. Raw Text: \n")
        print(str)
    else:
        print("Press control + D twice when you have finished entering your text.\n \nRaw Text: \n")
        str = sys.stdin.read()

def uppercase():
    os.system('cls')  # For Windows
    os.system('clear')  # For Linux/OS X
    methodID = 1 #method IDs passed for repeat method to identify method that needs to be repeated
    global str
    global edit_text
    
    print("*********     UPPERCASE CONVERTER      ********* \n")
    
    isImported()
    
    edit_text = str.upper()
    
    print("\n \nThis is your edited text: \n \n" + edit_text)

    repeat_method(methodID)

def lowercase():
    os.system('cls')  # For Windows
    os.system('clear')  # For Linux/OS X
    methodID = 2
    global str
    global edit_text

    print("*********     LOWERCASE CONVERTER      ********* \n")

    isImported()

    edit_text = str.lower()
    
    print("\n \nThis is your edited text: \n \n" + edit_text)

    repeat_method(methodID)

def sentence():
    os.system('cls')  # For Windows
    os.system('clear')  # For Linux/OS X
    methodID = 3
    global str
    global edit_text
    
    end_punc = [".", "?", "!"] #list of punctuations to check if string ends with them
    
    print("*********     SENTENCE FORMATTER      ********* \n")
    print("This does not automatically include punctuation marks except the period. \n \n"\
          "If there are multiple sentences, please separate them by punctuation marks. \n")

    isImported()

    if not str.endswith(tuple(end_punc)) and not str == "":
        str = str + "." #converts list to tuple for endswith() method to function

    edit_text = "".join(i[:1].upper() + i[1:] for i in re.split(r"(\s*[\.\?!]\s*) *", str)) #correct regex

    '''
    FOR THIS REGEX:
        r - interprets the special characters as they are and not literal
        () - to check regex in order exact
        \s* - 0 or more whitespace to consider if spacing is there
        [] - to check if ANY of the characters inside are match
        \. - escape character for dot
        \? - escape character for question mark
        * - checks if any of the punctuation marks were entered after each other eg. ?! or ..
        
    FOR .join():
        capitalizes first letter in first word +  rest of sentence that is split
    '''

    print("\n \nThis is your edited text: \n \n" + edit_text)

    repeat_method(methodID)

def import_text():
    os.system('cls')  # For Windows
    os.system('clear')  # For Linux/OS X
    methodID = 4
    global str

    print("*********     IMPORT TEXT      ********* \n")
    print("This allows you to import your unformatted text from a text file for formatting. \n")
    print("Store this file in the same directory as this program. \n")

    file_name = input("Enter file name in the format file_name.txt: ")
    
    #checks if file is formatted correctly with .txt
    if file_name.endswith(".txt"):
        file = open(file_name, "r")
        str = file.read()
    else:
        input("File name not valid. Press Enter to try again...")
        import_text()
    
    print("\nThis is your imported unformatted text: \n")
    print(str)

    repeat_method(methodID)



def export_text():
    os.system('cls')  # For Windows
    os.system('clear')  # For Linux/OS X
    methodID = 5
    global edit_text
    
    print("*********     EXPORT TEXT      ********* \n")
    print("This allows you to export your formatted text to a text file. \n")

    file_name = input("Enter file name you'd like to save in the format file_name.txt: ")
    
    if file_name.endswith(".txt"):
        file = open(file_name, "w+")
        file.write(edit_text)
        file.close()
        
        #checks OS to open file editor
        if sys.platform == "win32":
            os.startfile(file_name)
    
        else:
            subprocess.call(["open",file_name])
    
    else:
        input("File name not valid. Press Enter to try again...")
        export_text()
    
    print("\nThe file has been written with formatted text. Check directory for txt file.")

    repeat_method(methodID)

def menu():
    os.system('cls')  # For Windows
    os.system('clear')  # For Linux/OS X
    
    print("*********     WELCOME TO THE TEXT FORMATTER      ********* \n")
    print("This program was created by JesseETI :) \n \n")
    
    option = input("ENTER AN OPTION: \n" \
                           "1. UPPERCASE \n" \
                           "2. lowercase \n" \
                           "3. Sentence Format. \n" \
                           "4. Import text \n" \
                           "5. Export text \n" \
                           "6. Exit \n \n")
    
    #repeats until menu option is an int and is between 1 to 6
    try:
        int(option)
    except ValueError:
        input("Option not valid. Press Enter to try again...")
        menu()
    else:
        option = int(option)
        if option >= 1 and option <= 6:
            if option == 1:
                uppercase()

            elif option == 2:
                lowercase()
    
            elif option == 3:
                sentence()

            elif option == 4:
                import_text()
    
            elif option == 5:
                export_text()

            elif option == 6:
                exit()
    
            else:
                print("Program has crashed unexpectedly. Exiting.. \n")

        else:
            input("Option needs to be within 1 to 6. Press Enter to try again...")
            menu()

#from menu choice, function is called. Therefore, only menu is called in program code. Rest is user input.
menu()
