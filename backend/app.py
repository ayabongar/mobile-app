from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
from face_recognition import encode_face, verify_face
from bcrypt import hashpw, gensalt, checkpw
import face_recognition
import io
from PIL import Image
import base64

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Initialize the database if not exists
def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        password TEXT NOT NULL,
        face_encoding BLOB,
        role TEXT NOT NULL
    )''')
    conn.commit()
    conn.close()

# Function to connect to the database
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn    

@app.route('/register', methods=['POST'])
def register():
    try:
        username = request.form['username']
        password = request.form['password']
        role = request.form['role']
        face_image = request.form['face_image']

        # Debugging: Log received data
        print(f"Username: {username}")
        print(f"Password: {password}")
        print(f"Role: {role}")
        print(f"Face image length: {len(face_image)}")

        # Convert the image from base64
        face_image_data = base64.b64decode(face_image.split(',')[1])
        image = face_recognition.load_image_file(io.BytesIO(face_image_data))
        face_encoding = face_recognition.face_encodings(image)

        if len(face_encoding) == 0:
            return jsonify({"message": "No face detected!"}), 400
        
        face_encoding = face_encoding[0].tobytes()

        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        conn = get_db_connection()
        conn.execute('INSERT INTO users (username, password, role, face_encoding) VALUES (?, ?, ?, ?)',
                     (username, hashed_password, role, face_encoding))
        conn.commit()
        conn.close()

        return jsonify({"message": "Registration successful!"})
    except Exception as e:
        print(f"Error during registration: {str(e)}")
        return jsonify({"message": "Registration failed!", "error": str(e)}), 500


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    face_image = request.files.get('face_image')
    password = request.form.get('password')

    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT password, face_encoding FROM users WHERE username=?", (username,))
    user = c.fetchone()
    conn.close()

    if not user:
        return jsonify({"message": "Login failed! User not found."}), 401

    if face_image:
        if verify_face(user[1], face_image):
            return jsonify({"message": "Login successful with face recognition!"}), 200
        else:
            return jsonify({"message": "Face recognition failed!"}), 401
    elif password:
        if checkpw(password.encode('utf-8'), user[0]):
            return jsonify({"message": "Login successful with password!"}), 200
        else:
            return jsonify({"message": "Password authentication failed!"}), 401
    else:
        return jsonify({"message": "Login failed! No method of authentication provided."}), 401

@app.route('/request_ride', methods=['POST'])
def request_ride():
    username = request.form['username']
    destination = request.form['destination']

    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE role='driver'")
    drivers = c.fetchall()
    conn.close()

    if drivers:
        return jsonify({"message": f"Ride requested for {username} to {destination}. Driver found!"}), 200
    return jsonify({"message": "No drivers available at the moment."}), 404

if __name__ == '__main__':
    init_db()
    app.run(debug=True)


