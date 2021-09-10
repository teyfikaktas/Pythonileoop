class TodoSettings:
    Reset_Color = "\u001B[0m"
    COLO = "\u001B[30m"
    Color_Red = "\u001B[31m"
    Color_Green = "\u001B[32m"
    Color_Yellow = "\u001B[33m"
    Color_Blue = "\u001B[34m"
    Renk_Mor = "\u001B[35m"
    Color_Cyan = "\u001B[36m"
    Color_White = "\u001B[37m"
    __AssistantName = "Jahona"

    def GetAssistantName(self):
        return self.__AssistantName

    def SetAssistantName(self, __AssistantName):
        self.__AssistantName = __AssistantName
