from flask import Flask, jsonify, request
from user_info_manager import save_user_info

app = Flask(__name__)

@app.route('/api/hello', methods=['GET'])
def hello_world():
    return jsonify(message="Hello, World!")

@app.route('/api/save_user_info', methods=['POST'])
def save_user_info_route():
    user_info = request.json
    save_user_info(user_info)
    return jsonify(message="User information saved successfully")

if __name__ == '__main__':
    app.run(debug=True)
