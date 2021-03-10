from players import *
from tab_domino import Domino
from random import *
from os import system
player1 = Players()
player2 = Players()
player3 = Players()
player4 = Players()
class Board:
    def __init__(self):
        self.tab_list = []
        self.token = ''
        self.player = ''
        self.table = []
        self.turn = []
        self.input_domi = ''
        
        
        
        
    def search(self,tab): #funcion para que no guarde fichas repetidas en la lista
        for i in range(len(self.tab_list)): 
            if self.tab_list[i].v1 == tab.v2 and self.tab_list[i].v2 == tab.v1: 
                return True 
        return False
        
    def creator_tokens(self): #funcion para crear las fichas 
        for x in range(7):
            for y in range(7):
                tab = Domino(x,y) #[0|1] [1|0]
                if len(self.tab_list) == 0 or self.search(tab) == False: 
                    self.tab_list.append(tab) 
        return self.tab_list
    
        
    def random_tokens(self):# funcion para repartir las fichas a los jugadores
        for cont_players in range(4):
            for r in range(7):
                self.token = choice(self.tab_list)
                if len(player1.tokens_player) <  7:
                    player1.tokens_player.append(self.token.draw_tab())
                    self.tab_list.remove(self.token)
                    self.token = ''
                elif len(player2.tokens_player) <  7 :
                    player2.tokens_player.append(self.token.draw_tab())
                    self.tab_list.remove(self.token)
                    self.token = ''
                elif len(player3.tokens_player) <  7:
                    player3.tokens_player.append(self.token.draw_tab())
                    self.tab_list.remove(self.token)
                    self.token = ''
                elif len(player4.tokens_player) <  7 :
                    player4.tokens_player.append(self.token.draw_tab())
                    self.tab_list.remove(self.token)
                    self.token = ''
          
        return player1.tokens_player, player2.tokens_player, player3.tokens_player, player4.tokens_player
        
    def find_token6(self,player): # funcion para comprobar el jugador que tenga el doble seis 
        for travels in player.tokens_player:
            if int(travels[1]) + int(travels[3]) == 12:
                return True
        return False
        
    def assign_shifts(self): # funcion para buscar la ficha mas alta, solo al iniciar
        while True:
            if self.find_token6(player1):
                self.turn = [player1.tokens_player,player2.tokens_player, player3.tokens_player, player4.tokens_player]
                return self.turn
            
            elif self.find_token6(player2):
                self.turn = [player2.tokens_player, player3.tokens_player, player4.tokens_player, player1.tokens_player]
                return self.turn
            
            elif self.find_token6(player3):
                self.turn = [player3.tokens_player,player4.tokens_player, player1.tokens_player, player2.tokens_player]
                return self.turn
            
            else:
                self.turn = [player4.tokens_player, player1.tokens_player, player2.tokens_player, player3.tokens_player]
                return self.turn
        

    def return_token6(self,turn): # funcion para delvolver el doble seis
        for travels in turn:
            if int(travels[1]) + int(travels[3]) == 12:
                return travels
        return False    
      
    def shift_change(self): 
        self.creator_tokens()
        self.random_tokens()
        self.assign_shifts()
        cont = range(4) 
        for search_in_turn in self.turn:#turn[p1,p2,p3,p4]
            for search_in_search in search_in_turn:#p2[[3|6],[0|2],[2|4]]
                if len(self.table) == 0:
                    system('cls')
                    # display_player = "player{} ->".format(1)
                    print('table',self.table)
                    print("player{} ->".format(1),search_in_turn)
                    if self.return_token6(search_in_turn) == search_in_search:
                        self.table.append(search_in_search)
                        search_in_turn.remove(search_in_search)
                        # print(search_in_turn)
                elif len(self.table) > 0:
                    system('cls')
                    print(search_in_turn)
                    print('table: ',self.table)
                    print("player{} ->".format(cont),search_in_turn)
                    input_direccion = str(input('enter the address of the card: ').upper())
                    if input_direccion == 'L':
                        self.table.insert(0,search_in_search)
                        search_in_turn.remove(search_in_search)
                        cont += 1
                        print(search_in_turn)
                    elif input_direccion == 'R':
                        self.table.append(search_in_search)
                        search_in_turn.remove(search_in_search)
                        cont += 1
                        # print(search_in_turn)
                    else:
                        system('cls')
                        print('just enter a correct address is left "L" or right "R"')     
                    
                    

            
                
                
    # def choose_cards(self): 
    #     cont = 4
    #     while cont > 0:
    #         self.shift_change()
    #         cont -= 1
        
                           
domi = Board()   
print(domi.shift_change())


