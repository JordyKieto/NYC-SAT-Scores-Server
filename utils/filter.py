import sqlite3
from sqlite3 import Error
from common import conditional_map
from . import formatScores, formatScore
import pdb

class Filter:
    def __init__(self, db_file):
        try:
                self.conn = sqlite3.connect(db_file, check_same_thread=False)
                print(sqlite3.version)
        except Error as e:
                print(e)

    def bySubject(self, subject):
        sql = f""" 
        SELECT name, {subject.lower()}_score, percent_black, percent_asian, percent_white, percent_hispanic, percent_other 
        from schools 
        """
        curr = self.conn.cursor()
        curr.execute(sql)
        rows = curr.fetchall()
        return formatScores(rows)

    def bySchool(self, school):
        sql = """ 
        SELECT math_score, reading_score, writing_score from schools 
        WHERE name=?
        """
        curr = self.conn.cursor()
        curr.execute(sql, (school,))
        row = curr.fetchall()
        return formatScore(row)
    
    def byScore(self, req_args):
        condition = conditional_map[req_args['conditional']]
        subject = req_args['subject'].lower()
        sql = f""" 
        SELECT name, {subject}_score, percent_black, percent_asian, percent_white, percent_hispanic, percent_other
        from schools
        WHERE {subject}_score{condition}{req_args['score']}
        """
        curr = self.conn.cursor()
        curr.execute(sql)
        rows = curr.fetchall()
        return formatScores(rows)
