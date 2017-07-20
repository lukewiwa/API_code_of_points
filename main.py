from bottle import run, debug, get, HTTPError, error, request, response
import json

@get("/")
@get("/skills")
def skills():
    return {"hello": "world"}

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
        sql_debug(True)
        debug(True)
        run(app=app, server='gunicorn', host='localhost', reloader=True)

