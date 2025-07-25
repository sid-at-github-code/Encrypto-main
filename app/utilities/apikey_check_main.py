# # app.py or main.py
# from flask import Flask, request, jsonify
# from apikey_uti import generate_api_token, validate_token

# app = Flask(__name__)

# @app.route('/get-token', methods=['POST'])
# def get_token():
#     email = request.form.get("email")
    
#     if not email:
#         return jsonify({"error": "Email is required"}), 400

#     token = generate_api_token(email)
#     return jsonify({"api_token": token})

# @app.route('/protected-endpoint', methods=['GET'])
# def protected():
#     token = request.headers.get('x-api-key')
#     if not token or not validate_token(token):
#         return jsonify({"error": "Unauthorized"}), 401

#     return jsonify({"message": "Success! You are authorized."})


# app.run()
