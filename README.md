# Pitch-Desk
Pitch desk is a platform where users can view multiple pitches from different categories e.g Movies, Products and Jobs. Users can comment on this pitches, they can also add their pitches, upon signing up. Users can also view/Edit their profiles.

## Prerequisites
- Have Git installed.
- Have Python and Pip Installed
- Have a text editor or an IDE installed e.g VS Code, Atom
### Technologies Used
- Python, Flask, CSS and HTML
- VS Code.
### Setup Installation
To run the application:-
1. Clone the repository to a folder in your machine using `https://github.com/joanwanjiku/pitch-desk.git`
2. Cd to that folder.
3. Create a virtual environment using `python3 -m venv virtual`
4. Activate the virtual environment using `source virtual/bin/activate`
5. Install all the flask packages in 'requirements.txt' using `pip install <package-name>`.
6. Run:-
    - `python3 manage.py db init`- Creates a migrations folder and database with all the tables
    - `python3 manage.py db migrate`
    - `python3 manage.py db upgrade`

3. Open the project on your Text Editor/IDE
4. Run `./start.sh` on your terminal


#### Author
- Joan Wanjiku
    - joanevans18@gmail.com
#### License
Copyright &copy; 2020