import flask
import lib
from json import dumps, loads

DEFAULT_PORT = 8000

app = flask.Flask('series-server')
series = lib.SeriesList()

'''''''''''''''''''''''''''''''''POST'''''''''''''''''''''''''''''''''
@app.route('/add', methods=['POST'])
def add_series():
    series.add_series(flask.request.args['name'], flask.request.args['size'])
    return "ok"

@app.route('/add2see', methods = ['POST'])
def add_to_see():
    name = flask.request.args['name']
    return series.add_to_see(name)

@app.route('/add2watched', methods = ['POST'])
def add_watched():
    name = flask.request.args['name']
    return series.add_watched(name)

'''''''''''''''''''''''''''''''''POST-GET'''''''''''''''''''''''''''''''''

@app.route('/episode', methods = ['POST', 'GET'])
def watch_episode():
    if flask.request.method == 'POST':
        name, num = flask.request.args['name'], flask.request.args['num']
        return series.watch_episode(name, int(num))

    else:
        name = flask.request.form['name']
        return series.get_next_ep(name)

@app.route('/raiting', methods = ['POST', 'GET'])
def raiting():
    if flask.request.method == 'POST':
        name, rait= flask.request.args['name'], flask.request.args['rait']
        return series.set_raiting(name, int(rait))

    else:
        name = flask.request.form['name']
        return series.get_raiting(name)


'''''''''''''''''''''''''''''''''GET'''''''''''''''''''''''''''''''''
@app.route('/generator', methods = ['GET'])
def gen_series():
    return lib.generator_series(series)

@app.route('/2see', methods = ['GET'])
def get_to_see():
    return dumps(series.get_to_see())

@app.route('/watched', methods = ['GET'])
def get_watched():
    return dumps(series.get_watched())

'''''''''''''''''''''''''''''''''OTHER'''''''''''''''''''''''''''''''''
def main():
    app.run('::', port = DEFAULT_PORT)


if __name__ == '__main__':
    main()
