
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common import races, raceToIndex
import pdb
from functools import reduce

def formatScores(scores):
    responseData = {
        "scores": { "black": [], "asian": [], "white": [], "hispanic": [], "other": [] },
        "schools": []
    }
    def helper(acc, index):
        acc['schools'] += [scores[index][0]]
        for race in races:
                acc['scores'][race] += [({'x': scores[index][raceToIndex[race]], 'y': scores[index][1], 'index': index})]
        return acc
    return reduce(helper, range(len(scores)), responseData)