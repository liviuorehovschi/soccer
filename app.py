from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Function to assign players to teams
def assign_teams(players, team_size):
    random.shuffle(players)
    return [players[i:i + team_size] for i in range(0, len(players), team_size)]

# Home page route
@app.route('/')
def index():
    return render_template('index.html')

# Team assignment page route
@app.route('/assign_teams', methods=['GET', 'POST'])
def assign_teams_page():
    teams = None
    if request.method == 'POST':
        player_names = request.form.get('player_names').split(',')
        team_size = int(request.form.get('team_size'))
        teams = assign_teams(player_names, team_size)
    return render_template('assign_teams.html', teams=teams)


# Coin toss page route
@app.route('/coin_toss', methods=['GET', 'POST'])
def coin_toss_page():
    result = None
    if request.method == 'POST':
        result = random.choice(['Team A gets the ball', 'Team B gets the ball'])
    return render_template('coin_toss.html', result=result)


# Track game time page route
@app.route('/track_time')
def track_time_page():
    # Implement your timer logic here
    return render_template('track_time.html')

if __name__ == '__main__':
    app.run(debug=True)
