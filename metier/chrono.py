import tkinter 

###marche pas
class Chrono(tkinter.Label):
    '''
    Classe permettant d'obtenir la vitesse avec laquelle un joueur gagne une partie.
    '''
    def __init__(self,root,startTime=0):
        tkinter.Label.__init__(self,root,text='Starting...')
        
        self.value=startTime
        self.font=('Helvetica', 36, 'normal')
        self.__setitem__('font',self.font)
        self.after(1000,self.count)
    
    def formatTime(self):
        return str(self.value/60)+': '+str(self.value%60)
    
    def count(self):
        self.value=self.value+1
        self.__setitem__('text',self.formatTime())
        self.after(1000,self.count)
        
if __name__=="__main__":
    
    root = tkinter.Tk() 
    root.title('Chrono')
    label = Chrono(root)