import os
import shutil
import math

def FilesList(path):
    listoffiles = os.listdir(path)
    return listoffiles


def filesTypes(list):
    listoftypes = []
    for file in list:
        for i in range(0, len(file)):
            if file[i] == "." and IsItIn(listoftypes, file[i+1:]):
                listoftypes.append(file[i+1:])
    return listoftypes


def IsItIn(array, element):
    for i in array:
        if i == element:
            return False
    return True


def CreateDirectory(path, directoryName):
    newDirectory = path+"\\"+directoryName
    i = 1
    while True:
        if(os.path.isdir(newDirectory)):
            newDirectory = newDirectory +" ("+str(i)+")"
            i+=1
        else:
            os.mkdir(newDirectory)
    return newDirectory


def Thetypefile(filesname):
    for i in range(0, len(filesname)):
        if filesname[i] == ".":
            return filesname[i+1:]


def SortFilesAlphabetically(path, fileslist):
    filesAlphbeticlist = []
    for i in fileslist:
        if os.path.isfile(path+"\\"+i):
            if not IsItIn(filesAlphbeticlist,i[0]):
                filesAlphbeticlist.append(i[0])
                newDir = CreateDirectory(path,i)
                fileslist.remove(i)
                source_file = path +"\\"+i
                shutil.move(source_file,newDir)
            elif IsItIn(filesAlphbeticlist,i[0]):
                fileslist.remove(i)
                source_file = path +"\\"+i
                shutil.move(source_file,path+"\\"+i)


def SortFilesBasedOntype(path, typeslist, fileslist):
    for i in typeslist:
        CreateDirectory(path, i)
        for j in fileslist:
            if (i == Thetypefile(j)):
                source_file = path+"\\"+j
                destination_file = path+"\\"+i+"\\"+j
                shutil.move(source_file, destination_file)


def SortFilesBasedonsize(path, fileslist, Unit="MB"):
    SortUnit = sizeofDirectory(path, fileslist, Unit) / len(fileslist)
    SortUnit = round(SortUnit)
    sizeofTheSmallestFile = fileSizeconverter(os.path.getsize(path+"\\"+ smallestSizefile(path, fileslist)), Unit)
    smallestDirValue = sizeofTheSmallestFile 
    sizeofThelargestFile = fileSizeconverter(os.path.getsize(path+"\\"+ largestSizefile(path, fileslist)), Unit)
    sizeofTheSmallestFile = math.floor(sizeofTheSmallestFile)
    sizeofThelargestFile = math.ceil(sizeofThelargestFile)
    for i in range(sizeofTheSmallestFile, sizeofThelargestFile + SortUnit, SortUnit):
        files_list_for_new_Sort_Dir = []
        for j in fileslist:
            if fileSizeconverter(os.path.getsize(path+"\\"+j), Unit) <= i and os.path.isfile(path+"\\"+j):
                files_list_for_new_Sort_Dir.append(j)
        if (len(files_list_for_new_Sort_Dir) != 0):
            namevalue = ""
            if i == sizeofTheSmallestFile :
                namevalue = smallestDirValue
            else:
                namevalue = i
            newDirName = "less or equal to " + str(namevalue)+Unit
            newDir = path+"\\"+"less or equal to " + str(namevalue)+Unit
            CreateDirectory(path,newDirName)
            for g in files_list_for_new_Sort_Dir:
                source_file = path+"\\"+g
                destnation_file = newDir+"\\"+g
                fileslist.remove(g)
                shutil.move(source_file, destnation_file)


def largestSizefile(path, fileslist):
    largest = fileslist[0]
    for i in fileslist:
        if os.path.getsize(path+"\\"+i) > os.path.getsize(path+"\\"+largest):
            largest = i
    return largest


def smallestSizefile(path, fileslist):
    smallest = fileslist[0]
    for i in fileslist:
        if os.path.getsize(path+"\\"+i) < os.path.getsize(path+"\\"+smallest):
            smallest = i
    return smallest


def fileSizeconverter(argument, unit):
    match unit:
        case 'B':
            return argument
        case 'KB':
            return round(argument / pow(10, 3), 2)
        case 'MB':
            return round(argument / pow(10, 6), 2)
        case 'GB':
            return round(argument / pow(10, 9), 2)
        case 'TB':
            return round(argument / pow(10, 12), 2)
        case 'PB':
            return round(argument / pow(10, 15), 2)


def sizeofDirectory(path, fileslist, Unit="MB"):
    size = 0
    for i in fileslist:
        size += os.path.getsize(path+"\\"+i)
    return fileSizeconverter(size, Unit)


path = input("Enter path:")

# SortFilesBasedOntype(path, filesTypes(FilesList(path)), FilesList(path))
# CreateDirectory(path,"HelleWorld!")
# SortFilesBasedonsize(path,FilesList(path))
SortFilesAlphabetically(path, FilesList(path))

