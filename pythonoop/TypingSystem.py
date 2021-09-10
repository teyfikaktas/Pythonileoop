import datetime
from builtins import Exception
from lib2to3.fixes.fix_methodattrs import MAP

import OpeningScene
import ToDoMaterial
import ToDoMch
import ToDoSettings
import TodoMec


def StartingWhile():
    while True:
        t = Typing()
        print()
        selected_command = input("")
        Exist = ToDoMch.toDoMech.commandList.index(selected_command)
        if Exist == 0:
            print(
                ToDoSettings.TodoSettings.Color_Blue + "Title " + "         " + ToDoSettings.TodoSettings.Color_White + "Description " + "         " + ToDoSettings.TodoSettings.Color_Cyan + "Creation date " + "         " + ToDoSettings.TodoSettings.Color_Yellow + "Level " + "         " + ToDoSettings.TodoSettings.Color_Cyan + "Completion status " + "         " + ToDoSettings.TodoSettings.Reset_Color)
            t.LıstAllTodos()
        if Exist == 1:
            t.AddItem()
        if Exist == 2:
            t.UpdateItem()
        if Exist == 3:
            t.DeleteItem()
        if Exist == 4:
            t.ShowList()
        if Exist == 5:
            t.ComplatedItem()
        if Exist == 6:
            t.NotComplete()
        if Exist == 8:
            print("Thanks " + t.getUserName() + " Hope to see you again ^^");
            break


class Typing:
    PreferName = "type"
    QuitName = "quit"
    WelcomeText = "Welcome again. Can I know your name?"
    __UserName = "default"
    Numeritor = 0
    FirstText = "I see that you haven't prepared a to-do list for today. What can I do for you?"
    print(OpeningScene.OpeningScene.WelcomeText)

    def getUserName(self):
        return self.__UserName

    def SetUserName(self, __UserName):
        self.__UserName = __UserName

    def Starting(self):
        if self.Numeritor == 0:
            print(self.WelcomeText)
            NewUserName = input()
            self.SetUserName(self, NewUserName)
            print(self.getUserName(self))
        if len(ToDoMch.toDoMech.ToDoMaterials) <= 0:
            print("Welcome " + self.getUserName(self) + " today time " + datetime.datetime.now().strftime(
                "%c") + " I see that you haven't prepared a to-do list for today. What can I do for you?")
        else:
            print("Welcome " + self.getUserName(self) + " today time " + datetime.datetime.now().strftime(
                "%c") + "What can I do for you?")
        StartingWhile()

    def AddItem(self):
        title = input("Please write the title of the to-do list item you want to add.")
        desc = input("Please desc the title of the to-do list item you want to add.")
        DateTime = datetime.datetime.now().strftime("%c")
        Level = input('Please select  priority Level(type HIGH,MEDIUM,LOW)')
        Material = ToDoMaterial.toDoMaterial(title, desc, DateTime, Level, False)
        ToDoMch.toDoMech.ToDoMaterials.append(Material)
        print(ToDoMch.toDoMech.ToDoMaterials[0].GetTitle())

    def LıstAllTodos(self):
        for x in ToDoMch.toDoMech.ToDoMaterials:
            print(x.GetTitle() + "  " + x.getDescription() + "   " + "  " + x.getLevel() + " " + str(
                x.GetIsCompleted()) + "    " + str(x.getDateTime()))

    def UpdateItem(self):
        todo = ToDoMch.toDoMech
        t = Typing()
        if len(ToDoMch.toDoMech.ToDoMaterials) > 0:
            try:
                update = input("Please type the  name at you want to update the item first")
            except:

                Typing.UpdateItem()
                return 0
            if update.__eq__("title"):
                NewTitle = input(
                    "Please first write the index number and the new title you want to change, leaving a space.\n" +
                    "(for example \"1" +
                    " sample\")")
                try:
                    NewTitlee = NewTitle.split(" ")
                    IndexNumber = int(NewTitlee[0])
                    todo = ToDoMch.toDoMech
                    todo.ToDoMaterials[IndexNumber].SetTitle(NewTitlee[1])
                except Exception:
                    print("Please type valid characters")
                    t.UpdateItem()
            else:
                print("title word It should be between 3 and 100 letters, Please try again. ")
                t.UpdateItem()
                return 0
        if update.__eq__("Description"):
            NewDesc = input(
                "Please first type the index number and the new description you want to change, leaving a space.\n" +
                "(for example \"1" +
                " sample\")")

            try:
                NewDescc = NewDesc.split(" ")
                IndexNumber = int(NewDescc[0])
                todo = ToDoMch.toDoMech
                todo.ToDoMaterials[IndexNumber].setDescription(IndexNumber)
                print("Successfully")
                return 0

            except Exception:
                print("Please type valid characters")
                t.UpdateItem()

    def ComplatedItem(self):
        t = Typing()

        try:
            IndexNumber = input("Please type the index number to you want to completed Item")
            IndexNumber = int(IndexNumber)
            todo = ToDoMch.toDoMech
            todo.ToDoMaterials[IndexNumber].SetIsCompleted(True)
            print("Successfully")
        except Exception:
            print("Please try again")
            t.ComplatedItem()

    def DeleteItem(self):
        t = Typing()
        DeleteItemIndex = input("Please type the index number to you want to delete Item")
        DeleteItemIndex = int(DeleteItemIndex)
        try:
            todo = ToDoMch.toDoMech
            todo.ToDoMaterials.pop(DeleteItemIndex)
            print("Successfully")
        except Exception:
            print("Please try again")
            t.DeleteItem()

    def ShowList(self):
        t = Typing()
        todo = ToDoMch.toDoMech.commandList
        for x in todo:
            print(x)

    def NotComplete(self):
        t = ToDoMch.toDoMech()
        for x in t.ToDoMaterials:
            if x.GetIsCompleted:
                print(x.GetTitle() + "  " + x.getDescription() + "   " + "  " + x.getLevel() + " " + str(
                    x.GetIsCompleted()) + "    " + str(x.getDateTime()))
