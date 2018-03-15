import csv
from modules.schemas import db, Skill
from pony.orm import db_session, exists
import pytest

class Setup:
    def __init__(self, csv_file):
        self.csv = csv_file

    def get_skills(self):
        with open(self.csv) as file:
            skills = csv.DictReader(file)
            for skill in skills:
                yield skill

    def populate(self):
        with db_session:
            if not exists(s for s in Skill):
                for i in self.get_skills():
                    Skill(**i)

@pytest.fixture(scope="session")
def db_conn():
    try:
        db.conn(env="test")
    except TypeError:
        pass
    yield db

@pytest.fixture(scope="function")
def database():
    setup = Setup("./code_of_points_MAG_2020.csv")
    db.drop_all_tables(with_all_data=True)
    db.create_tables()
    setup.populate()
    yield db
