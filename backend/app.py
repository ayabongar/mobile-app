from flask import Flask, request, jsonify
import sqlite3
from face_recognition import encode_face, verify_face

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    face_image = request.files['face_image']
    face_encoding = encode_face(face_image)

    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("INSERT INTO users (username, password, face_encoding) VALUES (?, ?, ?)",
              (username, password, face_encoding))
    conn.commit()
    conn.close()

    return jsonify({"message": "User registered successfully!"}), 201

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    face_image = request.files['face_image']

    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT face_encoding FROM users WHERE username=?", (username,))
    user = c.fetchone()
    conn.close()

    if user and verify_face(user[0], face_image):
        return jsonify({"message": "Login successful!"}), 200
    return jsonify({"message": "Login failed!"}), 401

if __name__ == '__main__':
    app.run(debug=True)
