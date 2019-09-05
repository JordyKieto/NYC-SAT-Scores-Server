from common import subjects

def formatScore(row):
    return {subj: row[0][i] for i, subj in enumerate(subjects) }