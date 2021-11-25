import os
import re #used to split sentences based on multiple punctuation marks (RegEx)
import sys #used for inputting multiple lines as a string
import subprocess #used to open file in text editor on mac
from signal import signal, SIGINT #to test if SIGINT is called (Cmd + C)

class TextManager:
    def __init__(self):
        self.rawText = None
        self.formattedText = None   
    
    def formatUpperCase(self):
        # for mac / linux
        if os.name == 'posix':
            os.system('clear')
        else:
            # for windows platfrom
            os.system('cls')
    
        print("*********     UPPERCASE CONVERTER      ********* \n")

        if self.rawText:
            print("This is your raw text: ", self.rawText)
        else:
            self.rawText = input("Please enter/paste the text you'd like to make uppercase: ")
        
        self.formattedText = self.rawText.upper()
        print("\nThis is your edited text: " + self.formattedText)
        self.exportOrExit()

    def formatLowerCase(self):
        # for mac / linux
        if os.name == 'posix':
            os.system('clear')
        else:
            # for windows platfrom
            os.system('cls')

        print("*********     LOWERCASE CONVERTER      ********* \n")
        
        if self.rawText:
            print("This is your raw text: ", self.rawText)
        else:
            self.rawText = input("Please enter/paste the text you'd like to make lowercase: ")
        
        self.formattedText = self.rawText.lower()
        print("\nThis is your edited text: " + self.formattedText)
        self.exportOrExit()

    def formatSentence(self):
        # for mac / linux
        if os.name == 'posix':
            os.system('clear')
        else:
            # for windows platfrom
            os.system('cls')

        end_punc = [".", "?", "!"] #list of punctuations to check if string ends with them
    
        print("""*********     SENTENCE / PARAGRAPH FORMATTER      *********\n
        \nThis will add capitalize each sentence and add a period if the last sentence doesn't finish with a punctuation.\n""")
        
        if self.rawText:
            print("This is your raw text: ", self.rawText)
        else:
            self.rawText = input("Please enter/paste the text you'd like to format: ")

        str = self.rawText 

        if not str.endswith(tuple(end_punc)) and not str == "":
            str = str + "." #add period to end of sentence / paragraph

        self.formattedText = "".join(i[:1].upper() + i[1:] for i in re.split(r"(\s*[\.\?\!]\s*) *", str)) #correct regex

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

        print("\nThis is your edited text: " + self.formattedText)
        self.exportOrExit()

    def importText(self):
        # for mac / linux
        if os.name == 'posix':
            os.system('clear')
        else:
            # for windows platfrom
            os.system('cls')

        print("""*********     IMPORT TEXT      *********\n
        \nThis allows you to import your unformatted text from a text file for formatting. Place RAW text in sampleInput.txt in the same directory as this program.\n""")
        
        file = open("sampleInput.txt", "r")
        str = file.read()
        
        input("\nThis is your imported text, stored for the running duration of this program: " + str)
        self.rawText = str
        menu(self)

    def exportText(self):
        # for mac / linux
        if os.name == 'posix':
            os.system('clear')
        else:
            # for windows platfrom
            os.system('cls')

        print("""*********     EXPORT TEXT      *********\n
        \nThis allows you to export your formatted text to a text file. \n""")

        if not self.formattedText:
            input("No text was formatted by program. Try doing so before exporting")
            menu()

        file_name = input("Enter file name you'd like to save in the format file_name.txt: ")
        
        if file_name.endswith(".txt"):
            file = open(file_name, "w+")
            file.write(self.formattedText)
            file.close()
            
            #checks OS to open file editor
            if sys.platform == "win32":
                os.startfile(file_name)
            else:
                subprocess.call(["open",file_name])
        
        else:
            input("File name not valid. Press Enter to try again...")
            self.exportText()
        
        input("\nThe file has been written with formatted text. Check directory for txt file.")
        menu()

    #method for checking if user wants to export 
    def exportOrExit(self):
        choice = input("\nWould you like to EXPORT formatted text into a .txt file before returning to main menu(Y/N)?: ").upper()

        if choice == "Y": #gets methodID from being called in method
            self.exportText()
        elif choice == "N": #redirects user to menu if they want to go.
            menu()
        else:
            input("\nChoice was invalid. Press key to make choice again..\n")
            self.exportOrExit() #makes user repeat method if input is invalid

def menu(textManager = None):
    # for mac / linux
    if os.name == 'posix':
        os.system('clear')
    else:
      # for windows platfrom
      os.system('cls')
      
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
            if not textManager:
                textManager = TextManager()
            
            if option == 1:
                textManager.formatUpperCase()

            elif option == 2:
                textManager.formatLowerCase()
    
            elif option == 3:
                textManager.formatSentence()

            elif option == 4:
                textManager.importText()
    
            elif option == 5:
                textManager.exportText()

            elif option == 6:
                exit(0)
    
            else:
                print("Program has crashed unexpectedly. Exiting.. \n")

        else:
            input("Option needs to be within 1 to 6. Press Enter to try again...")
            menu()

def handler(signal_received, frame):
    # Handle any cleanup here
    print('\nSIGINT or CTRL-C detected. Exiting gracefully')
    exit(0)

if __name__ == "__main__":
    signal(SIGINT, handler)
    menu()
