class Domino:
    def __init__(self,v1,v2):
        self.v1 = v1
        self.v2 = v2
    def draw_tab(self):
        return "[{}|{}]".format(self.v1,self.v2)
        
  