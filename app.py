from flask import Flask, render_template, jsonify
import json
import os

app = Flask(__name__)

def load_data():
    try:
        with open('data/mock_data.json') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

@app.route('/')
def dashboard():
    return render_template('dashboard.html', page='overview')

@app.route('/transactions')
def transactions():
    return render_template('transactions.html', page='transactions')

@app.route('/alerts')
def alerts():
    return render_template('alerts.html', page='alerts')

@app.route('/system_health')
def system_health():
    return render_template('system_health.html', page='system_health')

@app.route('/settings')
def settings():
    return render_template('settings.html', page='settings')

@app.route('/api/data')
def api_data():
    return jsonify(load_data())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
