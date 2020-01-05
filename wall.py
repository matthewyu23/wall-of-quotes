from flask import Flask, render_template, url_for

app = Flask(__name__)
posts = [{"author" : "hehe", "date_posted" : "2019", "title": "haha", "content": "hoho"}, {"author" : "hehe", "date_posted" : "2019", "title": "haha", "content": "hoho"}, {"author" : "hehe", "date_posted" : "2019", "title": "haha", "content": "hoho"}, {"author" : "hehe", "date_posted" : "2019", "title": "haha", "content": "hoho"}]


@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html", posts=posts)

@app.route('/about')
def about():
    return render_template("about.html", title="about")