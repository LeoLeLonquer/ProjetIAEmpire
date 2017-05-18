import units


class city:
    def __init__(self,cityid,x,y):
        self.cityid = cityid
        self.x=x
        self.y=y
        self.production=None

    def set_production(piecetypeid):
        #if piecetypeid in units.piecetypelist
        self.production=piecetypeid

    def get_cityid():
        return self.cityid

    def get_x():
        return self.x

    def get_y():
        return self.y

    def get_pos():
        return self.x,self.y

    def get_production():
        return self.production



class citieslist:
    def __init__(self):
        self.citiesdico={}

    def add(city):
        self.citiesdico[city.get_cityid()]=city

    def remove(cityid):
        if cityid in self.citiesdico.keys():
            del citiesdico[cityid]
