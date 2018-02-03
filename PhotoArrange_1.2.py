# -*- coding: utf-8 -*-
#conding=gb
#! /usr/bin/env python
import time
import os
import shutil
import string
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
def ArrangeFile(SaveRootPath,FilePath,FileName,FileSaveYear,FileSaveMonth,CheckFlag):
    Path = FilePath+'/'+FileName
    #get file time
    FileTime = RetFileTime(FilePath,FileName)
    FileYear = FileTime.tm_year
    FileMonth = FileTime.tm_mon

    #判断文件时间是否符合要求
    if(FileYear > string.atoi(FileSaveYear)):
        return FLAG['true']
    elif (FileYear == string.atoi(FileSaveYear)):
        if (FileMonth > string.atoi(FileSaveMonth)):
            return FLAG['true']
    
    #check time file folder
    if CheckFolder(SaveRootPath,FileTime) == 1:
        SavePath = SaveRootPath + '/' + str(FileYear) + '/' + str(FileMonth)
        if ("Y " == CheckFlag):
            print ("SavePath %s" , (SavePath + '/' + FileName))
            if os.path.isfile(SavePath + '/' + FileName) == 0:
                print ("cp Path %s to %s", (Path,SavePath))
                shutil.move(Path,SavePath)
        else:
            if os.path.isfile(SavePath + '/' + FileName) == 1:
                os.remove(SavePath + '/' + FileName)
            print ("move Path %s to %s",(Path,SavePath))
            shutil.move(Path,SavePath)
        return FLAG['true']
    else:
        return FLAG['flase']

####################################
#* jinqiting 2015-12-14
#* Arrange Folder
####################################
def ArrangeFolder(SavePath,FilePath,FileName,FileYear,FileMonth,CheckFlag):
    NewPath = FilePath + '/' + FileName
    NewFileList = os.listdir(NewPath)

    for NewFile in NewFileList:
        if CheckDir(NewPath,NewFile) == 0:
            if ArrangeFile(SavePath,NewPath,NewFile,FileYear,FileMonth,CheckFlag) == 1:
                continue
            else:
                break
        else:
            ArrangeFolder(SavePath,NewPath,NewFile,FileYear,FileMonth,CheckFlag)


####################################
#* jinqiting 2016-05-29
#* main()
####################################
def mainInput():
    SavePath = input("Please save direction(\"D:/Photo\"):")
    RootPath = input("Please input src direction(\"C:/Users/Kting/Desktop/DCIM\"):")
    LastSaveDate=input("Please input arrange date(\"201605\"):")
    CheckFileFlag = input("Please input whether check dest file(\"Y\"/\"N\"):")
    SaveYear= LastSaveDate[0:4]
    SaveMonth = LastSaveDate[4:6]
    print ("照 片 源 路 径:" ,(RootPath))
    print ("照 片 目 标 路 径: ",  (SavePath))
    print ("整 理 照 片 年 份 : ", (SaveYear))# -*- coding: utf-8 -*-
#conding=gb
#! /usr/bin/env python
import time
import os
import shutil
import string
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
def ArrangeFile(SaveRootPath,FilePath,FileName,FileSaveYear,FileSaveMonth,CheckFlag):
    Path = FilePath+'/'+FileName
    #get file time
    FileTime = RetFileTime(FilePath,FileName)
    FileYear = FileTime.tm_year
    FileMonth = FileTime.tm_mon

    #判断文件时间是否符合要求
    if(FileYear > string.atoi(FileSaveYear)):
        return FLAG['true']
    elif (FileYear == string.atoi(FileSaveYear)):
        if (FileMonth > string.atoi(FileSaveMonth)):
            return FLAG['true']
    
    #check time file folder
    if CheckFolder(SaveRootPath,FileTime) == 1:
        SavePath = SaveRootPath + '/' + str(FileYear) + '/' + str(FileMonth)
        if ("Y " == CheckFlag):
            print ("SavePath %s" , (SavePath + '/' + FileName))
            if os.path.isfile(SavePath + '/' + FileName) == 0:
                print ("cp Path %s to %s", (Path,SavePath))
                shutil.move(Path,SavePath)
        else:
            if os.path.isfile(SavePath + '/' + FileName) == 1:
                os.remove(SavePath + '/' + FileName)
            print ("move Path %s to %s",(Path,SavePath))
            shutil.move(Path,SavePath)
        return FLAG['true']
    else:
        return FLAG['flase']

