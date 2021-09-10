from builtins import type

import Priority
import ToDoSettings


class toDoMaterial:
    __title = str()
    __description = str()
    __remainDate = str()
    __Level = str()
    __IsCompleted = False

    def __init__(self, __title, __description, __remainDate, __Level, __IsCompleted):
        self.__title = __title
        self.__description = __description
        self.__Level = __Level
        self.__remainDate = __remainDate
        self.__IsCompleted = False

    def GetTitle(self):
        return self.__title

    def SetTitle(self, __title):
        self.__title = __title

    def getDescription(self):
        return self.__description

    def setDescription(self, __description):
        self.__description = __description

    def getLevel(self):
        return self.__Level

    def setLevel(self, __Level):
        self.__Level = __Level

    def GetIsCompleted(self):
        if self.__IsCompleted:
            return ToDoSettings.TodoSettings.Color_Blue + " Is Completed " + ToDoSettings.TodoSettings.Reset_Color
        else:
            return ToDoSettings.TodoSettings.Color_Red + " Not Completed " + ToDoSettings.TodoSettings.Reset_Color

    def SetIsCompleted(self, __IsCompleted):
        self.__IsCompleted = __IsCompleted

    def getDateTime(self):
        return self.__remainDate

    def setDateTime(self, __remainDate):
        self.__remainDate = __remainDate
