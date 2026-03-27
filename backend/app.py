from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
# Enable CORS so the Express frontend can securely send requests to the Flask backend
CORS(app)

@app.route("/api/test")
def test():
    return "Working"

@app.route('/submit', methods=['POST'])
def handle_submission():
    data = request.get_json()
    
    if not data:
        return jsonify({"error": "No data provided"}), 400
        
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')
    
    print(f"Received form submission:")
    print(f"  Name: {name}")
    print(f"  Email: {email}")
    print(f"  Message: {message}")
    
    return jsonify({
        "status": "success",
        "message": f"Hello {name}, your submission has been processed by the Flask backend!"
    }), 200

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)