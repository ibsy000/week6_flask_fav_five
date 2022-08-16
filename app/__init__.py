# <!-- Using Flask, create a project that lists your top 5 
#     favorite artists, sports figures, historical figues, etc. Your project 
#     should have the following features:

# Steps:
# - Create project folder **CHECK**
# - Create virtual environment: python -m venv {name_of_environment}  **CHECK**
# - Activate virtual environment:  **CHECK**
#      - Windows: {name_of_environment}\Scripts\activate
# - Install python module: pip install flask  **CHECK**
# - Create instance of Flask class  **CHECK**
# - Create two routes using @app.route  **CHECK**
#     - A Home/index route - Can be generic, nothing fancy but feel free to make 
#       it look however you'd like
#     - A "Favorite 5" route - Pass through your list of five favorites and 
#       display them all nicely in the template -->


from flask import Flask

app = Flask(__name__)


from . import routes