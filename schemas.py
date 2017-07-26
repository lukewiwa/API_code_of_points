from pony.orm import *
from urllib.parse import urlparse
import os

db = Database()

if os.environ.get("APP_LOCATION") == "heroku":
    url = urlparse(os.environ["DATABASE_URL"])
    db.bind(
        'postgres',
        user=url.username,
        password=url.password,
        host=url.hostname,
        database=url.path[1:],
    )
else:
    db.bind(
        'sqlite',
        '../code_of_points.db',
        create_db=True,
    )

class Skill(db.Entity):
    app = Required(str)
    eg = Required(str)
    value = Required(str)
    index = Required(int)
    description = Required(str)
