from flask import jsonify, request, render_template
from flask_pymongo import PyMongo
from pymongo import ReturnDocument

from todo import JSONEncoder, app

app.json_encoder = JSONEncoder


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', app_name=app.name, app_author=app.config['AUTHOR'])


@app.route('/api/todo/', methods=['POST'])
@app.route('/api/todo/<int:id>', methods=['GET'])
def todo(id=None):
    mongo = PyMongo(app)
    if request.method == 'GET':
        doc = mongo.db.todos.find_one({"id": id})
        return jsonify({} if doc is None else {i: doc[i] for i in doc if i != '_id'}), 200
    elif request.method == 'POST':
        data = request.get_json()
        user_id = data.get("userId", None)
        title = data.get("title", None)
        completed = data.get("completed", None)
        if user_id is None or title is None or completed is None:
            err = {"message": "Bad request parameters"}
            return jsonify(err), 400
        else:
            todo_id = mongo.db.counters.find_one_and_update({"_id": "todo"}, {"$inc": {"seq": 1}},
                                                            return_document=ReturnDocument.AFTER)['seq']
            doc = {"id": todo_id, "userId": user_id, "title": title, "completed": completed}
            mongo.db.todos.insert_one(doc)
        return jsonify({i: doc[i] for i in doc if i != '_id'}), 200
