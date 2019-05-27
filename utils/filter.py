import pandas as pd

rowCols = ['Percent Black', 'Percent White', 'Percent Asian', 'Percent Hispanic']
subjects = ['math', 'reading', 'writing']
subjectCols = ['Average Score (SAT Math)', 'Average Score (SAT Reading)', 'Average Score (SAT Writing)']
neededCols = [rowCols[:1][0], 'Average Score (SAT Math)']
races = ['black', 'white', 'asian', 'hispanic', 'other']

class Filter:
    def __init__(self, scores):
            for col in neededCols:
                scores = scores[pd.notnull(scores[col])]
            self.scores = scores

    def bySubject(self, subject):
        responseData = {
        "scores": { "black": [], "asian": [], "white": [], "hispanic": [], "other": [] },
        "schools": []
        }
        subjectStr = 'Average Score (SAT ' + subject + ')'
        def appendValues(data, values, i):
                percentOther = 100
                for index, race in enumerate(races):
                        if race == 'other':
                                if percentOther < 0:
                                        percentOther = 0
                                data['scores'][race].append({'x': percentOther, 'y': values['score'], 'index': i})
                        else:
                                percentOther -= values[rowCols[index]]
                                data['scores'][race].append({'x': values[rowCols[index]], 'y': values['score'], 'index': i})
                data['schools'].append(values['school'])
                return data

        def extractValues(row, subject):
                rowData = {}
                for col in rowCols:
                        rowData[col] = float(row[col].strip('%'))
                rowData['school'] = row['School Name']
                rowData['score'] = row[subject]
                return rowData

        for index, row in self.scores.iterrows():
                        appendValues(responseData, extractValues(row, subjectStr), index)
        return responseData
    
    def bySchool(self, school):
        response = {}
        currentSchool = self.scores[self.scores['School Name'] == school].iloc[0]
        for index, sub in enumerate(subjects):
                response[sub] = currentSchool[subjectCols[index]]
        return response