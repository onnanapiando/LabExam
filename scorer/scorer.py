from random import *
class Scorer(object):
    def add_team(self, team1, team2):
        self.team1 = team1
        self.team2 = team2
        team1 = raw_input("Enter team name: ");
        print "Team 1 is: ", team1
        
        team2 = raw_input("Enter team name: ");
        print "Team 2 is: ", team2
        
    def score(self, x, y):
        random  = Random()
        for i in range(0,10): 
            team = random.randint(1,2)
            total_1 = 0
            total_2 = 0            
            if team == 1:
                score = random.randint(2,3)
                print "Team 1 scores", score
                total_1+=score
            else:
                score = random.randint(2,3)
                print "Team 2 scores", score
                total_2+=score
