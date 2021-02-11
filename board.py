from players import *
from tab_domino import Domino
from random import *
player1 = Players()
player2 = Players()
player3 = Players()
player4 = Players()
class Board:
    def __init__(self):
        self.tab_list = []
        self.token = ''
        self.player = ''
        
        
        
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
    
        
    def random_tokens(self):# funcion para repartir las fichas a los jugadores
        self.creator_tokens()
        for cont_players in range(4):
            for r in range(7):
                self.token = choice(self.tab_list)
                if len(player1.tokens_player) <  7:
                    player1.tokens_player.append(self.token.draw_tab())
                    self.token = ''
                elif len(player2.tokens_player) <  7:
                    player2.tokens_player.append(self.token.draw_tab())
                    self.token = ''
                elif len(player3.tokens_player) <  7:
                    player3.tokens_player.append(self.token.draw_tab())
                    self.token = ''
                elif len(player4.tokens_player) <  7:
                    player4.tokens_player.append(self.token.draw_tab())
                    self.token = ''
                
        return player1.tokens_player, player2.tokens_player, player3.tokens_player, player4.tokens_player
        
    def find_token6(self,player):
        print(player1.tokens_player)
        for rec1 in player.tokens_player:
            print(int(rec1[1]) + int(rec1[3]) )
            if int(rec1[1]) + int(rec1[3]) == 12:
                return True
        return False
    
    def token_max(self):
        self.random_tokens()
        # print(self.find_token6(player1))
        for rec2 in range(4):
            if self.find_token6(player1) == True:
                return player1.tokens_player
            
            elif self.find_token6(player2) == True:
                return player2.tokens_player
            
            elif self.find_token6(player3) == True:
                return player3.tokens_player
            
            elif self.find_token6(player4) == True:
                return player4.tokens_player
            
                           
domi = Board()   
domi.random_tokens()
print(domi.token_max())



