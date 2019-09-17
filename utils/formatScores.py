from common import races, raceToIndex
from functools import reduce

def formatScores(scores):
    responseData = {
        "scores": {race: [] for race in races},
        "schools": []
    }
    def helper(acc, index):
        acc['schools'] += [scores[index][0]]
        for race in races:
                acc['scores'][race] += [({'x': scores[index][raceToIndex[race]], 'y': scores[index][1], 'index': index})]
        return acc
    return reduce(helper, range(len(scores)), responseData)