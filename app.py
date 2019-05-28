from flask import Flask, request, send_file
import pandas as pd
import math
from utils.filter import Filter
from utils.formatResponse import formatResponse

filter = Filter(pd.read_csv('scores.csv'))

app = Flask(__name__)

@app.route("/scores")
def send_scores():
    if 'subject' in request.args:
        return formatResponse(filter.bySubject(request.args['subject']))
    elif 'school' in request.args:
        return formatResponse(filter.bySchool(request.args['school']))

@app.route("/matrix")
def send_matrix():
    res = send_file('matrix.svg', mimetype="image/svg+xml")
    res.headers.add('Access-Control-Allow-Origin', '*')
    return res
