from random import *
class Scorer(object):
    '''def __init__(self, score_x, score_y):
        self.score_x = score_x
        self.score_y = score_y'''

    def score(self, x, y):
        random  = Random()
        for i in range(0,10):
            score_x = random.randint(2,3)
            score_y = random.randint(2,3)
            print "Team 1 scores" ,score_x 
            print "Team 2 scores" ,score_y 

