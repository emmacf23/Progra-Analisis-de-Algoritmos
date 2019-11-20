from flask import Flask, jsonify, render_template, request, redirect, url_for, Response

from Test import reinar

app = Flask(__name__)


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers',
                         'Origin, X-Requested-With, Content-Type, Accept, Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response


@app.route("/")
def index():
    return "Hola"

@app.route("/run/", methods=["GET", "POST", "OPTIONS"])
def run():
    if request.method == 'POST':
        duration = request.json['time']
        print("Duracion", duration)
        results = reinar(int(duration))
        return jsonify([results])
    return jsonify(["Me cago en todo"])
