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


## Project dependencies
- Flask
- Flask SQLAlchemy

## To clone the repository
