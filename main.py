from flask import Flask, render_template, url_for


app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
  return render_template('about.html', title = 'About')

@app.route('/register')
def register():
  return 'This is the registration page'

@app.route('/login')
def login():
  return 'This is the log on page'

app.run(host='0.0.0.0', port=81,debug=True)
