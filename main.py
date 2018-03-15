"""Routes for API calls"""
from bottle import run, debug, get, HTTPError, error
from bottle import request, response, app, hook
from pony.orm import db_session, select
from modules.schemas import db, Skill
import json
import os
from test.setup import Setup

app = app()

@hook('after_request')
def enable_cors():
    response.headers['Access-Control-Allow-Origin'] = 'null'
    response.headers['Access-Control-Allow-Methods'] = 'GET'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'

@get("/")
@get("/skills")
@db_session
def skills():
    """ Return JSON of all skills with filtering using query string """
    query = dict(request.query)
    skills = select(s for s in Skill).filter(**query)
    skills = (s.to_dict() for s in skills)
    result = {'success': True, "skills": list(skills)}
    return result

@error(404)
def error404(error):
    error_data = {'success' : False}
    response.content_type = 'application/json'
    return json.dumps(error_data)


if __name__ == "__main__":
    setup = Setup("./test/code_of_points_MAG_2020.csv")
    if os.environ.get('APP_LOCATION') == 'heroku':
        db.conn(env="prod")
        setup.populate()
        run(
            app=app,
            server='gunicorn',
            host="0.0.0.0",
            port=int(os.environ.get("PORT", 5000)),
        )
    else:
        db.conn(env="test", debug=True)
        db.drop_all_tables(with_all_data=True)
        db.create_tables()
        setup.populate()
        debug(True)
        run(app=app, host='localhost', reloader=True)

