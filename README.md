mkdir REST
cd REST
python -m venv venv

venv\Scripts\activate
# shell should now show the activated enviroment

create .gitignore with

venv/
.idea/

pip install flask
pip install gunicorn

pip freeze > requirements.txt

create runtime.txt and include the following:
python-3.8.6

create Procfile to include
web: gunicorn app:app

from flask import make_response, jsonify, Flask

app = Flask(__name__)

@app.route('/todo')
def todo():
    data = [{"key1": "value1", "key2": "value2"}];
    res = make_response(jsonify(data));
    res.mimetype = 'application/json'
    return res

if __name__ == '__main__':
    app.run()

web: gunicorn app:app

Flask==1.1.2
gunicorn==20.0.4

python-3.8.6


git init