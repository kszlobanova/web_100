from flask import render_template, Flask, request

app = Flask(__name__)

@app.route('/')

@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/about_rus.html')
def about_rus():
    return render_template('about_rus.html')


@app.route('/about_eng.html')
def about_eng():
    return render_template('about_eng.html')