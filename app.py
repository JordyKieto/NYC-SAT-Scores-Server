from flask import Flask, jsonify, request
import pandas as pd
import math

scores = pd.read_csv('scores.csv')

def filterBySubject(subject):
        data = {
                'scores': 
                        {'black': [], 'asian':[], 'white':[], 'hispanic':[], 
                }, 
                'schools': 
                        []
        }

        i = 0
        subjectStr = 'Average Score (SAT ' + subject + ')'
        print(subjectStr)
        for index, row in scores.iterrows():
                if not pd.isnull(row['Percent Black']) and not pd.isnull(row[subjectStr]) and not pd.isnull(row['Percent White']) and not pd.isnull(row['Percent Asian']):
                        data['scores']['black'].append({'x': row['Percent Black'].strip('%'), 'y': row[subjectStr], 'index': i})
                        data['scores']['asian'].append({'x': row['Percent Asian'].strip('%'), 'y': row[subjectStr], 'index': i})
                        data['scores']['white'].append({'x': row['Percent White'].strip('%'), 'y': row[subjectStr], 'index': i})
                        data['scores']['hispanic'].append({'x': row['Percent Hispanic'].strip('%'), 'y': row[subjectStr], 'index': i})
                        data['schools'].append(row['School Name'])
                        i += 1
        return data

def filterBySchool(school):
        currentSchool = scores[scores['School Name'] == school].iloc[0]
        return {
                'math': currentSchool['Average Score (SAT Math)'],
                'reading': currentSchool['Average Score (SAT Reading)'],
                'writing': currentSchool['Average Score (SAT Writing)'],
        }

app = Flask(__name__)

@app.route("/scores")
def send_scores():
    if 'subject' in request.args:
        response = jsonify(filterBySubject(request.args.get('subject')))
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    elif 'school' in request.args:
        response = jsonify(filterBySchool(request.args.get('school')))
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response