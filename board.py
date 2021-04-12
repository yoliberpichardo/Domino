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
        self.table = ['']
        self.turn = []
        self.index_v = []
        self.checks_turn = ''
        self.enter_index = ''
        self.input_direccion = ''
        self.its_empty = True
        self.turnCount = 0
        self.corrects_index = ['0','1','2','3','4','5','6']
           
    def search(self,tab): #funcion para que no guarde fichas repetidas en la lista
        for i in range(len(self.tab_list)): 
            if self.tab_list[i].v1 == tab.v2 and self.tab_list[i].v2 == tab.v1: 
                return True 
        return False
        
    def creator_tokens(self): #funcion para crear las fichas 
        for x in range(7):
            for y in range(7):
                tab = Domino(x,y) #[0|1] 
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
    def len_token(self,turn):
        result = ''
        for len_turn in range(len(turn)):
            result += '      '+ str(len_turn) + '  '
        return result

    def direccionv2(self):
        cont_pass_player = 0
        exitGame = False
        while not exitGame:
            while True:
                if self.turnCount < len(self.turn):
                    if self.its_empty == True: 
                        self.insert_index()
                        self.index_v.append(self.turn[self.turnCount][int(self.enter_index)])
                        self.turn[self.turnCount].remove(self.index_v[0])
                        self.insert_token6_in_table(self.table)
                        self.turnCount += 1
                        
                    
                    elif self.its_empty == False:
                        if self.cheeck_table_in_turn(self.table,self.turn[self.turnCount]):
                            self.insert_index()
                            self.index_v.append(self.turn[self.turnCount][int(self.enter_index)])     
                            self.insert_tokens_in_table(self.table) 
                            cont_pass_player = 0
                            
                        elif cont_pass_player > 3:
                            print('El juego esta trancado')     
                            break
                               
                        else:
                            print('the Player{}'.format(self.turnCount+1), 'is no tiene token, its up to the next player')
                            self.turnCount += 1 
                            cont_pass_player += 1  
                            

                else: 
                    self.turnCount = 0
                
                continue
    
    def cheeck_table_in_turn(self,table,turn):# funcion para saber si el jugador pasa 
        cont = 0
        for rec_table in self.table:
            for rec_turn in turn:
                print(table[-1][3],rec_turn[1],table[0][1],rec_turn[3])
                if rec_turn[1] == table[-1][3] or rec_turn[3] == table[-1][3] or rec_turn[1] == table[0][1] or rec_turn[3] == table[0][1]: 
                    cont += 1 
                    return True
                              
        if cont == 0:
            cont = 0
            return False
    
    
    def insert_index(self):
        print('table',self.table)
        print('Player{}'.format(self.turnCount+1),self.turn[self.turnCount])
        print('index',self.len_token(self.turn[self.turnCount]))
        self.enter_index = input('enter the index of the file to choose:')
        
        if self.enter_index not in self.corrects_index:
            system('cls')
            print('enter a number that is in the range of your card or entered a letter')
            print('reenter the index')
            self.enter_index = ''
            self.direccionv2() 
        
        # self.enter_index = int(self.enter_index)
        elif isinstance(self.enter_index,int) or int(self.enter_index) > len(self.turn[self.turnCount]):
            system('cls')
            print('enter a number that is in the range of your card or entered a letter')
            print('reenter the index')  
            self.enter_index = ''
            self.direccionv2()
            
        return self.enter_index
            
   

    def insert_tokens_in_table(self,table):#funcion para agregar las demas ficha en la mesa
        self.input_direccion = input('enter the address of the card: ').upper()
        for checks_table in self.table:
            if not isinstance(self.input_direccion,str):
                # system('cls')
                print('enter the index again that date does not match the table')
                self.insert_tokens_in_table() 
                 
            else:   
                if self.input_direccion == 'L':
                    #aqui debo validar si la ficha coincide por el lado que escoja el jugador
                    if self.index_check_left_is_True(self.index_v,self.table):
                        self.table.insert(0,self.index_check_left(self.index_v,self.table))
                        self.index_v.pop()
                        self.turnCount += 1
                        return self.table
                    
                    elif self.index_check_right_is_True(self.index_v,self.table):
                        print('this token does not go by L but if it goes by R, re-enter the coordinate')
                    
                    else:
                        print('this token does not go on the board,  re-enter the token')   
                        self.index_v.pop()
                        self.direccionv2()
                        
                elif self.input_direccion == 'R':
                    #aqui debo validar si la ficha coincide por el lado que escoja el jugador
                    if self.index_check_right_is_True(self.index_v,self.table):
                        self.table.append(self.index_check_right(self.index_v,self.table))
                        self.index_v.pop()
                        self.turnCount += 1
                        return self.table    
                       
                    elif self.index_check_left_is_True(self.index_v,self.table):
                        print('this token does not go by R but if it goes by L, re-enter the coordinate')                
                
                else:
                    print('this token does not go on the board,  re-enter the token')  
                    self.index_v.pop()
                    self.direccionv2()
                                    
    def  index_check_right(self,index_v,table): # funcion de chequeo de la posicion derecha
        for rec_table in table:
            for rec_turn in self.index_v:
                if self.index_v[0][1] == self.table[-1][3]:
                    return self.index_v[0]
                
                elif self.index_v[0][3] == self.table[-1][3]:
                    self.invest_token(self.index_v)
                    return self.index_v[0]
                
    def  index_check_right_is_True(self,index_v,table): # funcion de chequeo de la posicion derecha si va por ese lado
        for rec_table in table:
            for rec_turn in self.index_v:
                if self.index_v[0][1] == self.table[-1][3] or self.index_v[0][3] == self.table[-1][3]:
                    return True
                
                else:
                    return False
                              
    def  index_check_left(self,index_v,table): # funcion de chequeo de la posicion izquierda
        for rec_table in table:
            for rec_turn in self.index_v:
                if self.index_v[0][1] == self.table[0][1]:
                    self.invest_token(self.index_v)
                    return self.index_v[0]
                
                elif self.index_v[0][3] == self.table[0][1]:
                    return self.index_v[0]
    
    def  index_check_left_is_True(self,index_v,table): # funcion de chequeo de la posicion izquierda  si va por ese lado
        for rec_table in table:
            for rec_turn in self.index_v:
                if self.index_v[0][1] == self.table[0][1] or self.index_v[0][3] == self.table[0][1]:
                    return True
                
                else:
                    return False
                           
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
            
    def check_token6(self,turn):
        for travels in turn:
            if int(travels[1]) + int(travels[3]) == 12:
                return True
            
        return False    
            
    def insert_token6_in_table(self,table):# funcion para agregar la primera ficha en la mesa
        for checks_table in self.table:
            if self.check_token6(self.index_v):
                self.table.remove('')
                self.table.append(self.index_v[0])
                self.index_v.pop()
                self.its_empty = False
                return self.table
            else:
                system('cls')
                print('⚠ ALERT ⚠')
                print('⚠ to place the first chip on the table it has to be [6|6] ⚠')
                self.direccion()
            
                            
                                 
domi = Board()
domi.creator_tokens()
domi.random_tokens()
domi.assign_shifts()
print(domi.direccionv2())
