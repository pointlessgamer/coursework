from flask import Flask, render_template, url_for


app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return 'Hello from Flask!'


@app.route('/about')
def about():
  return 'This is the about page.'


app.run(host='0.0.0.0', port=81)
