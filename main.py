from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify(message='Welcome to my API!')

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    return jsonify(message='User created!', data=data)

if __name__ == '__main__':
    app.run(debug=True)
