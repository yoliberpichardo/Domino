from tab_domino import Domino
class Board:
    def creator_domi(self): #funcion para crear las fichas 
        self.tab_list = []
        for x in range(7):
            for y in range(7):
                tab = Domino(x,y)
                if len(self.tab_list) == 0 or self.search(tab) == False : 
                    self.tab_list.append(tab)
                    print(tab.draw_tab()) 
                        
    def search(self,tab): #funcion para que no guarde fichas repetidas en la lista
        for i in range(len(self.tab_list)): 
            if self.tab_list[i].v1 == tab.v2 and self.tab_list[i].v2 == tab.v1: 
                return True 
        return False

domi = Board()   
domi.creator_domi()