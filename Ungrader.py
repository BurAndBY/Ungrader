import os
import glob

# Sets the main directory
main_path = input("Enter your scripts path. \n Example: D:/Unity Projects/MyGreatProject/Assets/Scripts/ \n ")

# Gets a list of everything in the main directory including folders
main_directory = os.listdir(main_path)

# This list will hold all of the folders to search through, including the main folder
sub_directories = []

# Adds the main folder to to the list of folders
sub_directories.append(main_path)

# Loops through everthing in the main folder, searching for sub folders
for item in main_directory:
    # Creates the full path to each item)
    item_path = os.path.join(main_path, item)

    # Checks each item to see if it is a directory
    if os.path.isdir(item_path) == True:
        # If it is a folder it is added to the list
        sub_directories.append(item_path)

for directory in sub_directories:
    for files in glob.glob(os.path.join(directory,"*.cs")): #Only C# files will work
        f = open( files, 'r' ) #Open files in read-only mode
        file_contents = f.read() #Read file
        
        if "ref " in file_contents: #Contains ref
            print("Files with ref:", f.name + "; \n") #Type file name
            print("Replace 'ref ' with '' ")
         
        if "out var " in file_contents: #Contains out var
            print(" Files with out var ", f.name + "; \n") #Type file name
            print("Replace 'out var ' with '' ")
        if "=>" in file_contents: #Contains out var
            print(" Files with out var ", f.name + "; \n") #Type file name
            print("Replace '=>' with '=' ")
answer = input("Close app? yes or no") #Ask should we close the app
if answer in ('yes', 'no'): #Yes is an only option. Accept your faith.
    exit() #Closing...
