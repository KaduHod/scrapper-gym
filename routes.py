from flask import Flask, redirect
import json

app = Flask(__name__)

@app.route("/workouts/wiki")
def exerciciosWiki():
    file = open('./jsons/exercises-2.json','r').read()
    return file, 200, {'Content-Type': 'application/json;' }

@app.route("/")
def rediredct():
    return redirect('http://127.0.0.1:9999/workouts/wiki')

@app.route("/muscles")
def muscles():
    file = open('./jsons/muscles-2.json','r').read()
    return file, 200, {'Content-Type': 'application/json;' }