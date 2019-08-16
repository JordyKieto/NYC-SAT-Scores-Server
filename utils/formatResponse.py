from flask import jsonify
from functools import wraps
import pdb

def formatResponse(func):
    # pdb.set_trace()
    @wraps(func)
    def wrapper():
        # pdb.set_trace()
        res = func() if func.__name__ == 'send_matrix' else jsonify(func())
        res.headers.add('Access-Control-Allow-Origin', '*')
        return res
    return wrapper
