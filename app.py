from flask import Flask, jsonify, request

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return "Welcome to my Flask API!"

# Student route
@app.route('/student', methods=['GET'])
def get_student():
    student = {
        "name": "Cristian Ojero",
        "grade": 10,
        "section": "Firebase"
    }
    return jsonify(student)

# Run the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
