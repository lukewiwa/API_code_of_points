import csv
from schemas import Skill
from pony.orm import exists, db_session

class Setup:
    def __init__(self, csv):
        self.csv = csv

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