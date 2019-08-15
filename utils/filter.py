import os, sys
import sqlite3
from sqlite3 import Error
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common import conditional_map
from .formatScores import formatScores

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
        return {"math": row[0][0], "reading": row[0][1], "writing": row[0][2]}
    
    def byScore(self, score, conditional, subject):
        condition = conditional_map[conditional]
        sql = f""" 
        SELECT name, {subject.lower()}_score, percent_black, percent_asian, percent_white, percent_hispanic, percent_other
        from schools
        WHERE {subject.lower()}_score{condition}{score}
        """
        curr = self.conn.cursor()
        curr.execute(sql)
        rows = curr.fetchall()
        return formatScores(rows)
