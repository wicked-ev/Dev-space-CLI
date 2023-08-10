import os
import shutil
import math
import magic


Sailpathsfile = open(".\\data\\starting_paths.txt",'r+')
sailpath = []
deafultSailpath = ''
for i in Sailpathsfile:
    if i[0:1] ==  "D_":
        deafultSailpath = i[1:]
    sailpath.append(i)
Sailpathsfile.close()


def readfileData(filepath):
    file = open(filepath,'r')
    linesarray = []
    for i in file:
        linesarray.append(i)
    file.close()
    return linesarray

def addsailpath(path):
    file = open(".\\data\\starting_paths.txt",'r+')
    newpath = fixpath(path) + "\n"
    for i in file:
        if i != newpath:
            continue
        else:
            print("this path already exists")
            return
    file.write(newpath)
    file.close()

def fixpath (path):
    newpath = ''
    for i in path:
        if i == "\\":
            newpath = newpath + "\\"
        newpath = newpath + i 
    return newpath


def sail(command_list):
    if(len(sailpath) == 0 and (not deafultSailpath)):
        print("""no Starting point are available use command Sail add "path" to add one!""")
    elif len(sailpath) == 1 and command_list[0] == "sail":
        pathlists = readfileData('.\\data\\starting_paths.txt')
        for i in range(len(pathlists)):
            print(i,')', pathlists[i])
    elif deafultSailpath:
        sailpath = defaultSailpath
    elif(command_list[1] == "add"):
        if validatepath(command_list[2]):
            addsailpath(command_list[2])


def FilesList(path):
    listoffiles = os.listdir(path)
    return listoffiles


def validatepath(path):
    if os.path.exists(path):
        return True
    else:
        return False

def commandargumentslist(command):
    
    argumentsList = command.split()

    return argumentsList


def filesTypes(list):
    if type(list) == str:
        list = [list]
    listoftypes = []
    for file in list:
        for i in range(len(file)-1,-1,-1):
            if file[i] == "." and not IsItIn(listoftypes, file[i+1:]):
                listoftypes.append(file[i+1:])
                break
    if(len(listoftypes) == 1):
        return listoftypes[0]
    else:
        return listoftypes


def filesContentsTypes(list,path):
    listoftypes = []
    for file in list:
        filetype = magic.from_filename(path+"\\"+file)
        for i in range(0,len(filetype)):
            if filetype[i] == "," and not IsItIn(listoftypes, filetype[:i-1]):
                listoftypes.append(filetype[:i-1])
                break
    return listoftypes


def IsItIn(array, element):
    for i in array:
        if i == element:
            return True
    return False


def CreateDirectory(path, directoryName):
    newDirectory = path+"\\"+directoryName
    i = 1
    while True:
        if(os.path.isdir(newDirectory)):
            newDirectory = newDirectory +" ("+str(i)+")"
            i+=1
        else:
            os.mkdir(newDirectory)
            break
    return newDirectory



def SortFilesAlphabetically(path, fileslist):
    filesAlphbeticlist = []
    for i in fileslist:
        if os.path.isfile(path+"\\"+i):
            if IsItIn(filesAlphbeticlist,i[0].upper()):
                filesAlphbeticlist.append(i[0])
                newDir = CreateDirectory(path,i[0].upper())
                source_file = path +"\\"+i
                shutil.move(source_file,newDir)
            else:
                source_file = path +"\\"+i
                shutil.move(source_file,path+"\\"+i[0].upper())
        print(fileslist)


# def Onload(path,listofdir,):





def SortFilesBasedOntype(path, typeslist, fileslist):
    for i in typeslist:
        CreateDirectory(path, i)
        for j in fileslist:
            if (i == filesTypes(j)):
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


# path = input("Enter path:")

# SortFilesBasedOntype(path, filesTypes(FilesList(path)), FilesList(path))
# CreateDirectory(path,"HelleWorld!")
# SortFilesBasedonsize(path,FilesList(path))
# print(FilesList(path))
# print(FilesList(path))

