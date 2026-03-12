from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample student data
student = {
    "name": "Cristian Ojero",
    "grade": 10,
    "section": "Firebase"
}

# Home route
@app.route('/')
def home():
    return "Welcome to my Flask API!"

# Get student information
@app.route('/student', methods=['GET'])
def get_student():
    return jsonify(student)

# Update student information
@app.route('/student', methods=['POST'])
def update_student():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data provided"}), 400

    # Update fields if they exist in request
    if "name" in data:
        student["name"] = data["name"]
    if "grade" in data:
        student["grade"] = data["grade"]
    if "section" in data:
        student["section"] = data["section"]

    return jsonify({
        "message": "Student updated successfully",
        "student": student
    })

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
