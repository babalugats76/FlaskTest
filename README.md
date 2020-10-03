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

echo "# FlaskTest" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/babalugats76/FlaskTest.git
git push -u origin main

git push heroku main
should show that 
remote: -----> Discovering process types
remote:        Procfile declares types -> web

(venv) C:\Users\James Colestock\Documents\REST>heroku ps:scale web=1
 »   Warning: heroku update available from 7.26.2 to 7.44.0.
Scaling dynos... done, now running web at 1:Free

https://sleepy-savannah-73999.herokuapp.com/todo
