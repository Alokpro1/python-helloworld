from time import asctime
from flask import Flask, json
import logging
app = Flask(__name__)


logging.basicConfig(filename='app.log', level=logging.DEBUG, datefmt='%Y-%m-%d %H:%M:%S')


@app.route("/")
def hello():
    app.logger.info(f'{(asctime())} root endpoint was reached.')
    return "Hello World!"

@app.route("/status")
def status():
    app.logger.info(f'{asctime()} status endpoint was reached.')
    response = app.response_class(
        response=json.dumps({"result" : "OK - healthy"}),
        status=200,
        mimetype='application/json'
    )

    return response

@app.route("/metrics")
def metrics():
    
    app.logger.info(f'{(asctime())} metrics endpoint was reached.')
    response = app.response_class(
        response=json.dumps({"status":"success","code":0,"data":{"UserCount": 140, "UserCountActive":23}}),
        status=200,
        mimetype='application/json'
    )

    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
