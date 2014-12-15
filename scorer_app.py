from flask import *
from scorer.scorer import *

APP = Flask(__name__)
SCORER = Scorer()

@APP.route('/')
def hello_world():
    return render_template('index.html')

@APP.route('/team/')
def team():    
    team1get = request.args.get('team1')
    team2get = request.args.get('team2')
    team1 = SCORER.add_team(team1get)
    team2 = SCORER.add_team(team2get)
    
    return render_template('success.html', team1=team1, team2=team2)

if __name__ == '__main__':
    APP.run(debug=True)