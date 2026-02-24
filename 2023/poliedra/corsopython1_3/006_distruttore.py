class Led:
    def __init__(self):
        print("init")
        self.__temp = 20
        self.__colore = "WHITE"
    
    def __del__(self):
        print("distruttore")
    
    
l1 = Led()
del l1


