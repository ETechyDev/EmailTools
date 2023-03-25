class Debugger:
    IsDebuggerOn = False
    def Opendebug(str):
        global IsDebuggerOn 
        if(Debugger.IsDebuggerOn):
            print(str)

DBG = Debugger
DBG.IsDebuggerOn = True