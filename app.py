from flask import render_template, Flask, request

app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
def index():
    # with open('index.html', 'r') as f:
    #     content = f.read()
    # return content
    return render_template('index.html')

@app.route('/about.html')
def about():
    return render_template('about.html')