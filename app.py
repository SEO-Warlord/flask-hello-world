from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_autosuggest')
def get_autosuggest():
    query = request.args.get('query')
    url = f'https://suggestqueries.google.com/complete/search?output=firefox&q={query}'
    response = requests.get(url)
    data = response.json()
    suggestions = data[1]
    return {'suggestions': suggestions}
