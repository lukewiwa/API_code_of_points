""" Models for database objects """
import os
from urllib.parse import urlparse
from pony.orm import Database, Required, sql_debug

class Db(Database):
    """
    Subclass database to add seperate prod and test connections
    """
    def conn(self, env="test", debug=False):
        """
        Return prod or test DB connections
        """
        if env == "prod":
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
                '../code_of_points.sqlite',
                create_db=True,
            )
            sql_debug(debug)

        self.generate_mapping(create_tables=True)

db = Db()

class Skill(db.Entity):
    """ Skill database entity """
    app = Required(str)
    eg = Required(int)
    value = Required(str)
    index = Required(int)
    description = Required(str)
