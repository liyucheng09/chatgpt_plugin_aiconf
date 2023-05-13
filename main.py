import requests
import time
import json
from datetime import datetime
from flask import Flask, send_from_directory
from flask_cors import CORS

from yaml import Loader, load as yaml_load

app = Flask(__name__)
CORS(app)

@app.get("/logo.png")
def logo():
    return send_from_directory(app.root_path, "logo.png")

@app.get("/.well-known/ai-plugin.json")
def plugin_manifest():
    with open(".well-known/ai-plugin.json") as f:
        return f.read()

@app.get("/openapi.yaml")
def openapi():
    with open("openapi.yaml") as f:
        return f.read()

def update_db():
    confs_yaml_file = requests.get('https://raw.githubusercontent.com/paperswithcode/ai-deadlines/gh-pages/_data/conferences.yml').text
    confs = yaml_load(confs_yaml_file, Loader=Loader)

    global up_coming_conferences
    up_coming_conferences = []
    for conf in confs:
        if 'abstract_deadline' in conf:
            deadline = conf['abstract_deadline']
        elif 'deadline' in conf:
            deadline = conf['deadline']
        try:
            deadline = datetime.strptime(deadline, "%Y-%m-%d %H:%M:%S")
        except:
            deadline = datetime.strptime(deadline, "%Y-%m-%d %H:%M")
        if deadline > datetime.now():
            up_coming_conferences.append(conf)

@app.get("/all")
def all():
    update_db()
    results = []
    # we only need title, year, link, place, sub, and deadline
    for conf in up_coming_conferences:
        result = {}
        result['title'] = conf['title']
        result['year'] = conf['year']
        result['link'] = conf['link']
        result['place'] = conf['place']
        result['sub'] = conf['sub']
        result['deadline'] = conf['deadline']
        results.append(result)
    responses = json.dumps(results)
    return responses

starred_conferences = []
@app.get("/star/<conf_name>")
def star(conf_name):
    update_db()
    for conf in up_coming_conferences:
        if conf['title'] == conf_name:
            starred_conferences.append(conf)
            return "OK"
    return "Not Found"

@app.get("/starred")
def starred():
    results = []
    for conf in starred_conferences:
        result = {}
        result['title'] = conf['title']
        result['year'] = conf['year']
        result['link'] = conf['link']
        result['place'] = conf['place']
        result['sub'] = conf['sub']
        result['deadline'] = conf['deadline']
        results.append(result)
    responses = json.dumps(results)
    return responses

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5023)