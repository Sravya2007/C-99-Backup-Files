import os
import shutil
#Write the name of directory here that needs to be sorted
path = input("Enter the name of directory to be sorted: ")
#This will create a properly organised list with all the files that are there in the directory
list_of_files = os.listdir(path)
#This will go through each and every file
for file in list_of_files:
    name, ext = os.path.splitext(file)
    #This is going to store extension type
    ext = ext[1:]
    #This forces the next iteration , if it is a directory
    if ext == ' ':
        continue
    #This will move the file to the directory where the name 'ext' already exists
    if os.path.exists(path + '/' + ext):
        shutil.move(path + '/' + file, path + '/' + ext + '/' + file)
    else:
        os.makedirs(path + '/' + ext)
        shutil.move(path + '/' + file, path + '/' + ext + '/' + file)