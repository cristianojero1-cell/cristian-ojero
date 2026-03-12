from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample student data
student = {
    "name": "Cristian Ojero",
    "grade": 11,
    "section": "Firebase"
}

# Home route
@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "message": "Welcome to my Flask API!"
    })

# Get student information
@app.route('/student', methods=['GET'])
def get_student():
    return jsonify(student), 200

# Update student information
@app.route('/student', methods=['POST'])
def update_student():

    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    data = request.get_json()

    # Update fields if provided
    student["name"] = data.get("name", student["name"])
    student["grade"] = data.get("grade", student["grade"])
    student["section"] = data.get("section", student["section"])

    return jsonify({
        "message": "Student updated successfully",
        "student": student
    }), 200


if __name__ == "__main__":
    app.run(debug=True)
