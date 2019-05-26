import pandas as pd

class Filter:
    def bySubject(scores, subject):
        data = {
                'scores': 
                        {'black': [], 'asian':[], 'white':[], 'hispanic':[], 'other': [],
                }, 
                'schools': 
                        []
        }

        i = 0
        subjectStr = 'Average Score (SAT ' + subject + ')'
        for index, row in scores.iterrows():
                if not pd.isnull(row['Percent Black']) and not pd.isnull(row[subjectStr]) and not pd.isnull(row['Percent White']) and not pd.isnull(row['Percent Asian']):
                        percentBlack = float(row['Percent Black'].strip('%'))
                        percentAsian = float(row['Percent Asian'].strip('%'))
                        percentWhite = float(row['Percent White'].strip('%'))
                        percentHispanic = float(row['Percent Hispanic'].strip('%'))
                        percentOther = 100 - percentBlack - percentAsian - percentWhite - percentHispanic
                        subjectScore = row[subjectStr]
                        if percentOther < 0:
                                percentOther = 0
                        data['scores']['black'].append({'x': percentBlack, 'y': subjectScore, 'index': i})
                        data['scores']['asian'].append({'x': percentAsian, 'y': subjectScore, 'index': i})
                        data['scores']['white'].append({'x': percentWhite, 'y': subjectScore, 'index': i})
                        data['scores']['hispanic'].append({'x': percentHispanic, 'y': subjectScore, 'index': i})
                        data['scores']['other'].append({'x': percentOther, 'y': subjectScore, 'index': i})
                        data['schools'].append(row['School Name'])
                        i += 1
        return data
    
    def bySchool(scores, school):
        currentSchool = scores[scores['School Name'] == school].iloc[0]
        return {
                'math': currentSchool['Average Score (SAT Math)'],
                'reading': currentSchool['Average Score (SAT Reading)'],
                'writing': currentSchool['Average Score (SAT Writing)'],
        }