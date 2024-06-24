from flask import Flask, request, jsonify
import sqlite3
from face_recognition import encode_face, verify_face
from bcrypt import hashpw, gensalt, checkpw

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    face_image = request.files['face_image']
    face_encoding = encode_face(face_image)
    hashed_password = hashpw(password.encode('utf-8'), gensalt())

    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("INSERT INTO users (username, password, face_encoding) VALUES (?, ?, ?)",
              (username, hashed_password, face_encoding))
    conn.commit()
    conn.close()

    return jsonify({"message": "User registered successfully!"}), 201

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    face_image = request.files['face_image']

    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT password, face_encoding FROM users WHERE username=?", (username,))
    user = c.fetchone()
    conn.close()

    if user and checkpw(password.encode('utf-8'), user[0]) and verify_face(user[1], face_image):
        return jsonify({"message": "Login successful!"}), 200
    return jsonify({"message": "Login failed!"}), 401

@app.route('/register_driver', methods=['POST'])
def register_driver():
    name = request.form['name']
    vehicle = request.form['vehicle']

    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("INSERT INTO drivers (name, vehicle) VALUES (?, ?)", (name, vehicle))
    conn.commit()
    conn.close()

    return jsonify({"message": "Driver registered successfully!"}), 201

@app.route('/request_ride', methods=['POST'])
def request_ride():
    username = request.form['username']
    destination = request.form['destination']

    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM drivers")  # Simplified logic for demo
    drivers = c.fetchall()
    conn.close()

    if drivers:
        return jsonify({"message": f"Ride requested for {username} to {destination}. Driver found!"}), 200
    return jsonify({"message": "No drivers available at the moment."}), 404

if __name__ == '__main__':
    app.run(debug=True)
