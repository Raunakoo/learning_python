#importing modules

from character import Pig

from polygon import Polygon
###########################################################


class Level():

    def __init__(self, pigs, columns, beams, space):

        self.pigs = pigs
        self.columns = columns
        self.beams = beams
        self.space = space
        self.number = 0
        #the more birds you create the easier the game becomes
        self.number_of_birds = 4
        #########################################################

        self.bool_space = False

    def build0(self):

        #level 0
        #creating pigs,  the more pigs you create the harder the game becomes
        pig1 = Pig(980, 100, self.space)

        pig2 = Pig(985, 182, self.space)

        self.pigs.append(pig1)
        self.pigs.append(pig2)

        #create beam and column

        p = (950, 80)

        self.columns.append(Polygon(p, 20, 85, self.space))

        p = (1010, 80)
        self.columns.append(Polygon(p, 20, 85, self.space))

        p = (980, 150)
        self.beams.append(Polygon(p, 20, 85, self.space))

        p = (950, 200)
        self.columns.append(Polygon(p, 20, 85, self.space))
        
        p = (1010, 200)
        self.colums.append(Polygon(p, 20, 85, self.space))

        p = (980, 240)
        self.beams.append(Polygon(p, 20, 85, self.space))

        self.number_of_birds = 4
        if self.bool_space == true:

            self.number_of_birds = 8

    def load_level(self):

        try:
            build_name = "build" + str(self.number)
            getattr(self, build_name) ()

        except AttributeError:
            self.number = 0
            build_name = getattr(self, build_name)