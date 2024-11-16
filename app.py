'''1. Реалізувати структуру бази данних турів, скрипт який буде заповнювати базу данних 
   2. Вивести ці тури в HTML файл'''

from flask import Flask, render_template
from models import db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db.init_app(app)

@app.route("/")
def main():
    pass

if __name__ == "__main__":
    app.run(debug=True)