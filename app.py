from flask import Flask, render_template, jsonify, redirect, url_for
import json

app = Flask(__name__)

def load_data():
    try:
        with open('data/mock_data.json') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# Home redirects to login
@app.route('/')
def home():
    return redirect(url_for('login'))

# Login page
@app.route('/login')
def login():
    return render_template('login.html')

# Password reset page
@app.route('/password_reset')
def forgot_password():
    return render_template('password_reset.html')

# Dashboard page
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', page='overview')

# Transactions page
@app.route('/transactions')
def transactions():
    return render_template('transactions.html', page='transactions')

# Alerts page
@app.route('/alerts')
def alerts():
    return render_template('alerts.html', page='alerts')

# System Health page
@app.route('/system_health')
def system_health():
    return render_template('system_health.html', page='system_health')

# Settings page
@app.route('/settings')
def settings():
    return render_template('settings.html', page='settings')

# API endpoint
@app.route('/api/data')
def api_data():
    return jsonify(load_data())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
