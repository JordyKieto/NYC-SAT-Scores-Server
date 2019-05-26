import pytest
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import app

@pytest.fixture
def client():
    return app.app.test_client()

def test_subjectQuery(client):
    data = client.get('/scores?subject=Math').get_json()
    assert ('scores' in data and 'schools' in data) == True

def test_schoolQuery(client):
    data = client.get('/scores?school=Essex Street Academy').get_json()
    assert data['math'] == 395.0
    assert data['writing'] == 387.0
    assert data['reading'] == 411.0