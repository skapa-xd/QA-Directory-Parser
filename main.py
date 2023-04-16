import os
import pandas as pd

# Check if path exists or not
def checkIfExist(path):
    if os.path.exists(path) and os.path.isdir(path):
        print("Valid folder path.")
    else:
        print("Invalid folder path.")

# Check if path is Folder
def checkIfFolder(path):
    isFolder = os.path.isfile(path)
    if(isFolder == False):
        print("The given path is of a Folder")
    else:
        print("The given path is not for a Folder")

# Returns a list of all files in the path
def printAllFileNames(path):
    files = os.listdir(path)
    print("The folder contains", len(files), "files.\nThe files are ", files)
    return files

# Returns a list of all files with path
def concatenatePathAndFile(files, path):
    concatenatedPaths = []
    
    for filename in files:
        concatenatedPath = path + '\\' + filename
        concatenatedPaths.append(concatenatedPath)
    return concatenatedPaths

# Returns count of each file type          
def countOfFiles(files):
    countOfFile = {}
    # updating dict with key and value
    for file in files:
        fileType = file.split(".")[-1]
        
        countOfFile[fileType] = countOfFile.get(fileType, 0) +1
    # printing the file types
    for file_type, occurrence in countOfFile.items():
        print(f"File type: {file_type}, Occurrence: {occurrence}")
    return countOfFile

# Counts the records     
def countRecords(file_path):
    totalLines = 0
    
    for path in file_path:
        if path.endswith('.xlsx'):
            try:
                df = pd.read_excel(path)
                numRecords = df.shape[0]
                print(f"File: {path}, Number of Records: {numRecords+1}")
                totalLines += numRecords
            except Exception as e:
                print(f"Error reading Excel file: {path} - {e}")
        else :
            try:
                with open(path, 'r', encoding="utf8", errors="ignore") as file:
                    lines = file.readlines()
                    numRecords = sum(1 for line in lines if line.strip())
                    print(f"File: {path}, Number of Records: {numRecords}")
                    totalLines += numRecords
            except Exception as e:
                print(f"Error reading file: {path} - {e}")

    print(f"Total number of records in all files: {totalLines+1}")
        


def main():
    
    path = input("Enter the Path ")
    checkIfExist(path)
    #checkIfFolder(path)
    files =  printAllFileNames(path)
    countOfFile = countOfFiles(files)
    originalFiles = concatenatePathAndFile(files, path)
    #print(originalFiles)
    countRecords(originalFiles)
    
if __name__ == "__main__":
    main()
    
    