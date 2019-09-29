from flask import Flask, request, send_file
from utils import Filter, formatResponse, formatPredictionInput
import pickle

filter = Filter('pythonsqlite.db')
app = Flask(__name__)
# sat_model = pickle.load(open('primary_sat_model.sav', 'rb'))

@app.route("/scores")
@formatResponse
def send_scores():
    if all(arg in request.args for arg in ['score','conditional','subject']):
        return filter.byScore(request.args)
    elif 'subject' in request.args:
        return filter.bySubject(request.args['subject'])
    elif 'school' in request.args:
        return filter.bySchool(request.args['school'])

@app.route("/matrix")
@formatResponse
def send_matrix():
    res = send_file('matrix.svg', mimetype="image/svg+xml")
    return res

# @app.route("/predict")
# @formatResponse
# def predict():
#     input = formatPredictionInput(request.args)
#     prediction = sat_model.predict(input)
#     return list(prediction)