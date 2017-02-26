class girl:
    def __init__(self,name,attractiveness,budget,intelligence):
        self.name=name
        self.attractiveness=attractiveness
        self.budget=budget
        self.intelligence=intelligence
        self.status='single'
        self.bf=""

    def is_elligible(self,boy):
        if (self.budget<=boy.budget):
            return True
        else:
            return False
        
