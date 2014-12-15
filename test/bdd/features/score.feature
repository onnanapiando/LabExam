Feature: Tally score application

         As the scorer, I wish to be able to record scores made in the said basketball competition


        Scenario:
        Given "team1" shoots the ball
        When the team shoots the ball and scored "2"
        Then the system updates the score of the team

