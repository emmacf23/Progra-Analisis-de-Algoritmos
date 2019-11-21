from flask import Flask, jsonify, render_template, request, redirect, url_for, Response
from Test import reinar, getData

app = Flask(__name__)


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers',
                         'Origin, X-Requested-With, Content-Type, Accept, Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response


@app.route("/run/", methods=["GET"])
def run():
    if request.method == 'GET':
        return jsonify({'trees': getData()})
    return jsonify({'data': 'Hello World!'})


@app.route("/test/", methods=["GET", "POST", "OPTIONS"])
def test():
    if request.method == 'POST':
        duration = request.json['time']
        print("Duracion", duration)
        results = reinar(int(duration))
        return jsonify({'order': results[0]})
    return jsonify({'data': 'Hello World!'})
