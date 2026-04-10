from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({"message": "Welcome to NoteKeeper API", "version": "1.0.0"})

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

@app.route("/notes", methods=["GET"])
def get_notes():
    return jsonify({"notes": []})

@app.route("/notes", methods=["POST"])
def create_note():
    data = request.get_json()
    if not data or "title" not in data:
        return jsonify({"error": "title is required"}), 400
    return jsonify({"message": "Note created"}), 201

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5000)
