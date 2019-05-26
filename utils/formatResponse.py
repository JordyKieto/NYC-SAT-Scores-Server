from flask import jsonify

def formatResponse(data):
    res = jsonify(data)
    res.headers.add('Access-Control-Allow-Origin', '*')
    return res
