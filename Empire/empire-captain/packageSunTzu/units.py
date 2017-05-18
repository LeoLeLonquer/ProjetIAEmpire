
class piece:
    def __init__(self,pieceid,piecetypeid,x,y):
        self.pieceid=pieceid
        self.piecetypeid=piecetypeid
        self.x=x
        self.y=y

    def get_pieceid(self):
        return pieceid

    def get_piecetypeid(self):
        return piecetypeid

    def get_x(self):
        return x

    def get_y(self):
        return y

    def get_position(self):
        return x,y


class pieceslist:
    def __init__(self):
        self.piecesdico={}

    def get_piecesdico(self):
        return self.piecesdico

    def get_piece(self,pieceid):
        if (piecesid in self.piecesdico.keys()):
            return piecesdico[pieceid]
        else :
            return none

    def add(self,pieceid,piece):
        self.piecesdico[piece.get_pieceid()]=piece

    def remove(self,pieceid):
        if (piecesid in self.piecesdico.keys()):
            del self.pieceid[pieceid]


class piecetype:
    def __init__(self,id,name,symbol,move):
        self.id=id
        self.name=name
        self.symbol=symbol
        self.move=move

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_symbol(self):
        return self.symbol

    def get_move(self):
        return self.move



class piecetypelist:
    def __init__ (self):
        self.piecestypesdico= {0:piecetype(0,"ARMY",'A',1),
                               1:piecetype(1,"FIGHT",'F',8),
                               2:piecetype(2,"TRANSPORT",'T',2),
                               3:piecetype(3,"PATROL",'P',4),
                               4:piecetype(4,"BATTLESHIP",'B',2)}



    def get_piecestypesdico(self):
        return self.piecestypesdico

    def get_piecetype(self,piecetypeid):
        if (piecetypeid in self.piecestypesdico.key()):
            return piecetypedico[piecetypeid]
        else :
            return None
