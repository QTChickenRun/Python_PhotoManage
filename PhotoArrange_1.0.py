# -*- coding: utf-8 -*-
#conding=gb

import time
import os
import shutil
####################################
#* jinqiting 2015-12-14
#* Variable
####################################
FLAG = {'true':1,'flase':0}

####################################
#* jinqiting 2015-12-14
#* return file time struct
####################################
def RetFileTime(FilePath,FileName):
    fpath = os.path.join(FilePath,FileName)
    FileTime = time.gmtime(os.path.getmtime(fpath))
    return FileTime

####################################
#* jinqiting 2015-12-14
#* Check File Direction
####################################
def CheckDir(FilePath,FileName):
    if os.path.isdir(FilePath + '/' + FileName):
        return FLAG['true']
    else:
        return FLAG['flase']

####################################
#* jinqiting 2015-12-14
#* Check File Folder
####################################
def CheckFolder(FilePath,FileTime):
    YearFolderPath = FilePath + '/' + str(FileTime.tm_year)
    if os.path.exists(YearFolderPath) == 0:
       os.makedirs(YearFolderPath)
    #Check month path
    MonFolderPath = FilePath + '/' +  str(FileTime.tm_year) + '/' + str(FileTime.tm_mon)
    if os.path.exists(MonFolderPath) == 0:
        os.makedirs(MonFolderPath)

    if os.path.exists(MonFolderPath):
        return FLAG['true']
    else:
        return FLAG['flase']
####################################
#* jinqiting 2015-12-14
#* Arrange File
####################################
def ArrangeFile(FilePath,FileName):
    Path = FilePath+'/'+FileName
    #get file time
    FileTime = RetFileTime(FilePath,FileName)
    SavePath = g_SavePath
    #check time file folder
    if CheckFolder(SavePath,FileTime) == 1:
        SavePath = SavePath + '/' + str(FileTime.tm_year) + '/' + '/' + str(FileTime.tm_mon)
        if os.path.isfile(SavePath + '/' + FileName) == 0:
            shutil.move(Path,SavePath)
        return FLAG['true']
    else:
        return FLAG['flase']

####################################
#* jinqiting 2015-12-14
#* Arrange Folder
####################################
def ArrangeFolder(FilePath,FileName):
    NewPath = FilePath + '/' + FileName
    NewFileList = os.listdir(NewPath)

    for NewFile in NewFileList:
        if CheckDir(NewPath,NewFile) == 0:
            if ArrangeFile(NewPath,NewFile) == 1:
                continue
            else:
                break
        else:
            ArrangeFolder(NewPath,NewFile)

####################################
#* jinqiting 2015-12-14
#* Program Entry
####################################
#Step1:获取路径
g_SavePath = input("Please save direction:");
RootPath = input("Please input direction:")
#g_SavePath = r'I:/photo'
#RootPath = r'I:/test'
print (RootPath)
print (g_SavePath)
print ("Start Arrange")
FileList = os.listdir(RootPath)
print (time.ctime())
for FileName in FileList:
    #判断为文件
    if CheckDir(RootPath,FileName) == 0:
        if ArrangeFile(RootPath,FileName) == 1:
            continue
        else:
            break
    else:
        ArrangeFolder(RootPath,FileName)

print (time.ctime())
print ('End Arrange')
