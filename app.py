# app.py
from flask import Flask, jsonify, request, render_template
import json
import os

app = Flask(__name__)
COUNTER_FILE = 'counter.json'

def load_counter():
    if not os.path.exists(COUNTER_FILE):
        return 0
    with open(COUNTER_FILE, 'r') as f:
        return json.load(f).get('count', 0)

def save_counter(count):
    with open(COUNTER_FILE, 'w') as f:
        json.dump({'count': count}, f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/counter', methods=['GET'])
def get_counter():
    count = load_counter()
    return jsonify({'count': count})

@app.route('/counter', methods=['POST'])
def increment_counter():
    count = load_counter() + 1
    save_counter(count)
    return jsonify({'count': count})

if __name__ == '__main__':
    app.run(debug=True)
