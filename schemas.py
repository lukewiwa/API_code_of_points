from pony.orm import Database, Required, sql_debug
from urllib.parse import urlparse
import os

class Db(Database):
    def conn(self):
        if os.environ.get("APP_LOCATION") == "heroku":
            url = urlparse(os.environ["DATABASE_URL"])
            self.bind(
                'postgres',
                user=url.username,
                password=url.password,
                host=url.hostname,
                database=url.path[1:],
            )
        else:
            self.bind(
                'sqlite',
                './code_of_points.db',
                create_db=True,
            )
            sql_debug(True)
        
        self.generate_mapping(create_tables=True)

db = Db()

class Skill(db.Entity):
    app = Required(str)
    eg = Required(int)
    value = Required(str)
    index = Required(int)
    description = Required(str)

