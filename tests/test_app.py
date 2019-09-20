
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pytest
import app
import pdb
import random
import xml.etree.ElementTree as ET
from common import conditional_map, subjects
from utils import formatScores, formatResponse

@pytest.fixture
def client():
    return app.app.test_client()

def test_subject_query(client):
    data = client.get('/scores?subject=Math').get_json()
    assert all([
                len(data['schools']) > 0, 
                len(data['scores']['black']) == len(data['schools']), 
                ('scores' in data and 'schools' in data)
            ])

def test_school_query(client):
    data = client.get('/scores?school=Essex Street Academy').get_json()
    assert all([
                data['math'] == 395.0, 
                data['writing'] == 387.0, 
                data['reading'] == 411.0
            ])

def test_matrix_query(client):
    data = client.get('/matrix')
    element = ET.fromstring(data.data)
    assert 'svg' in element.tag

def test_score_filter_query(client):
    score = str(random.randint(350, 800))
    conditional = random.choice(list(conditional_map.keys()))
    subject = random.choice(['Math', 'Reading', 'Writing'])
    url = f"/scores?subject={subject}&score={score}&conditional={conditional}"
    data = client.get(url).get_json()['scores']
    data =  data[random.choice(list(data.keys()))]
    if not all(eval(f"{s['y']} {conditional_map[conditional]} {float(score)}") for s in data):
        pdb.set_trace()
    assert all(eval(f"{s['y']} {conditional_map[conditional]} {float(score)}") for s in data)

def test_format_scores():
    row = ('New Explorations into Science, Technology and Math High School', 13.3, 38.5, 28.6, 18.0, 1.6000000000000014, 657.0, 601.0, 601.0)
    result = formatScores([row])
    assert all((isinstance(result['schools'], list), isinstance(result['schools'], list)))

def test_format_response(client):
    with app.app.app_context():
        @formatResponse
        def test_func():
            return ({'height': 100})
        response = test_func()
        assert all([
            str(response.headers) == "Content-Type: application/json\r\nContent-Length: 15\r\nAccess-Control-Allow-Origin: *\r\n\r\n",
            response.is_json,
            response.get_json() == {'height': 100}
        ])

def test_predict_score(client):
    data = client.get("http://127.0.0.1:5000/predict?Percent Black=0&Percent White=0&Percent Asian=50&Percent Hispanic=50&Percent Other=0&Spent Per Student=1000&Student enrollment=100&Manhattan=1&Staten=0&Bronx=0&Queens=0&Brooklyn=0&Math=0&Reading=0&Writing=1").get_json()
    assert data  ==  [417.98115435118456]