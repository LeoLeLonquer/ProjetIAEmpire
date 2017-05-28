
class Piece:
    def __init__(self,pieceid,piecetypeid,x,y):
        self.pieceid=pieceid
        self.piecetypeid=piecetypeid
        self.x=x
        self.y=y

    def get_pieceid(self):
        return self.pieceid

    def get_piecetypeid(self):
        return self.piecetypeid

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_position(self):
        return self.x,self.y

    def set_position(self,x,y):
        self.x=x
        self.y=y

class Pieceslist:
    def __init__(self):
        self.piecesdico={}

    def get_pieces(self):
        return self.piecesdico

    def get_piece(self,pieceid):
        if (pieceid in self.piecesdico.keys()):
            return self.piecesdico[pieceid]
        else :
            return None

    def add(self,pieceid,piece):
        self.piecesdico[piece.get_pieceid()]=piece

    def remove(self,pieceid):
        if (pieceid in self.piecesdico.keys()):
            del self.piecesdico[pieceid]


class Piecetype:
    def __init__(self,id,name,symbol,move,terrain):
        self.id=id
        self.name=name
        self.symbol=symbol
        self.move=move
        self.terrain=terrain

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_symbol(self):
        return self.symbol

    def get_move(self):
        return self.move

    def get_terrain(self):
        return self.terrain



class Piecestypeslist:
    def __init__ (self):
        self.piecestypesdico= {0:Piecetype(0,"ARMY",'A',1,{'B':"GROUND"}),
                               1:Piecetype(1,"FLIGHT",'F',8,{'B':'GROUND','A':"Water"}),
                               2:Piecetype(2,"TRANSPORT",'T',2,{'A':"Water"}),
                               3:Piecetype(3,"PATROL",'P',4,{'A':"Water"}),
                               4:Piecetype(4,"BATTLESHIP",'B',2,{'A':"Water"})
                               }
        self.nbpiecetype=10 #TODO a modifier automatiquement
        self.allied_units=['C','M','N','O','P','Q']
        self.ennemy_units=['D','W','X','Y','Z']

    def get_piecestypesdico(self):
        return self.piecestypesdico

    def get_nbpiecetype(self):
        return self.nbpiecetype

    def get_piecetype(self,piecetypeid):
        if (piecetypeid in self.piecestypesdico.keys()):
            return self.piecestypesdico[piecetypeid]
        else :
            return None

    def get_allied_units(self):
        return self.allied_units

    def get_ennemy_units(self):
        return self.ennemy_units
