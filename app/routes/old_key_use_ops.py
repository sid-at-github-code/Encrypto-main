# import redis
# import os 
# from dotenv import load_dotenv 

# from ..logics import encoder
# from ..logics import finalandsigner

# from flask import Blueprint, jsonify,request

# use_kv_bp = Blueprint("new_kv_bp", __name__)

# @use_kv_bp.route("/useold-kvgen", methods=["POST"])
# def submitnewkv():
#     #step 0 
#     new_key=request.form.get("key")
#     new_msg=request.form.get("msg")
    
#     # step 1 - using a dict stored in db 
#     load_dotenv()
#     my_redis_url = os.environ.get("REDIS_URL")
#     if not my_redis_url:
#         raise ValueError("Unable to fetch or access the Redis URL from environment variables.")

#     r = redis.Redis.from_url(my_redis_url)
    
#     dirty_pass_dict = r.hgetall(new_key)
#     if not dirty_pass_dict:
#         return jsonify({"error": "key not found, generate new "}), 404
#     pass_dict = {k.decode(): v.decode() for k, v in dirty_pass_dict.items()}
     
    
#     #step 2  - getting teh msg encoded  
#     encoded_msg=encoder(new_msg,pass_dict)
    
#     # Step 3 and 4: Redis operations
#     try:
#         # Get hash and redis key for encoded message
#         hash_to_user = finalandsigner(encoded_msg)

#         # Store the encoded message mapping
#         r.set(hash_to_user,encoded_msg,ex=86400)

#     except redis.ConnectionError:
#         return jsonify({"error": "Failed to connect to Redis."}), 500

#     except redis.RedisError as e:
#         return jsonify({"error": f"Redis error: {str(e)}"}), 500

#     except Exception as e:
#         return jsonify({"error": f"Unexpected error: {str(e)}"}), 500

    
#     #step 5 - return the hashed signed jey to user for open msg 
#     return jsonify({"status":"recieved",
#                     "your_set_key":f"{new_key} expires after 30 days ",
#                     "user_h_s_msg":hash_to_user,
#                     "note":"msg is deleted after recieved, if not then auto-deleted in 24-hrs "})
