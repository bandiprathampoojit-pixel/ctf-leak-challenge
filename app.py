from flask import Flask, jsonify, request
import time

app = Flask(__name__)
START_TIME = time.time()

@app.route("/")
def index():
    return jsonify({"message": "Welcome to NoteKeeper API", "version": "1.0.0", "status": "running"})

@app.route("/health")
def health():
    uptime = round(time.time() - START_TIME, 2)
    return jsonify({"status": "ok", "uptime_seconds": uptime})

@app.route("/notes", methods=["GET"])
def get_notes():
    # TODO: connect to real database
    return jsonify({"notes": [
        {"id": 1, "title": "Buy groceries", "body": "Milk, eggs, bread"},
        {"id": 2, "title": "Meeting",       "body": "3pm standup"},
    ]})

@app.route("/notes", methods=["POST"])
def create_note():
    data = request.get_json()
    if not data or "title" not in data:
        return jsonify({"error": "title is required"}), 400
    return jsonify({"message": "Note created", "title": data["title"]}), 201

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5000)
