import function
import subprocess
commandslist = ['sail','h','list','li','copy','copypaste','search','sch','kickout','project','sort',"ex"]
Progstatus = "running"
CommandGuid = [['sail','->','<-','copy','add','setdef'],
               ['h'],
               ['list','copyname',],
               ['li'],
               ['copy'],
               ['copypast','cp'],
               ['search'],['sch'],
               ['kickout','c','x'],
               ['project','jhc'],
               ['sort','type','name','size'],
               ['ex'],]
while True and Progstatus == "running":
    command = str(input())
    arrayCommand = function.commandargumentslist(command)
    match arrayCommand[0]:
        case 'sail':
            function.sail(arrayCommand)
        case 'ex':
            Progstatus = "exiting"
        case other:
            print ("Shell command")
            resault = subprocess.run(command,shell = True,capture_output=True, text = True)
            print(resault.stdout)

