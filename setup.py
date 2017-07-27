from schemas import db, Skill
from pony.orm import *
import csv

db.conn()

def get_skills():
    with open("code_of_points_MAG_2020.csv") as file:
        skills = csv.DictReader(file)
        for skill in skills:
            yield skill

@db_session
def populate(gen):
    if not exists(s for s in Skill):
        for i in gen:
            Skill(**i)