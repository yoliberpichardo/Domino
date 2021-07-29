
class Domino:
    def __init__(self,v1,v2):
        self.v1 = v1
        self.v2 = v2
        
    def draw_tab(self):
        return f'[{self.v1}|{self.v2}]'
        
#     def creator_tokens(self):   
#         """funcion para crear las fichas"""
#         for x in range(7):
#             for y in range(7):
#                 tab = Domino(x, y)  # [0|1]
#                 if len(domino_1.tab_list) == 0 or self.search(tab) == False:
#                     domino_1.tab_list.append(tab)
#         return domino_1.tab_list
    
    
#     def search(self,tab): 
#         """funcion para que no guarde fichas repetidas en la lista"""
#         for i in range(len(self.tab_list)): 
#             if domino_1.tab_list[i].v1 == tab.v2 and domino_1.tab_list[i].v2 == tab.v1: 
#                 return True 
#         return False
    
# dominos = Domino(0,0)
# print(dominos.creator_tokens())
