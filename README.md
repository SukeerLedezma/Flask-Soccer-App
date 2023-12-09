## Flask-Soccer-App
This is a simple web app for displaying information about soccer leagues, teams, and players.

## Project Objectives
To display leagues and their information
Once the information is displayed, a link to a team belonging to the league should be available to click
Once the the team link is clicked, it should display information regarding the team and a player link should be available
Once the player link is accessed, it should display information about a player belonging to the team, their stats, etc

## Project Structure

The project is organized with the following directory structure:

- `static`: Contains static files such as images and styles.
    - `images`: Stores images for leagues, teams, and players.
    - `style.css`: CSS file for styling.

- `templates`: Contains HTML templates for different pages in the app.
    - `index.html`: Home page displaying top soccer leagues.
    - `layout.html`: Base template for common elements shared across pages.
    - `league.html`: Page displaying information about a specific soccer league.
    - `team.html`: Page displaying information about a specific soccer team.
    - `player.html`: Page displaying information about a specific soccer player.
    
- `app.py`: Main Python file containing the Flask application and database setup.
    - Defines the data models for leagues, teams, and players.
    - Includes routes for rendering HTML pages and fetching data from the database.

## Documented Issues
- The purpose of the index page is to show the top 3 leagues, however, the three leagues repeat many times. 
- Images are not showing up for the perspective leagues, teams, and players. The error I’m seeing is that the images aren’t being retrieved from my images folder, which 
  causes the database not to display the images.
- Any changes added to the CSS file do not cause any changes to the website, hence the very basic design

## Project dependencies
- Flask
- Flask SQLAlchemy

## To clone the repository
- git clone https://github.com/SukeerLedezma/Flask-Soccer-App.git

## Sources for information
https://one-versus-one.com/en/players/jude-bellingham
https://en.as.com/resultados/ficha/deportista/bukayo_saka/44896/2022/estadisticas/inglaterra/
https://www.transfermarkt.us/18-goals-in-12-games-will-harry-kane-break-robert-lewandowskis-bundesliga-record-/view/news/430558#:~:text=As%20previously%20mentioned%2C%20Kane%20already,in%20the%20English%20top%2Dflight.

https://theanalyst.com/na/2023/08/the-strongest-leagues-in-world-football-opta-power-rankings/

https://formation-y.com/en/formation/arsenal.html
https://fbref.com/en/squads/18bb7c10/Arsenal-Stats

https://formation-y.com/en/formation/real_madrid.html
https://fbref.com/en/squads/53a2f082/Real-Madrid-Stats

https://formation-y.com/en/formation/bayern.html
https://fbref.com/en/squads/054efa67/Bayern-Munich-Stats

## Author
Sukeer Ledezma
