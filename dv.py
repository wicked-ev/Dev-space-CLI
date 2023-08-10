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
    for i in commandslist:
        if i == arrayCommand[0]:
            match arrayCommand[0]:
                case 'sail':
                    function.sail()
                case 'ex':
                    Progstatus = "exiting"
                case _:
                    resault = subprocess.run(command,shell = True,capture_output=True, text = True)


