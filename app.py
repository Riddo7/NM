from flask import Flask, render_template, jsonify
import random
import time

app = Flask(__name__)

def measure_distance():
    # Simulate a random distance between 5 and 100 cm
    return round(random.uniform(5, 100), 2)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sensor')
def sensor():
    dist = measure_distance()
    status = "Moving Forward" if dist > 20 else "Turning"
    return jsonify({'distance': dist, 'status': status})

if __name__ == '__main__':
    app.run(debug=True)
