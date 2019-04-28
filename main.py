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
ignoreList=(input('Enter the extentions to ignore in a space seperated format: ').strip().split())
if(exists):
    extentions=loadExtentions(path)
else:
    extentions=[]
for (dirpath,dirnames,files) in os.walk(path):
    for filename in files:
        if(filename=='extentions.db'):
            continue
        extpos=filename.find('.')
        extention=filename[extpos+1:]
        if(extention in ignoreList):
            continue
        print(dirpath)
        # print(dirnames)
        print(filename)
        print(extention)
        if(extention in extentions):
            if(extention =='py'):
                #Do not move Python Files
                continue
            #No need to make a new folder
            sourcePath=dirpath+delimit+filename
            destinationPath=dirpath+delimit+extention+delimit+filename
            # print('Source Path ',sourcePath)
            # print('Destination Path',destinationPath)
            shutil.move(sourcePath,destinationPath)
        else:
            sourcePath=dirpath+delimit+filename
            destinationPath=dirpath+delimit+extention+delimit+filename
            # print('Source Path ',sourcePath)
            # print('Destination Path',destinationPath)
            extentions.append(extention)
            os.mkdir(dirpath+delimit+extention)
            shutil.move(sourcePath,destinationPath)
    #Break the loop for 1 Iteration only and organize only level 1
    break
print(extentions)
saveExtentions(extentions,path)