####################################
#* jinqiting 2015-12-14
#* Arrange Folder
####################################
def ArrangeFolder(SavePath,FilePath,FileName,FileYear,FileMonth,CheckFlag):
    NewPath = FilePath + '/' + FileName
    NewFileList = os.listdir(NewPath)

    for NewFile in NewFileList:
        if CheckDir(NewPath,NewFile) == 0:
            if ArrangeFile(SavePath,NewPath,NewFile,FileYear,FileMonth,CheckFlag) == 1:
                continue
            else:
                break
        else:
            ArrangeFolder(SavePath,NewPath,NewFile,FileYear,FileMonth,CheckFlag)


####################################
#* jinqiting 2016-05-29
#* main()
####################################
def mainInput():
    SavePath = input("Please save direction(\"D:/Photo\"):")
    RootPath = input("Please input src direction(\"C:/Users/Kting/Desktop/DCIM\"):")
    LastSaveDate=input("Please input arrange date(\"201605\"):")
    CheckFileFlag = input("Please input whether check dest file(\"Y\"/\"N\"):")
    SaveYear= LastSaveDate[0:4]
    SaveMonth = LastSaveDate[4:6]
    print ("照 片 源 路 径:" ,(RootPath))
    print ("照 片 目 标 路 径: ",  (SavePath))
    print ("整 理 照 片 年 份 : ", (SaveYear))
    print ("整 理 照 片 月 份 :"  ,(SaveMonth))
    print ("是否检查目标文件存在 " ,(CheckFileFlag))
    
    StartFlag = input("Start Arrange(\"Y\"/\"N\"):");
    print ("StartFlag "  ,(StartFlag))
    if ((StartFlag != "Y" ) and (StartFlag != "y")):
        print("Stop Arrange Photo!!") 
        return

    #开始计时
    print ("Start Time" ,(time.ctime()))

    #获取文件列表
    FileList = os.listdir(RootPath)

    for FileName in FileList:
        #是否为文件夹
        if CheckDir(RootPath,FileName) == 0:
            if ArrangeFile(SavePath,RootPath,FileName,SaveYear,SaveMonth,CheckFileFlag) == 1:
                continue
            else:
                break;
        else:
            ArrangeFolder(SavePath,RootPath,FileName,SaveYear,SaveMonth,CheckFileFlag)
    
    
            
if  __name__ == '__main__':
    mainInput()
    print (time.ctime())
    print ('End Arrange!please enter ctrl+c!\n')
    while(1):
        continue
    
   
	    
    
        



    print ("整 理 照 片 月 份 :"  ,(SaveMonth))
    print ("是否检查目标文件存在 " ,(CheckFileFlag))
    
    StartFlag = input("Start Arrange(\"Y\"/\"N\"):");
    print ("StartFlag "  ,(StartFlag))
    if ((StartFlag != "Y" ) and (StartFlag != "y")):
        print("Stop Arrange Photo!!") 
        return

    #开始计时
    print ("Start Time" (time.ctime()))

    #获取文件列表
    FileList = os.listdir(RootPath)

    for FileName in FileList:
        #是否为文件夹
        if CheckDir(RootPath,FileName) == 0:
            if ArrangeFile(SavePath,RootPath,FileName,SaveYear,SaveMonth,CheckFileFlag) == 1:
                continue
            else:
                break;
        else:
            ArrangeFolder(SavePath,RootPath,FileName,SaveYear,SaveMonth,CheckFileFlag)
    
    
            
if  __name__ == '__main__':
    mainInput()
    print (time.ctime())
    print ('End Arrange!please enter ctrl+c!\n')
    while(1):
        continue
    
   
	    
    
        


