from pony.orm import *
from urllib.parse import urlparse
import os

db = Database()

try:
    url = urlparse(os.environ["DATABASE_URL"])
    db.bind(
        'postgres',
        user=url.username,
        password=url.password,
        host=url.hostname,
        database=url.path[1:],
    )
except KeyError:
    db.bind(
        'sqlite',
        '../code_of_points.db',
        create_db=True,
    )

class Skill(db.Entity):
    # insert skills schema