import os
import shutil
import sqlite3
import database_utils
def loadExtentions(path):
    extentions=database_utils.fetchExtentions(path)
    return extentions
def saveExtentions(extentions,path):
    database_utils.create_tables(path)
    database_utils.saveExtentions(extentions,path)
delimit=str('\\')
path=input('Enter the path to scan for Files: ')
#Check if sqlite file is present?
exists=os.path.isfile(path+'\\'+'extentions.db')
if(exists):
    extentions=loadExtentions(path)
else:
    extentions=[]
for (dirpath,dirnames,files) in os.walk(path):
    for filename in files:
        extpos=filename.find('.')
        extention=filename[extpos+1:]
        print(dirpath)
        # print(dirnames)
        print(filename)
        print(extention)
        if(extention in extentions):
            #No need to make a new folder
            sourcePath=dirpath+delimit+filename
            destinationPath=dirpath+delimit+extention+delimit+filename
            print('Source Path ',sourcePath)
            print('Destination Path',destinationPath)
            shutil.move(sourcePath,destinationPath)
        else:
            sourcePath=dirpath+delimit+filename
            destinationPath=dirpath+delimit+extention+delimit+filename
            print('Source Path ',sourcePath)
            print('Destination Path',destinationPath)
            extentions.append(extention)
            shutil.move(sourcePath,destinationPath)
print(extentions)
saveExtentions(extentions,path)