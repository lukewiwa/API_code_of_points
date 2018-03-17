from boddle import boddle
from main import skills
from bottle import response
from test.setup import db_conn, database

def test_skills(db_conn, database):
    route = skills()
    assert response.status_code == 200
    assert route["skills"][0]["app"] == "Floor Exercise"
