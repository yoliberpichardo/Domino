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
        self.search_in_turn = ''
        self.index_v = []
        self.token_inv = ''
        self.token_turn = ''
           
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
    
    # def a_shift_change(self):
    #     while looking in range(4):
      
    def shift_change(self): # funcion para cambio de turno
        self.creator_tokens()
        self.random_tokens()
        self.assign_shifts()
        for self.search_in_turn in self.turn:
            if len(self.table) == 0:
                toke6 = self.return_token6(self.search_in_turn)
                if self.return_token6(self.search_in_turn):
                    self.table.append(toke6)
                    self.search_in_turn.remove(toke6)
                    print(self.search_in_turn)
            elif len(self.table) > 0:
                print('table',self.table)
                print(self.search_in_turn)
                self.direccion()
            
    
    def direccion(self):# funcion para poner la ficha en la direccion correcta
        enter_index = int(input('enter the index of the file to choose:'))
        for  checks_turn in self.turn:
            for checks_table in self.table:
                self.index_v.append(checks_turn[enter_index])
                print(self.index_v[0])
                input_direccion = str(input('enter the address of the card: ').upper())
                if input_direccion == 'L':
                    if len(self.table) > 0:
                        if self.index_v[0][1] == checks_table[1] or self.index_v[0][3] == checks_table[1]:
                            if self.index_check_left(self.index_v,self.table):
                                self.table.insert(0,self.index_check_left(self.index_v,self.table))
                                self.index_v.pop()
                                return self.table
                        else:
                            # system('cls')
                            print('enter the index again that date does not match the table')
                            self.index_v.pop()
                            self.direccion()
                            enter_index = int(input('enter the index of the file to choose:'))
                            
                elif input_direccion == 'R':
                    if len(self.table) > 0:
                        if self.index_v[0][1] == checks_table[3] or self.index_v[0][3] == checks_table[3]:
                            if self.index_check_right(self.index_v,self.table):
                                self.table.append(self.index_check_right(self.index_v,self.table))
                                self.index_v.pop()
                                return self.table
                                
                        else:
                            # system('cls')
                            print('enter the index again that date does not match the table')
                            self.index_v.pop()
                            self.direccion()
                            enter_index = int(input('enter the index of the file to choose:'))
                
                else:
                    # system('cls')
                    print('enter the index again that date does not match the table')
                    self.direccion()
                    
    def  index_check_right(self,index_v,table): # funcion de chequeo de la posicion derecha
        for rec_table in table:
            for rec_turn in self.index_v:
                if self.index_v[0][1] == self.table[-1][3]:
                    return self.index_v[0]
                elif self.index_v[0][3] == self.table[-1][3]:
                    self.invest_token(self.index_v)
                    return self.index_v[0]
                    
                
    def  index_check_left(self,index_v,table): # funcion de chequeo de la posicion izquierda
        for rec_table in table:
            for rec_turn in self.index_v:
                if self.index_v[0][1] == self.table[0][1]:
                    self.invest_token(self.index_v)
                    return self.index_v[0]
                elif self.index_v[0][3] == self.table[0][1]:
                    return self.index_v[0]
                           
    def invest_token(self,index_v):# funcion para invertir los indices de las fichas
        index_3 = 0
        index_1 = 0
        token_1 = ''
        for num1 in self.index_v:
            for num2 in num1:
                if num1[0] == num2:
                    index_3 = num1[1]
                    index_1 = num1[3] 
                    token_1 = '[{}|{}]'.format(index_1,index_3)
                self.index_v.pop()
                self.index_v.append(token_1)  
                return self.index_v
        
                                 
domi = Board()   
print(domi.shift_change())

# turn = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

# def turn_ch(turn):
#     for search in turn:
#         print(search)
#         for se_search in search:
#             print(se_search)
        
            
# turn_ch(turn)



