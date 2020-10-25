from todo import app
from flask import make_response, jsonify, request, render_template
from pymongo import MongoClient
import os
import sqlite3

author = os.environ.get('AUTHOR', None)
app.config['MONGO_URI'] = os.environ.get('MONGO_URI', None)
client = MongoClient(app.config['MONGO_URI'])
db = client['flask-demo']
#todos = db['todos']

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', app_name=app.name, app_author=author)


@app.route('/api/todo/', methods=['POST'])
@app.route('/api/todo/<int:id>', methods=['GET'])
def todo(id=None):
    conn = sqlite3.connect('rest.db', isolation_level=None)
    conn.row_factory = dict_factory
    c = conn.cursor()
    if request.method == 'GET':
        c.execute("SELECT id, user_id AS userId, title, completed FROM todos WHERE id = %s" % id)
        data = c.fetchone()
        if data is None:
            return make_response(jsonify({}))
        data['completed'] = bool(data['completed'])
        res = make_response(jsonify(data))
        res.mimetype = 'application/json; charset=utf-8'
        c.close()
        conn.close()
        return res
    elif request.method == 'POST':
        payload = request.get_json()
        data = tuple([payload['userId'], payload['title'], (0, 1)[bool(payload['completed'])]])
        sql = 'INSERT INTO todos (user_id, title, completed) VALUES ({0}, "{1}", {2})'.format(*tuple(data))
        c.execute(sql)

        res = make_response(jsonify({
            "id": c.lastrowid,
            "userId": data[0],
            "title": data[1],
            "completed": bool(data[2])
        }))
        res.mimetype = 'application/json; charset=utf-8'
        c.close()
        conn.close()
        return res

