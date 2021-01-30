from players import *
from tab_domino import Domino
from random import *
class Board:
    def __init__(self):
        self.tab_list = []
        
        
        
    def search(self,tab): #funcion para que no guarde fichas repetidas en la lista
        for i in range(len(self.tab_list)): 
            if self.tab_list[i].v1 == tab.v2 and self.tab_list[i].v2 == tab.v1: 
                return True 
        return False
        
    def creator_tokens(self): #funcion para crear las fichas 
        for x in range(7):
            for y in range(7):
                tab = Domino(x,y)
                if len(self.tab_list) == 0 or self.search(tab) == False : 
                    self.tab_list.append(tab) 
                    # print(tab.draw_tab())
        return self.tab_list
    
    def random_tokens(self):
        list_player = Players()
        self.creator_tokens()
        for cont_players in range(4):
            for r in range(7):
                token = choice(self.tab_list)
                if len(list_player.tokens_p1) <  7:
                    list_player.tokens_p1.append(token)
                elif len(list_player.tokens_p2) <  7:
                    list_player.tokens_p2.append(token)
                elif len(list_player.tokens_p3) <  7:
                    list_player.tokens_p3.append(token)
                elif len(list_player.tokens_p4) <  7:
                    list_player.tokens_p4.append(token)
                
        return list_player.tokens_p1,list_player.tokens_p2,list_player.tokens_p3,list_player.tokens_p4
            
                
                
domi = Board()   
print(domi.random_tokens())


