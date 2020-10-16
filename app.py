from flask import make_response, jsonify, Flask, request
import sqlite3

app = Flask(__name__)

@app.route('/api/todo/<int:id>', methods=['GET', 'POST'])
def todo(id):
    conn = sqlite3.connect('rest.db',isolation_level=None)
    c = conn.cursor()
    if request.method == 'GET':
        c.execute('SELECT * FROM todos WHERE id = %s' % id)
        todo_data = c.fetchone()
        res = make_response(jsonify(todo_data))
        res.mimetype = 'application/json'
        c.close()
        conn.close()
        return res
    elif request.method == 'POST':
        payload = request.get_json()
        sql = 'INSERT INTO todos (description) VALUES ("{0}")'.format(payload['description'])
        c.execute(sql)
        c.close()
        conn.close()
        return make_response(jsonify(c.lastrowid))

if __name__ == '__main__':
    app.run()
