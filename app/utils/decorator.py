from functools import wraps
from flask import jsonify
import json
from flask_jwt_extended import verify_jwt_in_request,get_jwt_identity

def jwt_required(fn):
    @wraps(fn)
    def warpeds(*args,**kwargs):
        try:
            verify_jwt_in_request
            return fn(*args,**kwargs)
        except Exception as e:
            jsonify({"error":str(e)}),403
        return warpeds
    
    
def roles_required(roles=[]):
    def decorator(fn):
        @wraps(fn)
        def warpeds(*args,**kwargs):
            try:
                verify_jwt_in_request
                user=get_jwt_identity()
                user_roles=json.loads(user.get("roles",[]))
                if set(roles).intersection(user_roles):
                    return fn(*args,**kwargs)
                else:
                    return jsonify({"error":"roles no encontrados"}),403
            except Exception as e:
                jsonify({"error":str(e)}),401
            return warpeds
        return decorator
                