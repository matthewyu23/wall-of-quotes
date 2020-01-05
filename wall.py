from flask import Flask, render_template, url_for
import sqlite3
connection =  sqlite3.connect("posts.sql")
cursor = connection.cursor()

app = Flask(__name__)
#posts = [{"author" : "hehe", "date_posted" : "2019", "title": "haha", "content": "hoho"}, {"author" : "hehe", "date_posted" : "2019", "title": "haha", "content": "hoho"}, {"author" : "hehe", "date_posted" : "2019", "title": "haha", "content": "hoho"}, {"author" : "hehe", "date_posted" : "2019", "title": "haha", "content": "hoho"}]
cursor.execute("SELECT * FROM posts;")
posts = cursor.fetchall() 


@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html", posts=posts)

@app.route('/about')
def about():
    return render_template("about.html", title="about")