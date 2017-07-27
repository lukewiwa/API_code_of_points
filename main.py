from bottle import run, debug, get, HTTPError, error, request, response, app
from pony.orm import db_session, select
from schemas import db, Skill
import json
import os

db.conn()
app = app()

@get("/")
@get("/skills")
@db_session
def skills():
    query = dict(request.query)
    skills = select(s for s in Skill).filter(**query)
    skills = (s.to_dict() for s in skills)
    result = {"skills": list(skills)}
    return result

@get('/test')
def test():
    query = dict(request.query)
    return query

@error(404)
def error404(error):
    error_data = {'success' : False}
    response.content_type = 'application/json'
    return json.dumps(error_data)


if __name__ == "__main__":
    if os.environ.get('APP_LOCATION') == 'heroku':
        run(
            app=app,
            server='gunicorn',
            host="0.0.0.0",
            port=int(os.environ.get("PORT", 5000)),
        )
    else:
        debug(True)
        run(app=app, server='gunicorn', host='localhost', reloader=True)

