from flask import Flask, render_template,redirect, url_for, request, session
from bson import ObjectId
from datetime import datetime
import hashlib
import time
import mysql.connector

mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="",
	database="domaci0607"
)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'decembar2020'

@app.route('/')
@app.route('/raspored')
def raspored():
	cursor = mydb.cursor()
	cursor.execute("SELECT * FROM raspored")
	raspored = cursor.fetchall()
	cursor.execute("SELECT DISTINCT vreme FROM raspored")
	ucionica = cursor.fetchall()
	cursor.execute("SELECT DISTINCT nastavnik FROM raspored ORDER BY nastavnik ASC")
	nastavnik = cursor.fetchall()
	return render_template("raspored.html",raspored=raspored,ucionica=ucionica,nastavnik=nastavnik)

if __name__ == '__main__':
	app.run(debug=True)
