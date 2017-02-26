class boy:
    def __init__(self,name,attractiveness,budget,intelligence,MAQ):
        self.name=name
        self.attractiveness=attractiveness
        self.budget=budget
        self.intelligence=intelligence
        self.status='single'
        self.gf=""
        self.MAQ=MAQ

    def is_elligible(self,girl):
        if (self.budget>=girl.budget) and (girl.attractiveness>=self.MAQ):
            return True
        else:
            return False
