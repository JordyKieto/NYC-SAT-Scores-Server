from flask import jsonify
from functools import wraps
import pdb

def formatResponse(func):
    @wraps(func)
    def wrapper():
        res = func() if func.__name__ == 'send_matrix' else jsonify(func())
        res.headers.add('Access-Control-Allow-Origin', '*')
        return res
    return wrapper
