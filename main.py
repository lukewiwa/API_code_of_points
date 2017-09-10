from bottle import run, debug, get, HTTPError, error
from bottle import request, response, app, hook
from pony.orm import db_session, select
from schemas import db, Skill
import json
import os
from setup import Setup

db.conn()
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
    setup = Setup("code_of_points_MAG_2020.csv")
    setup.populate()

    if os.environ.get('APP_LOCATION') == 'heroku':
        run(
            app=app,
            server='gunicorn',
            host="0.0.0.0",
            port=int(os.environ.get("PORT", 5000)),
        )
    else:
        debug(True)
        run(app=app, host='localhost', reloader=True)

