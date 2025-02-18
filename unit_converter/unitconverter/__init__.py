import os
from flask import Flask
from unitconverter.database.db import DatabaseHandler

cwd = os.getcwd()

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

app.config['SQLALCHEMY_DATABASE_URI'] = f'{cwd}+/unitconverter/database/lookup.db'

db = DatabaseHandler()


from unitconverter import routes