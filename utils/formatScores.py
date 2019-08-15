
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common import races, raceToIndex

def formatScores(rows):
    responseData = {
        "scores": { "black": [], "asian": [], "white": [], "hispanic": [], "other": [] },
        "schools": []
    }
    for index, row in enumerate(rows):
            responseData['schools'].append(row[0])
            for race in races:
                    responseData['scores'][race].append({'x': row[raceToIndex[race]], 'y': row[1], 'index': index})
            
    return responseData