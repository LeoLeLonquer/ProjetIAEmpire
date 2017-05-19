
class City:
    def __init__(self,cityid,x,y):
        self.cityid = cityid
        self.x=x
        self.y=y
        self.production=None

    def set_production(self,piecetypeid):
        #if piecetypeid in units.piecetypelist
        self.production=piecetypeid

    def get_cityid(self):
        return self.cityid

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_pos(self):
        return (self.x,self.y)

    def get_production(self):
        return self.production



class Citieslist:
    def __init__(self):
        self.citiesdico={}

    def get_cities(self):
        self.citiesdico

    def add(self,city):
        self.citiesdico[city.get_cityid()]=city

    def remove(self,cityid):
        if cityid in self.citiesdico.keys():
            del self.citiesdico[cityid]
