import sqlite3
from sqlite3 import Error
races = ['black', 'white', 'asian', 'hispanic', 'other']
raceToIndex = {'black': 2, 'asian': 3, 'white': 4, 'hispanic': 5, 'other': 6}

class Filter:
    def __init__(self, db_file):
        try:
                self.conn = sqlite3.connect(db_file, check_same_thread=False)
                print(sqlite3.version)
        except Error as e:
                print(e)

    def bySubject(self, subject):
        responseData = {
        "scores": { "black": [], "asian": [], "white": [], "hispanic": [], "other": [] },
        "schools": []
        }
        sql = f""" 
        SELECT name, {subject.lower()}_score, percent_black, percent_asian, percent_white, percent_hispanic, percent_other 
        from schools 
        """
        curr = self.conn.cursor()
        curr.execute(sql)
        rows = curr.fetchall()
        for index, row in enumerate(rows):
                responseData['schools'].append(row[0])
                for race in races:
                        responseData['scores'][race].append({'x': row[raceToIndex[race]], 'y': row[1], 'index': index})
                
        return responseData

    def bySchool(self, school):
        sql = """ 
        SELECT math_score, reading_score, writing_score from schools 
        WHERE name=?
        """
        curr = self.conn.cursor()
        curr.execute(sql, (school,))
        row = curr.fetchall()
        return {"math": row[0][0], "reading": row[0][1], "writing": row[0][2]}