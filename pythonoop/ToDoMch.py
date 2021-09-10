import ToDoMaterial
import ToDoSettings
from abc import ABC, abstractmethod
from typing import List

import TodoMec


class toDoMech(ABC):
    commandList = list()
    ToDoMaterials = list()
    commandList.append("list all to-dos")
    commandList.append("create new todo")
    commandList.append("update a todo")
    commandList.append("delete a todo")
    commandList.append("Comandslist")
    commandList.append("complete todo")
    commandList.append("show not complete")
    commandList.append("settings")
    commandList.append("quit")
    commandList.append("info")

    def MethodList(self):
        for x in self.commandList:
            print(x)
    pass

    def LevelStyle(level):
        if str(level).__eq__("high"):
            return ToDoSettings.TodoSettings.Color_Red + "high"


    @abstractmethod
    def ListAllItem(self):
        pass

    @abstractmethod
    def AddItem(self, index):
        pass

    @abstractmethod
    def DeleteItem(self):
        pass

    @abstractmethod
    def UpdateItem(self):
        pass

    @abstractmethod
    def CompleteItem(self):
        pass

    @abstractmethod
    def DeleteItem(self):
        pass

    @abstractmethod
    def PrintAllCommands(self):
        pass

    def ShowNotCompletedItem(self):
        pass