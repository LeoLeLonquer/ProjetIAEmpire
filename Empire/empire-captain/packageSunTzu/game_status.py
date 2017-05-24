
class Game_status :
    def __init__(self):
        self.player_id=None
        self.turn=0
        # self.the_map=the_map


    def get_player_id(self):
        return self.player_id

    def set_player_id(self,id):
        self.player_id=id

    def get_turn(self):
        return self.turn

    # def get_map(self):
    #     return self.the_map

    def add_turn(self):
        self.turn=self.turn+1
