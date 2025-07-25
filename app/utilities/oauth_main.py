# from flask import Flask, redirect, request, jsonify
# from oauth_uti import get_google_auth_url, exchange_code_for_token, get_user_info, register_or_login_user

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return '<a href="/login">Login with Google</a>'

# @app.route("/login")
# def login():
#     return redirect(get_google_auth_url())

# @app.route("/callback")
# def callback():
#     code = request.args.get("code")
#     if not code:
#         return "Missing code", 400

#     tokens = exchange_code_for_token(code)
#     access_token = tokens.get("access_token")
#     if not access_token:
#         return "Failed to get access token", 400 

#     user_info = get_user_info(access_token)
#     redis_key = register_or_login_user(user_info)

#     return jsonify({
#         "message": "User logged in",
#         "email": user_info["email"],
#         "redis_key": redis_key
#     })

# if __name__ == "__main__":
#     app.run(debug=True)
