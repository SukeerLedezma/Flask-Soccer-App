from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class League(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    games_played = db.Column(db.Integer, default=0)
    viewers = db.Column(db.Integer, default=0)
    logo = db.Column(db.String(100), nullable=False)

    teams = db.relationship('Team', backref='league', cascade='all, delete-orphan')

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    goals = db.Column(db.Integer, default=0)
    games_played = db.Column(db.Integer, default=0)
    wins = db.Column(db.Integer, default=0)
    formation = db.Column(db.String(20))
    best_player = db.Column(db.String(100))

    league_id = db.Column(db.Integer, db.ForeignKey('league.id', ondelete='CASCADE'))
    players = db.relationship('Player', backref='team', cascade='all, delete-orphan')

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    goals_scored = db.Column(db.Integer, default=0)
    preferred_foot = db.Column(db.String(10))
    position = db.Column(db.String(20))
    nationality = db.Column(db.String(50))
    team_id = db.Column(db.Integer, db.ForeignKey('team.id', ondelete='CASCADE'))

def soccer_data():
    try:
        print("Creating sample data...")

        if League.query.count() == 0:
            premier_league = League(name='Premier League', location='England', logo='images/premier(1).jpg')
            la_liga = League(name='La Liga', location='Spain', logo='images/laliga.jpg')
            bundesliga = League(name='Bundesliga', location='Germany', logo='images/bundesliga(1).jpg')

            db.session.add_all([premier_league, la_liga, bundesliga])
            db.session.commit()

            if Team.query.count() == 0:
                arsenal = Team(name='Arsenal', formation='4-3-3', best_player='Bukayo Saka', league=premier_league, logo='images/arsenellogo.jpg')
                real_madrid = Team(name='Real Madrid', formation='4-4-2', best_player='Jude Bellingham', league=la_liga, logo='images/realmadridlogo.jpg')
                bayern_munich = Team(name='Bayern Munich', formation='4-2-3-1', best_player='Harry Kane', league=bundesliga, logo='images/BayernMunichlogo.jpg')

                db.session.add_all([arsenal, real_madrid, bayern_munich])
                db.session.commit()

                if Player.query.count() == 0:
                    player1 = Player(name='Bukayo Saka', goals_scored=12, preferred_foot='Left', position='Striker', nationality='English', team=arsenal, image='images/bukayosaka.jpg')
                    player2 = Player(name='Jude Bellingham', goals_scored=11, preferred_foot='Right', position='Midfielder', nationality='England', team=real_madrid, image='images/judebellingham.jpg')
                    player3 = Player(name='Harry Kane', goals_scored=18, preferred_foot='Right', position='Striker', nationality='Norwegian', team=bayern_munich, image='images/harrykane.jpg')

                    db.session.add_all([player1, player2, player3])
                    db.session.commit()

    except Exception as e:
        print(f"Error in create_sample_data: {e}")

    print("Sample data creation complete.")

# Routes
@app.route('/')
def index():
    print("Fetching leagues...")
    leagues = League.query.all()
    print("Fetched leagues:", leagues)
    return render_template('index.html', leagues=leagues)

@app.route('/league/<int:league_id>')
def league(league_id):
    league = League.query.get(league_id)
    teams = league.teams
    return render_template('league.html', league=league, teams=teams)

@app.route('/team/<int:team_id>')
def team(team_id):
    team = Team.query.get(team_id)
    players = team.players
    return render_template('team.html', team=team, players=players)

@app.route('/player/<int:player_id>')
def player(player_id):
    player = Player.query.get(player_id)
    return render_template('player.html', player=player)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        soccer_data()
    app.run(debug=True)
